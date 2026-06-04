import os

views_path = r"apps\registry\views.py"

with open(views_path, "r", encoding="utf-8") as f:
    content = f.read()

# budget_calculator функцийн POST хэсгийг бүрэн орлуулах
old = '''    if request.method == "POST":
        building_type = request.POST.get("building_type", "")
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
        units_per_floor = request.POST.get("units_per_floor", "4")
        ground_floor_units = request.POST.get("ground_floor_units", "Дээрх давхартай адил")'''

new = '''    if request.method == "POST":
        building_type = request.POST.get("building_type", "")
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
        units_per_floor = request.POST.get("units_per_floor", "4")
        ground_floor_units = request.POST.get("ground_floor_units", "Дээрх давхартай адил")
        # ШИНЭ: Python норм тооцоо — AI ашиглахгүй
        if length and width:
            try:
                norm_data = {
                    "building_type": building_type,
                    "floors": floors,
                    "length": length,
                    "width": width,
                    "ceiling_height": ceiling_height,
                    "wall_material": request.POST.get("wall_material", "Мак блок"),
                    "insulation": request.POST.get("insulation", ""),
                    "foundation_type": request.POST.get("foundation_type", "Шугаман суурь"),
                    "foundation_depth": request.POST.get("foundation_depth", "2.5"),
                    "roof_type": request.POST.get("roof_type", ""),
                    "floor_material": request.POST.get("floor_material", "Ламинат"),
                    "facade": request.POST.get("facade", "Шавар штукатур"),
                    "wall_finish": request.POST.get("wall_finish", "Хосолсон"),
                    "electrical": request.POST.get("electrical", "Стандарт 220В"),
                    "heating": request.POST.get("heating", ""),
                    "windows": windows,
                    "doors": doors,
                    "units_per_floor": units_per_floor,
                    "quality": quality,
                    "location": location,
                }
                result = calculate_budget_norm(norm_data)
            except Exception as e:
                error = f"Тооцооны алдаа: {str(e)}"'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK1 - POST хэсэг шинэчлэгдлээ")
else:
    print("NOT FOUND - текст таарахгүй байна")
    # Хэдэн тэмдэгт таарахгүй байгааг шалгах
    check = '        building_type = request.POST.get("building_type", "")'
    if check in content:
        print("building_type мөр байна")
    exit()

# Хуучин AI тооцооны том блокийг хасах
# est_grand_total-с эхлэн result_json хүртэлх хэсэг
idx_start = content.find("        # Талбай тооцоолох — нийт давхрын талбай")
idx_end = content.find("    import json as _json\n    result_json")

if idx_start >= 0 and idx_end >= 0:
    old_block = content[idx_start:idx_end]
    content = content.replace(old_block, "")
    print("OK2 - хуучин AI блок хасагдлаа")
else:
    print(f"SKIP2 - idx_start={idx_start}, idx_end={idx_end}")

with open(views_path, "w", encoding="utf-8") as f:
    f.write(content)
print("DONE")