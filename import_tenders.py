import os, json, sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")

import django
django.setup()

from apps.public.models import Tender

# Барилгатай холбоотой түлхүүр үгс
CONSTRUCTION_KEYWORDS = [
    "барилга", "засвар", "угсралт", "зураг төсөл", "бетон", "хучилт",
    "дотоод засал", "гадаад засал", "дулаалга", "цахилгаан", "сантехник",
    "хаалга", "цонх", "дээвэр", "суурь", "төлөвлөлт", "инженер",
    "construction", "repair", "building", "зам", "гүүр", "усан хангамж",
    "халаалт", "агааржуулалт", "лифт", "өргөтгөх", "шинэчлэх"
]

with open("tenders.json", "r", encoding="utf-8") as f:
    data = json.load(f)

added = 0
skipped = 0

for item in data:
    url = item.get("url", "")
    if not url:
        skipped += 1
        continue

    # Барилгатай холбоотой эсэх шалгах
    text = (item.get("title", "") + " " + item.get("method", "")).lower()
    is_construction = any(kw in text for kw in CONSTRUCTION_KEYWORDS)

    tender, created = Tender.objects.get_or_create(
        url=url,
        defaults={
            "title": item.get("title", "")[:500],
            "organization": item.get("organization", "")[:300],
            "price": item.get("price", "")[:100],
            "deadline": item.get("deadline", "")[:20],
            "method": item.get("method", "")[:200],
            "tender_code": item.get("tender_code", "")[:100],
            "is_construction": is_construction,
        }
    )
    if created:
        added += 1
    else:
        skipped += 1

print(f"✅ Нэмэгдсэн: {added}")
print(f"⏭ Давхардсан: {skipped}")
print(f"📊 Нийт DB-д: {Tender.objects.count()}")
print(f"🏗 Барилгатай холбоотой: {Tender.objects.filter(is_construction=True).count()}")