import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()

# Model нэмэх
content = open("apps/public/models.py", "r", encoding="utf-8").read()

addon = '''

class MaterialPrice(models.Model):
    CATEGORIES = [
        ("cement", "Цемент, шохой"),
        ("sand_gravel", "Элс, хайрга, дайрга"),
        ("brick_block", "Тоосго, блок"),
        ("rebar_metal", "Арматур, төмөр"),
        ("wood", "Модон материал"),
        ("roof", "Дээврийн материал"),
        ("insulation", "Дулаалга"),
        ("window_door", "Цонх, хаалга"),
        ("interior", "Дотор засал"),
        ("plumbing", "Сантехник"),
        ("electrical", "Цахилгаан"),
        ("labor", "Ажилчдын хөлс"),
        ("transport", "Тээвэр"),
        ("other", "Бусад"),
    ]

    category = models.CharField("Ангилал", max_length=30, choices=CATEGORIES)
    name = models.CharField("Материалын нэр", max_length=200)
    unit = models.CharField("Нэгж", max_length=30)
    price_min = models.DecimalField("Доод үнэ", max_digits=12, decimal_places=0)
    price_max = models.DecimalField("Дээд үнэ", max_digits=12, decimal_places=0)
    note = models.CharField("Тайлбар", max_length=300, blank=True, default="")
    updated_at = models.DateTimeField("Шинэчилсэн", auto_now=True)
    is_active = models.BooleanField("Идэвхтэй", default=True)

    class Meta:
        verbose_name = "Материалын үнэ"
        verbose_name_plural = "Материалын үнэнүүд"
        ordering = ("category", "name")

    def __str__(self):
        return f"{self.name} — {self.price_min:,}₮/{self.unit}"
    
    @property
    def price_avg(self):
        return (self.price_min + self.price_max) / 2
'''

if "class MaterialPrice" not in content:
    with open("apps/public/models.py", "a", encoding="utf-8") as f:
        f.write(addon)
    print("OK — MaterialPrice model нэмэгдлээ")
else:
    print("Аль хэдийн байна")

# Admin-д нэмэх
admin_content = open("apps/public/admin.py", "r", encoding="utf-8").read()
admin_addon = '''
from .models import MaterialPrice

@admin.register(MaterialPrice)
class MaterialPriceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "unit", "price_min", "price_max", "updated_at", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name",)
    list_editable = ("price_min", "price_max", "is_active")
    ordering = ("category", "name")
'''

if "MaterialPrice" not in admin_content:
    with open("apps/public/admin.py", "a", encoding="utf-8") as f:
        f.write(admin_addon)
    print("OK — Admin нэмэгдлээ")

print("Дууслаа")