import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()

# Model-ын category choices шинэчлэх
content = open("apps/public/models.py", "r", encoding="utf-8").read()

old = '''    CATEGORIES = [
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
    ]'''

new = '''    CATEGORIES = [
        # 1. Материал
        ("mat_cement", "1. Материал — Цемент, шохой"),
        ("mat_sand", "1. Материал — Элс, хайрга, дайрга"),
        ("mat_brick", "1. Материал — Тоосго, блок"),
        ("mat_rebar", "1. Материал — Арматур, төмөр"),
        ("mat_wood", "1. Материал — Модон материал"),
        ("mat_roof", "1. Материал — Дээврийн материал"),
        ("mat_insulation", "1. Материал — Дулаалга"),
        ("mat_window", "1. Материал — Цонх, хаалга"),
        ("mat_interior", "1. Материал — Дотор засал"),
        ("mat_plumbing", "1. Материал — Сантехник"),
        ("mat_electrical", "1. Материал — Цахилгаан"),
        ("mat_other", "1. Материал — Бусад материал"),
        # 2. Цалин
        ("labor_general", "2. Цалин — Барилгачин"),
        ("labor_special", "2. Цалин — Мэргэжилтэн"),
        ("labor_engineer", "2. Цалин — Инженер, хяналт"),
        # 3. Тээвэр
        ("transport_material", "3. Тээвэр — Материал тээвэр"),
        ("transport_waste", "3. Тээвэр — Хог зайлуулах"),
        ("transport_other", "3. Тээвэр — Бусад тээвэр"),
        # 4. Машин механизм
        ("machine_crane", "4. Машин механизм — Кран"),
        ("machine_excavator", "4. Машин механизм — Экскаватор"),
        ("machine_concrete", "4. Машин механизм — Бетон зуурагч"),
        ("machine_other", "4. Машин механизм — Бусад машин"),
        # 5. Бусад
        ("other_design", "5. Бусад — Зураг төсөл"),
        ("other_vat", "5. Бусад — НӨАТ"),
        ("other_permit", "5. Бусад — Зөвшөөрөл, бүртгэл"),
        ("other_insurance", "5. Бусад — Даатгал"),
        ("other_misc", "5. Бусад — Бусад"),
    ]'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/public/models.py", "w", encoding="utf-8").write(content)
    print("OK — ангиллууд шинэчлэгдлээ")
else:
    print("NOT FOUND")