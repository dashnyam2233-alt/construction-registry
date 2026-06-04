content = open("apps/public/admin.py", "r", encoding="utf-8").read()

old = '''from .models import MaterialPrice

@admin.register(MaterialPrice)
class MaterialPriceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "unit", "price_min", "price_max", "updated_at", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name",)
    list_editable = ("price_min", "price_max", "is_active")
    ordering = ("category", "name")'''

new = '''from .models import MaterialPrice

@admin.register(MaterialPrice)
class MaterialPriceAdmin(admin.ModelAdmin):
    list_display = ("name", "get_main_category", "unit", "price_min", "price_max", "note", "updated_at", "is_active")
    list_filter = ("is_active", "category")
    search_fields = ("name", "note")
    list_editable = ("price_min", "price_max", "is_active")
    ordering = ("category", "name")

    def get_main_category(self, obj):
        cat = obj.category
        if cat.startswith("mat_"): return "🧱 Материал"
        if cat.startswith("labor_"): return "👷 Цалин"
        if cat.startswith("transport_"): return "🚛 Тээвэр"
        if cat.startswith("machine_"): return "🔩 Машин механизм"
        return "📦 Бусад"
    get_main_category.short_description = "Үндсэн ангилал"

    fieldsets = (
        ("Үндсэн мэдээлэл", {
            "fields": ("category", "name", "unit", "note", "is_active")
        }),
        ("Үнийн мэдээлэл (₮)", {
            "fields": ("price_min", "price_max"),
            "description": "Монгол төгрөгөөр оруулна уу. НӨАТ ороогүй үнэ."
        }),
    )'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/public/admin.py", "w", encoding="utf-8").write(content)
    print("OK — Admin шинэчлэгдлээ")
else:
    print("NOT FOUND")

# Одоогийн үнэнүүдийн ангиллыг шинэ системд шилжүүлэх
import django
import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
django.setup()

from apps.public.models import MaterialPrice

mapping = {
    "cement": "mat_cement",
    "sand_gravel": "mat_sand",
    "brick_block": "mat_brick",
    "rebar_metal": "mat_rebar",
    "wood": "mat_wood",
    "roof": "mat_roof",
    "insulation": "mat_insulation",
    "window_door": "mat_window",
    "interior": "mat_interior",
    "plumbing": "mat_plumbing",
    "electrical": "mat_electrical",
    "labor": "labor_general",
    "transport": "transport_material",
    "other": "other_misc",
}

updated = 0
for old_cat, new_cat in mapping.items():
    n = MaterialPrice.objects.filter(category=old_cat).update(category=new_cat)
    if n:
        print(f"  {old_cat} → {new_cat}: {n} үнэ")
        updated += n

print(f"Нийт {updated} үнэ шилжлээ")

# Машин механизм үнэ нэмэх
machines = [
    ("machine_crane", "Кран (50 тонн)", "цаг", 200000, 350000, ""),
    ("machine_crane", "Кран (25 тонн)", "цаг", 150000, 250000, ""),
    ("machine_excavator", "Экскаватор", "цаг", 120000, 200000, ""),
    ("machine_excavator", "Бульдозер", "цаг", 100000, 180000, ""),
    ("machine_concrete", "Бетон зуурагч (500л)", "цаг", 50000, 80000, ""),
    ("machine_concrete", "Бетон насос", "цаг", 150000, 250000, ""),
    ("machine_other", "Компрессор", "цаг", 40000, 70000, ""),
    ("machine_other", "Скафольд (түрээс)", "м²/сар", 3000, 5000, ""),
    ("machine_other", "Хэв хашмал (түрээс)", "м²", 8000, 15000, ""),
]

other_prices = [
    ("other_design", "Архитектурын зураг төсөл", "м²", 15000, 35000, ""),
    ("other_design", "Инженерийн зураг", "м²", 8000, 20000, ""),
    ("other_design", "Зураг төсвийн тооцоо", "м²", 5000, 12000, ""),
    ("other_permit", "Барилгын зөвшөөрөл", "удаа", 500000, 2000000, "талбайгаас хамаарна"),
    ("other_permit", "Газрын зөвшөөрөл", "удаа", 300000, 1000000, ""),
    ("other_insurance", "Барилгын даатгал", "жил", 500000, 2000000, ""),
    ("other_misc", "Туршилт, шинжилгээ", "удаа", 200000, 500000, ""),
]

added = 0
for items in [machines, other_prices]:
    for cat, name, unit, pmin, pmax, note in items:
        obj, created = MaterialPrice.objects.get_or_create(
            name=name,
            defaults={
                "category": cat,
                "unit": unit,
                "price_min": pmin,
                "price_max": pmax,
                "note": note,
            }
        )
        if created:
            added += 1

print(f"✅ {added} шинэ үнэ нэмэгдлээ")
print(f"📊 Нийт: {MaterialPrice.objects.count()}")