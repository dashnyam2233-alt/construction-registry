content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''        building_type = request.POST.get("building_type", "")
        area = request.POST.get("area", "")
        floors = request.POST.get("floors", "1")
        location = request.POST.get("location", "Улаанбаатар")
        quality = request.POST.get("quality", "дунд")
        extra = request.POST.get("extra", "")'''

new = '''        building_type = request.POST.get("building_type", "")
        floors = request.POST.get("floors", "1")
        quality = request.POST.get("quality", "дунд")
        location = request.POST.get("location", "Улаанбаатар")
        build_year = request.POST.get("build_year", "2026")
        length = request.POST.get("length", "")
        width = request.POST.get("width", "")
        total_height = request.POST.get("total_height", "")
        ceiling_height = request.POST.get("ceiling_height", "2.7")
        inner_wall_length = request.POST.get("inner_wall_length", "")
        windows = request.POST.get("windows", "")
        doors = request.POST.get("doors", "")
        foundation_type = request.POST.get("foundation_type", "")
        foundation_depth = request.POST.get("foundation_depth", "")
        foundation_width = request.POST.get("foundation_width", "")
        concrete_grade = request.POST.get("concrete_grade", "М250")
        soil_type = request.POST.get("soil_type", "")
        water_table = request.POST.get("water_table", "")
        wall_material = request.POST.get("wall_material", "")
        wall_thickness = request.POST.get("wall_thickness", "")
        insulation = request.POST.get("insulation", "")
        inner_wall_material = request.POST.get("inner_wall_material", "")
        roof_type = request.POST.get("roof_type", "")
        facade = request.POST.get("facade", "")
        floor_material = request.POST.get("floor_material", "")
        wall_finish = request.POST.get("wall_finish", "")
        heating = request.POST.get("heating", "")
        water = request.POST.get("water", "")
        electrical = request.POST.get("electrical", "")
        extras = request.POST.get("extras", "")
        
        # Талбай тооцоолох
        try:
            area = str(float(length) * float(width)) if length and width else "мэдэгдэхгүй"
        except:
            area = "мэдэгдэхгүй"'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK — параметрүүд нэмэгдлээ")
else:
    print("NOT FOUND")

old2 = '''        prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн. Дараах барилгын төсвийг тооцоолж өгнө үү.

Барилгын мэдээлэл:
- Төрөл: {building_type}
- Талбай: {area} м²
- Давхар: {floors}
- Байршил: {location}
- Чанарын түвшин: {quality}
- Нэмэлт мэдээлэл: {extra}'''

new2 = '''        prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн. Дараах барилгын төсвийг тооцоолж өгнө үү.

Барилгын дэлгэрэнгүй мэдээлэл:
- Зориулалт: {building_type}
- Давхар: {floors}
- Байршил: {location}
- Чанар: {quality}
- Барилгын жил: {build_year}

Хэмжээс:
- Урт x Өргөн: {length}м x {width}м
- Нийт өндөр: {total_height}м
- Тааз өндөр: {ceiling_height}м
- Нийт талбай: {area} м²
- Дотор хуваалтын урт: {inner_wall_length}м
- Цонх: {windows}, Хаалга: {doors}

Суурь:
- Төрөл: {foundation_type}
- Гүн: {foundation_depth}м, Өргөн: {foundation_width}см
- Бетоны марк: {concrete_grade}
- Хөрс: {soil_type}, Газрын ус: {water_table}

Хана, дээвэр:
- Гадна хана: {wall_material}, {wall_thickness}
- Дулаалга: {insulation}
- Дотор хуваалт: {inner_wall_material}
- Дээвэр: {roof_type}
- Гадна засал: {facade}

Дотор засал:
- Шал: {floor_material}
- Ханын засал: {wall_finish}

Инженерийн систем:
- Халаалт: {heating}
- Ус: {water}
- Цахилгаан: {electrical}
- Нэмэлт: {extras}'''

if old2 in content:
    content = content.replace(old2, new2, 1)
    print("OK — prompt шинэчлэгдлээ")
else:
    print("NOT FOUND 2")

old3 = '''  "summary": {
    "materials_total": 15000000,
    "labor_total": 10000000,
    "other_total": 3500000,
    "grand_total": 28500000,
    "price_per_m2": 407142,
    "duration_months": 5
  },'''

new3 = '''  "transport": [
    {{"name": "Материал тээвэр", "unit": "удаа", "qty": 10, "unit_price": 150000, "total": 1500000}}
  ],
  "summary": {
    "materials_total": 15000000,
    "labor_total": 10000000,
    "transport_total": 1500000,
    "other_total": 3500000,
    "grand_total": 30000000,
    "price_per_m2": 375000,
    "duration_months": 5
  },'''

if old3 in content:
    content = content.replace(old3, new3, 1)
    print("OK — transport нэмэгдлээ")
else:
    print("NOT FOUND 3")

open("apps/registry/views.py", "w", encoding="utf-8").write(content)
print("Дууслаа")