# View-д chat endpoint нэмэх
content = open("apps/registry/views.py", "r", encoding="utf-8").read()

chat_view = '''

def budget_chat(request):
    from django.conf import settings
    from django.http import JsonResponse
    import anthropic, json

    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    try:
        body = json.loads(request.body)
        messages = body.get("messages", [])
        user_msg = body.get("message", "")
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if not user_msg:
        return JsonResponse({"error": "Хоосон асуулт"}, status=400)

    system_prompt = """Та Монголын барилгын салбарын туршлагатай мэргэжилтэн. 
Барилга барихаар төлөвлөж байгаа хүмүүст практик зөвлөгөө өгнө.

Та дараах мэдлэгтэй:
- Монголын барилгын норм, дүрэм (БНбД)
- Барилгын материал, технологи
- Зөвшөөрөл, бүртгэлийн процесс
- Зураг төсөл, инженерийн шийдэл
- Барилгын компани сонгох зөвлөгөө
- Барилгын хугацаа, зардлын тооцоо
- Монголын цаг уур, газар хөрсний онцлог

Хариултаа товч, практик, Монгол хэлээр өгнө үү. 
Хэрэв тооцоо хийх шаардлагатай бол /budget/ хуудсыг ашиглахыг санал болгоно уу."""

    try:
        client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        
        # Өмнөх яриаг нэмэх
        api_messages = []
        for msg in messages[-10:]:  # Сүүлийн 10 мессеж
            api_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        api_messages.append({"role": "user", "content": user_msg})

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1000,
            system=system_prompt,
            messages=api_messages
        )
        reply = response.content[0].text
        return JsonResponse({"reply": reply})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
'''

if "def budget_chat" not in content:
    with open("apps/registry/views.py", "a", encoding="utf-8") as f:
        f.write(chat_view)
    print("OK — chat view нэмэгдлээ")
else:
    print("Аль хэдийн байна")

# URL нэмэх
urls = open("apps/registry/urls.py", "r", encoding="utf-8").read()
if "budget_chat" not in urls:
    urls = urls.replace(
        "from .views import (\n    budget_calculator,\n    budget_excel,",
        "from .views import (\n    budget_calculator,\n    budget_excel,\n    budget_chat,"
    )
    urls = urls.replace(
        'path("budget/excel/", budget_excel, name="budget_excel"),',
        'path("budget/excel/", budget_excel, name="budget_excel"),\n    path("budget/chat/", budget_chat, name="budget_chat"),'
    )
    open("apps/registry/urls.py", "w", encoding="utf-8").write(urls)
    print("OK — URL нэмэгдлээ")

print("Дууслаа")