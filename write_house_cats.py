import json, os

# Орон сууцны ангиллын өгөгдөл
HOUSE_DATA = {
    "rooms": {
        "label": "🛏 Өрөөний тоо",
        "items": [
            ("r1", "1 өрөө"),
            ("r2", "2 өрөө"),
            ("r3", "3 өрөө"),
            ("r3plus", "3-аас дээш өрөө"),
            ("duplex", "Дуплекс"),
            ("studio", "Студи"),
        ]
    },
    "ub": {
        "label": "🏙 Улаанбаатар",
        "items": [
            ("bgd", "Баянгол дүүрэг"),
            ("bzd", "Баянзүрх дүүрэг"),
            ("sbd", "Сүхбаатар дүүрэг"),
            ("hud", "Хан-Уул дүүрэг"),
            ("chd", "Чингэлтэй дүүрэг"),
            ("shd", "Сонгинохайрхан дүүрэг"),
            ("nld", "Налайх дүүрэг"),
            ("bnd", "Багануур дүүрэг"),
            ("bhd", "Багахангай дүүрэг"),
        ]
    },
    "province": {
        "label": "🗺 Орон нутаг",
        "items": [
            ("arkhangai", "Архангай"),
            ("bayan_olgii", "Баян-Өлгий"),
            ("bayankhongor", "Баянхонгор"),
            ("bulgan", "Булган"),
            ("gobi_altai", "Говь-Алтай"),
            ("govisumber", "Говьсүмбэр"),
            ("darkhan", "Дархан-Уул"),
            ("dornod", "Дорнод"),
            ("dornogobi", "Дорноговь"),
            ("dundgobi", "Дундговь"),
            ("zavkhan", "Завхан"),
            ("orkhon", "Орхон"),
            ("uvurkhangai", "Өвөрхангай"),
            ("umnugobi", "Өмнөговь"),
            ("sukhbaatar", "Сүхбаатар"),
            ("selenge", "Сэлэнгэ"),
            ("tuv", "Төв"),
            ("uvs", "Увс"),
            ("khovd", "Ховд"),
            ("khuvsgul", "Хөвсгөл"),
            ("khentii", "Хэнтий"),
        ]
    },
    "type": {
        "label": "🏷 Зарын төрөл",
        "items": [
            ("sale", "Зарна"),
            ("rent", "Түрээслэнэ"),
            ("buy", "Худалдаж авна"),
            ("rent_partial", "Хэсэгчлэн түрээслэнэ"),
        ]
    }
}

with open("house_cats.json", "w", encoding="utf-8") as f:
    json.dump(HOUSE_DATA, f, ensure_ascii=False, indent=2)
print("OK — house_cats.json үүслээ")

# Ad model-д house талбарууд нэмэх
content = open("apps/public/models.py", "r", encoding="utf-8").read()

addon = '''    house_rooms = models.CharField(
        "Өрөөний тоо", max_length=20, blank=True, default="",
        choices=[
            ("r1", "1 өрөө"),
            ("r2", "2 өрөө"),
            ("r3", "3 өрөө"),
            ("r3plus", "3-аас дээш өрөө"),
            ("duplex", "Дуплекс"),
            ("studio", "Студи"),
        ]
    )
    house_location = models.CharField(
        "Байршил (дүүрэг/аймаг)", max_length=30, blank=True, default=""
    )
    house_location_type = models.CharField(
        "Байршлын төрөл", max_length=10, blank=True, default="",
        choices=[("ub", "Улаанбаатар"), ("province", "Орон нутаг")]
    )
    house_type = models.CharField(
        "Зарын төрөл", max_length=20, blank=True, default="",
        choices=[
            ("sale", "Зарна"),
            ("rent", "Түрээслэнэ"),
            ("buy", "Худалдаж авна"),
            ("rent_partial", "Хэсэгчлэн түрээслэнэ"),
        ]
    )
'''

if "house_rooms" not in content:
    content = content.replace(
        '    contact_name = models.CharField("Холбоо барих нэр"',
        addon + '    contact_name = models.CharField("Холбоо барих нэр"'
    )
    open("apps/public/models.py", "w", encoding="utf-8").write(content)
    print("OK — house талбарууд нэмэгдлээ")
else:
    print("Аль хэдийн байна")