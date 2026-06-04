content = open("apps/registry/views.py", "r", encoding="utf-8").read()

# File upload view нэмэх
file_view = '''

def budget_file_upload(request):
    from django.conf import settings
    result = None
    error = None

    if request.method == "POST":
        import anthropic, openpyxl, json
        from io import BytesIO

        uploaded_file = request.FILES.get("budget_file")
        if not uploaded_file:
            error = "Файл оруулаагүй байна."
        else:
            try:
                # Excel файл унших
                wb = openpyxl.load_workbook(BytesIO(uploaded_file.read()))
                ws = wb.active

                rows_data = []
                for row in ws.iter_rows(values_only=True):
                    if any(cell is not None for cell in row):
                        rows_data.append([str(c) if c is not None else "" for c in row])

                # DB-аас үнэ авах
                from apps.public.models import MaterialPrice
                key_prices = [
                    ("mat_cement", "Цемент"),
                    ("mat_sand", "Элс, хайрга"),
                    ("mat_brick", "Тоосго, блок"),
                    ("mat_rebar", "Арматур"),
                    ("mat_wood", "Мод"),
                    ("mat_insulation", "Дулаалга"),
                    ("mat_window", "Цонх, хаалга"),
                    ("mat_interior", "Дотор засал"),
                    ("mat_plumbing", "Сантехник"),
                    ("mat_electrical", "Цахилгаан"),
                    ("labor_general", "Барилгачин"),
                    ("labor_special", "Мэргэжилтэн"),
                    ("transport_material", "Тээвэр"),
                    ("machine_crane", "Кран"),
                    ("machine_excavator", "Экскаватор"),
                ]
                price_lines = []
                for cat, label in key_prices:
                    items = MaterialPrice.objects.filter(is_active=True, category=cat)[:2]
                    for p in items:
                        price_lines.append(f"- {p.name}: {int(p.price_min):,}₮-{int(p.price_max):,}₮/{p.unit}")
                price_text = "\\n".join(price_lines[:40])

                # Excel өгөгдлийг текст болгох
                excel_text = "\\n".join([" | ".join(row) for row in rows_data[:80]])

                prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн. Дараах Excel файлын өгөгдлөөс барилгын төсвийг тооцоолж өгнө үү.

Excel файлын агуулга:
{excel_text}

Одоогийн зах зээлийн үнэ:
{price_text}

Excel дээр тоо хэмжээ оруулсан бол тэр тоог ашиглана уу.
Тоо хэмжээ байхгүй бол хоосон орхино уу.
Нэгж үнэ байхгүй бол дээрх зах зээлийн үнийг ашиглана уу.

ЗӨВХӨН JSON форматаар хариу өгнө үү:
{{
  "building_info": {{"type": "файлаас авсан барилгын нэр", "area": "талбай", "location": "", "quality": ""}},
  "materials": [{{"name": "нэр", "unit": "нэгж", "qty": тоо, "unit_price": үнэ, "total": нийт}}],
  "labor": [{{"name": "нэр", "unit": "нэгж", "qty": тоо, "unit_price": үнэ, "total": нийт}}],
  "transport": [{{"name": "нэр", "unit": "нэгж", "qty": тоо, "unit_price": үнэ, "total": нийт}}],
  "other": [{{"name": "нэр", "unit": "нэгж", "qty": тоо, "unit_price": үнэ, "total": нийт}}],
  "summary": {{"materials_total": 0, "labor_total": 0, "transport_total": 0, "other_total": 0, "grand_total": 0, "price_per_m2": 0, "duration_months": 0}},
  "notes": "тайлбар"
}}"""

                client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
                message = client.messages.create(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=4000,
                    messages=[{"role": "user", "content": prompt}]
                )
                import re
                raw = message.content[0].text.strip()
                raw = re.sub(r"^```json\\s*", "", raw)
                raw = re.sub(r"^```\\s*", "", raw)
                raw = re.sub(r"\\s*```$", "", raw)
                raw = raw.strip()
                start = raw.find("{")
                end = raw.rfind("}") + 1
                if start >= 0 and end > start:
                    raw = raw[start:end]
                result = json.loads(raw)

            except Exception as e:
                error = f"Алдаа: {str(e)}"

    import json as _json
    result_json = _json.dumps(result, ensure_ascii=False) if result else "{}"
    return render(request, "registry/budget_file.html", {
        "result": result,
        "result_json": result_json,
        "error": error,
        "display_name": get_display_name(request.user),
    })
'''

if "def budget_file_upload" not in content:
    with open("apps/registry/views.py", "a", encoding="utf-8") as f:
        f.write(file_view)
    print("OK — view нэмэгдлээ")

# URL нэмэх
urls = open("apps/registry/urls.py", "r", encoding="utf-8").read()
if "budget_file_upload" not in urls:
    urls = urls.replace(
        "from .views import (\n    budget_calculator,\n    budget_excel,\n    budget_chat,",
        "from .views import (\n    budget_calculator,\n    budget_excel,\n    budget_chat,\n    budget_file_upload,"
    )
    urls = urls.replace(
        'path("budget/chat/", budget_chat, name="budget_chat"),',
        'path("budget/chat/", budget_chat, name="budget_chat"),\n    path("budget/file/", budget_file_upload, name="budget_file_upload"),'
    )
    open("apps/registry/urls.py", "w", encoding="utf-8").write(urls)
    print("OK — URL нэмэгдлээ")

print("Дууслаа")