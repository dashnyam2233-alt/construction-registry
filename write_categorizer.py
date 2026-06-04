import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()

from apps.public.models import Tender

# Ангиллын түлхүүр үгс
CATEGORIES = {
    "construction": [
        "барилга", "угсралт", "цутгалт", "бетон", "суурь", "хана",
        "дээвэр", "шал", "давхар", "байшин", "орон сууц", "өргөтгөх",
        "шинэ барилга", "building", "construction"
    ],
    "repair": [
        "засвар", "их засвар", "засварлах", "шинэчлэх", "renovation",
        "repair", "сэргээн засварлах", "дотоод засал", "гадаад засал",
        "будаг", "тааз", "шалны"
    ],
    "design": [
        "зураг төсөл", "зураг", "төсөл", "зураг төсөл боловсруулах",
        "ded", "fed", "tod", "дод", "тэзү", "судалгаа", "геодези",
        "геологи", "топограф", "design", "архитектур"
    ],
    "road": [
        "зам", "гүүр", "хучилт", "авто зам", "талбай", "явган",
        "замын", "road", "bridge", "тротуар", "явган зорчигч"
    ],
    "engineering": [
        "цахилгаан", "сантехник", "дулаан", "халаалт", "агааржуулалт",
        "усан хангамж", "ус", "дулаалга", "дулаан хангамж", "хий",
        "лифт", "mechanical", "electrical", "plumbing", "хоолой"
    ],
    "material": [
        "материал", "тоосго", "цемент", "арматур", "хайрга", "элс",
        "төмөр", "мод", "шил", "будаг", "нийлүүлэлт", "бараа",
        "material", "supply", "худалдан авах"
    ],
    "equipment": [
        "тоног төхөөрөмж", "машин", "механизм", "техник", "equipment",
        "machinery", "кран", "экскаватор", "бульдозер", "генератор"
    ],
    "consulting": [
        "зөвлөх", "consulting", "судалгаа", "үнэлгээ", "хяналт",
        "supervision", "monitoring", "аудит", "менежмент"
    ],
    "service": [
        "үйлчилгээ", "ажил", "service", "хөдөлмөр", "ажиллах хүч"
    ],
}

def categorize(title, method, org):
    text = (title + " " + method + " " + org).lower()
    for cat, keywords in CATEGORIES.items():
        if any(kw in text for kw in keywords):
            return cat
    return "other"

# Бүх тендерийг дахин ангилах
tenders = Tender.objects.all()
updated = 0
for t in tenders:
    cat = categorize(t.title, t.method, t.organization)
    is_construction = cat in ["construction", "repair", "design", "road", "engineering"]
    if t.category != cat or t.is_construction != is_construction:
        t.category = cat
        t.is_construction = is_construction
        t.save(update_fields=["category", "is_construction"])
        updated += 1

print(f"✅ {updated} тендер шинэчлэгдлээ")
print("\nАнгиллаар:")
from django.db.models import Count
for row in Tender.objects.values("category").annotate(n=Count("id")).order_by("-n"):
    print(f"  {row['category']:15} : {row['n']}")