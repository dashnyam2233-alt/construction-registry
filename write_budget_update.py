# View-г шинэчлэх
content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''        prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн. Дараах барилгын төсвийг тооцоолж өгнө үү.

Барилгын мэдээлэл:
- Төрөл: {building_type}
- Талбай: {area} м²
- Давхар: {floors}
- Байршил: {location}
- Чанарын түвшин: {quality}
- Нэмэлт мэдээлэл: {extra}

Монголын 2024-2025 оны үнийн мэдээлэлд үндэслэн дараах бүтэцтэй тооцоо гаргаж өгнө үү:

1. МАТЕРИАЛЫН ЗАРДАЛ (₮):
   - Бетон, арматур, цемент
   - Тоосго, блок
   - Дээвэр
   - Цонх, хаалга
   - Дотор засал (будаг, шал, тааз)
   - Сантехник, цахилгаан
   - Бусад материал
   
2. АЖИЛЧДЫН ЗАРДАЛ (₮):
   - Барилгачид
   - Инженер, хяналт
   - Тусгай ажилтан
   
3. БУСАД ЗАРДАЛ (₮):
   - Тоног төхөөрөмж түрээс
   - Зураг төсөл
   - Зөвшөөрөл, бүртгэл
   
4. НИЙТ ТӨСӨВ (₮)
5. 1 М² ҮНЭ (₮)
6. БАРИЛГЫН ХУГАЦАА (сар)
7. АНХААРАХ ЗҮЙЛС

Тооцоог тодорхой, задаргаатай, бодитой тоогоор гаргана уу. Монгол хэлээр бичнэ үү."""'''

new = '''        prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн. Дараах барилгын төсвийг тооцоолж өгнө үү.

Барилгын мэдээлэл:
- Төрөл: {building_type}
- Талбай: {area} м²
- Давхар: {floors}
- Байршил: {location}
- Чанарын түвшин: {quality}
- Нэмэлт мэдээлэл: {extra}

Монголын 2024-2025 оны үнийн мэдээлэлд үндэслэн ЗӨВХӨН JSON форматаар хариу өгнө үү. Өөр текст огт бичихгүй.

Дараах JSON бүтцийг яг ийм байдлаар буцаана уу:
{{
  "building_info": {{
    "type": "{building_type}",
    "area": "{area} м²",
    "floors": "{floors}",
    "location": "{location}",
    "quality": "{quality}"
  }},
  "materials": [
    {{"name": "Цемент", "unit": "уут", "qty": 25, "unit_price": 35000, "total": 875000}},
    {{"name": "Элс", "unit": "м³", "qty": 12, "unit_price": 25000, "total": 300000}}
  ],
  "labor": [
    {{"name": "Барилгачид", "unit": "өдөр", "qty": 120, "unit_price": 60000, "total": 7200000}},
    {{"name": "Инженер хяналт", "unit": "сар", "qty": 4, "unit_price": 800000, "total": 3200000}}
  ],
  "other": [
    {{"name": "Тоног төхөөрөмж түрээс", "unit": "сар", "qty": 4, "unit_price": 500000, "total": 2000000}},
    {{"name": "Зураг төсөл", "unit": "удаа", "qty": 1, "unit_price": 1500000, "total": 1500000}}
  ],
  "summary": {{
    "materials_total": 15000000,
    "labor_total": 10000000,
    "other_total": 3500000,
    "grand_total": 28500000,
    "price_per_m2": 407142,
    "duration_months": 5
  }},
  "notes": "Анхаарах зүйлс энд бичнэ"
}}

Бодитой Монголын үнээр тооцоолно уу. ЗӨВХӨН JSON, өөр юу ч бичихгүй."""'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK — prompt шинэчлэгдлээ")
else:
    print("NOT FOUND")

# Result processing нэмэх
old2 = '''            result = message.content[0].text
        except Exception as e:
            error = f"Алдаа гарлаа: {str(e)}"
    
    return render(request, "registry/budget_calculator.html", {
        "result": result,
        "error": error,
        "post_data": request.POST,
        "display_name": get_display_name(request.user),
    })'''

new2 = '''            import json
            raw = message.content[0].text.strip()
            # JSON цэвэрлэх
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            raw = raw.strip()
            try:
                result = json.loads(raw)
            except:
                result = {"error": raw}
        except Exception as e:
            error = f"Алдаа гарлаа: {str(e)}"
    
    return render(request, "registry/budget_calculator.html", {
        "result": result,
        "error": error,
        "post_data": request.POST,
        "display_name": get_display_name(request.user),
    })'''

if old2 in content:
    content = content.replace(old2, new2, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK — result processing нэмэгдлээ")
else:
    print("NOT FOUND 2")

print("Дууслаа")