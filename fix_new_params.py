content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = "        windows = request.POST.get(\"windows\", \"\")\n        doors = request.POST.get(\"doors\", \"\")"

new = """        windows = request.POST.get("windows", "")
        doors = request.POST.get("doors", "")
        units_per_floor = request.POST.get("units_per_floor", "4")
        ground_floor_units = request.POST.get("ground_floor_units", "Дээрх давхартай адил")

        # Нийт айлын тоо тооцоолох
        try:
            fl = int(floors) if floors else 1
            upf = int(units_per_floor.replace("+","")) if units_per_floor else 4
            if ground_floor_units == "Дээрх давхартай адил":
                total_units = upf * fl
            elif "Хагас" in ground_floor_units:
                total_units = (upf // 2) + upf * (fl - 1)
            elif "Бүгд нийтийн" in ground_floor_units or "Гараж" in ground_floor_units:
                total_units = upf * (fl - 1)
            else:
                total_units = upf * fl
            total_units_text = f"{total_units} айл ({upf} айл × {fl} давхар)"
        except:
            total_units = 0
            total_units_text = "тодорхойгүй" """

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK — параметрүүд нэмэгдлээ")
else:
    print("NOT FOUND")