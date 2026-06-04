content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''        try:
            area = str(float(length) * float(width)) if length and width else "мэдэгдэхгүй"
        except:
            area = "мэдэгдэхгүй"'''

new = '''        try:
            area = str(float(length) * float(width)) if length and width else "мэдэгдэхгүй"
        except:
            area = "мэдэгдэхгүй"

        # DB-аас үнийн мэдээлэл татах
        from apps.public.models import MaterialPrice
        prices = MaterialPrice.objects.filter(is_active=True).order_by("category", "name")
        price_text = "\\n".join([
            f"- {p.name}: {p.price_min:,}₮-{p.price_max:,}₮ / {p.unit}"
            for p in prices
        ])'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK — үнэ татах код нэмэгдлээ")
else:
    print("NOT FOUND")

# Prompt-д үнэ нэмэх
old2 = '''Монголын 2024-2025 оны үнийн мэдээлэлд үндэслэн ЗӨВХӨН JSON форматаар хариу өгнө үү.'''

new2 = '''Дараах ОДООГИЙН ЗАХ ЗЭЭЛИЙН ҮНИЙГ ЗААВАЛ ашиглана уу:

{price_text}

Эдгээр үнэд үндэслэн ЗӨВХӨН JSON форматаар хариу өгнө үү.'''

if old2 in content:
    content = content.replace(old2, new2, 1)
    print("OK — prompt-д үнэ нэмэгдлээ")
else:
    print("NOT FOUND 2")

open("apps/registry/views.py", "w", encoding="utf-8").write(content)
print("Дууслаа")