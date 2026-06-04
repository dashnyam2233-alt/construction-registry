import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()

# Шинэ ангиллын бүтэц JSON-д хадгалах
import json

CATEGORIES = {
    "material": {
        "label": "🧱 Материал", "icon": "🧱",
        "subs": {
            "foundation": ("🏗 Барилгын үндсэн хийц", {
                "rebar": "Арматур төмөр",
                "metal_structure": "Металь хийц",
                "concrete": "Бетон зуурмаг",
                "insulation": "Дулаан дуу тусгаарлах",
                "roof_material": "Дээврийн материал",
                "formwork": "Хэв хашмал",
                "brick_block": "Тоосго блок",
                "wood": "Модон материал",
                "door_window": "Цонх хаалга",
                "glass": "Шилэн хийц",
                "cement_lime": "Цемент шохой",
                "sand_gravel": "Элс хайрга дайрга",
                "facade": "Гадна фасад",
            }),
            "interior": ("🎨 Засал чимэглэл", {
                "paint": "Будаг эмульс",
                "dry_mix": "Хуурай хольц",
                "wallpaper": "Обой хуулга",
                "parquet": "Паркет ламинат",
                "floor_accessories": "Шал дагалдах",
                "tile_stone": "Плита чулуу",
                "decoration": "Гоёл чимэглэл",
                "curtain": "Хөшиг тюль",
            }),
            "outdoor": ("🌿 Гадна тохижилт", {
                "paving": "Замын хавтан болон бродюр",
                "fence_gate": "Хашаа гадна хаалга",
                "playground": "Хүүхдийн тоглоом талбай",
                "landscaping": "Мод зүлэгжүүлэлт",
                "cleaning": "Цэвэрлэгээ тоног төхөөрөмж",
            }),
            "plumbing": ("🚿 Сан, халаалт, агааржуулалт", {
                "pipe_fitting": "Шугам хоолой холбох хэрэгсэл",
                "heating": "Халаах хэрэгсэл",
                "sanitary": "Угаалтуур суултуур ванн",
                "ventilation": "Агааржуулалт хөргөлт",
            }),
            "electrical": ("⚡ Цахилгаан, холбоо, дохиолол", {
                "wire_cable": "Цахилгааны утас кабель",
                "electrical_fitting": "Цахилгаан холбох хэрэгсэл",
                "lighting": "Гэрэл гэрэлтүүлэг",
                "generator_meter": "Цахилгааны үүсгүүр тоолуур",
                "switch_socket": "Унтраалга залгуур",
                "signal": "Холбоо дохиолол",
                "fire_alarm": "Галын дохиолол",
                "domophone": "Домофон ухаалаг цоож",
                "internet_tv": "Интернэт ТВ",
            }),
            "furniture": ("🪑 Тавилга", {
                "office": "Албан тасалгаа",
                "household": "Гэр ахуй",
            }),
            "software": ("💻 Программ хангамж ном", {
                "software_item": "Программ хангамж",
                "book": "Ном сэтгүүл",
                "manual": "Гарын авлага",
            }),
            "safety": ("🦺 ХАБЭА", {
                "safety_equipment": "ХАБЭА хэрэгсэл",
            }),
        }
    },
    "equipment": {
        "label": "🔩 Тоног төхөөрөмж", "icon": "🔩",
        "subs": {
            "excavator": ("Экскаватор", {}),
            "crane": ("Кран", {}),
            "bucket": ("Ковш", {}),
            "iron": ("Индүү", {}),
            "concrete_mixer": ("Бетон зуурагч", {}),
            "generator": ("Генератор", {}),
            "compressor": ("Компрессор", {}),
            "welding": ("Гагнуурын төхөөрөмж", {}),
            "lifting": ("Өргөх төхөөрөмж", {}),
            "tools": ("Барилгын багаж", {}),
            "measuring": ("Хэмжилтийн багаж", {}),
            "warehouse_eq": ("Агуулахын төхөөрөмж", {}),
            "other_eq": ("Бусад төхөөрөмж", {}),
        }
    },
    "rental": {
        "label": "🔑 Түрээс", "icon": "🔑",
        "subs": {
            "tech_rent": ("Техник түрээс", {}),
            "tool_rent": ("Багаж түрээс", {}),
            "scaffold_rent": ("Скафольд түрээс", {}),
            "formwork_rent": ("Хэв хашмал түрээс", {}),
            "crane_rent": ("Кран түрээс", {}),
            "container_rent": ("Контейнер түрээс", {}),
            "office_rent": ("Оффис түрээс", {}),
            "warehouse_rent": ("Агуулах түрээс", {}),
            "machine_rent": ("Машин механизм түрээс", {}),
            "other_rent": ("Бусад түрээс", {}),
        }
    },
    "realestate": {
        "label": "🏠 Үл хөдлөх хөрөнгө", "icon": "🏠",
        "subs": {
            "apartment": ("Орон сууц", {}),
            "house": ("Амины орон сууц", {}),
            "office_re": ("Оффис", {}),
            "commercial": ("Үйлчилгээний талбай", {}),
            "warehouse_re": ("Агуулах үйлдвэр", {}),
            "land": ("Газар", {}),
            "under_construction": ("Баригдаж буй объект", {}),
            "re_rent": ("Түрээс", {}),
            "re_sale": ("Худалдах", {}),
        }
    },
    "service": {
        "label": "🏗 Барилгын үйлчилгээ", "icon": "🏗",
        "subs": {
            "construction_co": ("Барилгын компани", {}),
            "interior_svc": ("Интерьер", {}),
            "exterior_svc": ("Экстерьер", {}),
            "carpenter": ("Мужаан", {}),
            "tiler": ("Плитачин", {}),
            "electrician": ("Цахилгаанчин", {}),
            "plumber": ("Сантехник", {}),
            "welder": ("Гагнуур", {}),
            "roofing": ("Дээвэр", {}),
            "facade_svc": ("Фасад", {}),
            "road_svc": ("Зам талбай", {}),
            "cleaning_svc": ("Цэвэрлэгээ", {}),
            "demolition": ("Нураалт", {}),
            "crane_svc": ("Өргөлт кран үйлчилгээ", {}),
            "engineering_svc": ("Инженеринг", {}),
            "consulting": ("Хяналт зөвлөх", {}),
            "other_svc": ("Бусад үйлчилгээ", {}),
        }
    },
    "design": {
        "label": "📐 Зураг төсөв, дизайн", "icon": "📐",
        "subs": {
            "architecture": ("Архитектур", {}),
            "interior_design": ("Интерьер дизайн", {}),
            "structure": ("Конструкц", {}),
            "engineering_design": ("Инженерийн зураг", {}),
            "visualization": ("3D визуал", {}),
            "landscape": ("Ландшафт дизайн", {}),
            "budget": ("Төсөв", {}),
            "render": ("Render", {}),
            "other_design": ("Бусад дизайн", {}),
        }
    },
    "worker": {
        "label": "👷 Ажилтан, ажлын зар", "icon": "👷",
        "subs": {
            "jobseeker_engineer": ("Ажил хайгч: Инженер", {}),
            "jobseeker_architect": ("Ажил хайгч: Архитектор", {}),
            "jobseeker_operator": ("Ажил хайгч: Оператор", {}),
            "jobseeker_welder": ("Ажил хайгч: Гагнуурчин", {}),
            "jobseeker_carpenter": ("Ажил хайгч: Мужаан", {}),
            "jobseeker_electrician": ("Ажил хайгч: Цахилгаанчин", {}),
            "jobseeker_plumber": ("Ажил хайгч: Сантехникч", {}),
            "jobseeker_helper": ("Ажил хайгч: Туслах ажилтан", {}),
            "jobseeker_brigade": ("Ажил хайгч: Бригад", {}),
            "jobseeker_other": ("Ажил хайгч: Бусад", {}),
            "job_engineer": ("Ажлын байр: Инженер", {}),
            "job_field": ("Ажлын байр: Талбайн ажилтан", {}),
            "job_operator": ("Ажлын байр: Оператор", {}),
            "job_estimator": ("Ажлын байр: Төсөвчин", {}),
            "job_pm": ("Ажлын байр: Project manager", {}),
            "job_safety": ("Ажлын байр: Safety officer", {}),
            "job_other": ("Ажлын байр: Бусад", {}),
        }
    },
    "tender": {
        "label": "📋 Тендер, төсөл", "icon": "📋",
        "subs": {
            "tender_item": ("Тендер", {}),
            "contractor": ("Гүйцэтгэгч хайх", {}),
            "subcontractor": ("Туслан гүйцэтгэгч", {}),
            "investment": ("Хөрөнгө оруулалт", {}),
            "partnership": ("Хамтран ажиллах", {}),
            "new_project": ("Шинэ төсөл", {}),
            "tender_other": ("Бусад", {}),
        }
    },
    "company": {
        "label": "🏢 Компаниуд", "icon": "🏢",
        "subs": {
            "construction_company": ("Барилгын компани", {}),
            "material_supplier": ("Материал нийлүүлэгч", {}),
            "equipment_supplier": ("Тоног нийлүүлэгч", {}),
            "engineering_co": ("Инженеринг", {}),
            "interior_co": ("Интерьер", {}),
            "architecture_co": ("Архитектур", {}),
            "factory": ("Үйлдвэр", {}),
            "rental_co": ("Түрээс үйлчилгээ", {}),
            "other_company": ("Бусад компани", {}),
        }
    },
    "other": {
        "label": "📦 Бусад", "icon": "📦",
        "subs": {
            "leftover": ("Үлдэгдэл материал", {}),
            "warehouse_trade": ("Агуулахын худалдаа", {}),
            "used_goods": ("Хэрэглэсэн бараа", {}),
            "news": ("Барилгын мэдээ", {}),
            "training": ("Сургалт", {}),
            "other_misc": ("Бусад", {}),
        }
    },
}

