from django.contrib import admin

# Register your models here.
from .models import Ad, MaterialNorm

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price_type", "city", "status", "author", "created_at")
    list_filter = ("category", "status", "city")
    search_fields = ("title", "description", "contact_name", "contact_phone")
    ordering = ("-created_at",)
from .models import Tender

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "price", "deadline", "is_construction", "created_at")
    list_filter = ("is_construction",)
    search_fields = ("title", "organization", "tender_code")
    ordering = ("-created_at",)

from .models import MaterialPrice

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
    )

@admin.register(MaterialNorm)
class MaterialNormAdmin(admin.ModelAdmin):
    list_display = ['building_type', 'work_type', 'material_name', 'norm_per_m2', 'unit', 'db_category', 'is_active']
    list_filter = ['building_type', 'work_type', 'is_active']
    search_fields = ['material_name', 'db_category', 'db_name_contains']
    list_editable = ['norm_per_m2', 'is_active']
    ordering = ['building_type', 'work_type', 'material_name']
    list_per_page = 50