with open("all_categories.json", "w", encoding="utf-8") as f:
    json.dump(CATEGORIES, f, ensure_ascii=False, indent=2)
print(f"OK — all_categories.json үүслээ ({len(CATEGORIES)} ангилал)")

# Ad model-д category choices шинэчлэх
content = open("apps/public/models.py", "r", encoding="utf-8").read()

old_choices = """    class Category(models.TextChoices):
        HOUSE = "house", "Орон сууц & Барилга"
        MATERIAL = "material", "Материал & Тоног"
        WORKER = "worker", "Ажилтан & Бригад"
        REPAIR = "repair", "Засвар & Үйлчилгээ"
        DESIGN = "design", "Зураг төсөл"
        OTHER = "other", "Бусад" """

new_choices = """    class Category(models.TextChoices):
        MATERIAL = "material", "Материал"
        EQUIPMENT = "equipment", "Тоног төхөөрөмж"
        RENTAL = "rental", "Түрээс"
        REALESTATE = "realestate", "Үл хөдлөх хөрөнгө"
        SERVICE = "service", "Барилгын үйлчилгээ"
        DESIGN = "design", "Зураг төсөв, дизайн"
        WORKER = "worker", "Ажилтан, ажлын зар"
        TENDER = "tender", "Тендер, төсөл"
        COMPANY = "company", "Компаниуд"
        OTHER = "other", "Бусад" """

if old_choices in content:
    content = content.replace(old_choices, new_choices, 1)
    open("apps/public/models.py", "w", encoding="utf-8").write(content)
    print("OK — Category choices шинэчлэгдлээ")
else:
    print("NOT FOUND — гараар засна")
    idx = content.find("class Category(")
    if idx >= 0:
        print(repr(content[idx:idx+300]))