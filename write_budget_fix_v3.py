import os

path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

fixes = [
    # 1. Скафольд — зөвхөн гадна ханын талбай, 1 удаа (сараар биш)
    (
        "        {'name': 'Скафольд түрээс', 'unit': 'м²/сар', 'qty': round(scaffold_area * duration_prelim), 'unit_price': scaffold_price, 'total': round(scaffold_area * duration_prelim * scaffold_price)},",
        "        {'name': 'Скафольд түрээс', 'unit': 'м²/сар', 'qty': round(scaffold_area), 'unit_price': scaffold_price * 3, 'total': round(scaffold_area * scaffold_price * 3)},",
        "Скафольд"
    ),
    # 2. Кран — том барилгад цаг хязгаарлах
    (
        "    crane_hours = round(total_area / 5)",
        "    crane_hours = min(200, round(total_area / 20))",
        "Кран"
    ),
    # 3. Экскаватор — хязгаарлах
    (
        "    excavator_hours = round(fv * 0.5)",
        "    excavator_hours = min(100, round(fv * 0.3))",
        "Экскаватор"
    ),
    # 4. Бетон насос — хязгаарлах
    (
        "    concrete_pump_hours = round((fv + sv) / 10)",
        "    concrete_pump_hours = min(80, round((fv + sv) / 15))",
        "Бетон насос"
    ),
    # 5. Санамсаргүй зардал — хувиар тооцох (тогтмол хэмжээтэй)
    (
        "        {'name': 'Санамсаргүй зардал (3%)', 'unit': 'хувь', 'qty': 1, 'unit_price': round(total_area*45000), 'total': round(total_area*45000)},",
        "        {'name': 'Санамсаргүй зардал (3%)', 'unit': 'хувь', 'qty': 1, 'unit_price': round((sub_mat+sub_lab)*0.03), 'total': round((sub_mat+sub_lab)*0.03)},",
        "Санамсаргүй зардал"
    ),
    # 6. Инженер хяналт — хязгаарлах
    (
        "        {'name': 'Инженер хяналт', 'unit': 'сар', 'qty': duration, 'unit_price': min(1750000, max(500000, round(total_area * 300))), 'total': duration * min(1750000, max(500000, round(total_area * 300)))},",
        "        {'name': 'Инженер хяналт', 'unit': 'сар', 'qty': duration, 'unit_price': 1750000, 'total': duration * 1750000},",
        "Инженер хяналт"
    ),
    # 7. Зураг төсөл — хязгаарлах
    (
        "        {'name': 'Архитектур, инженерийн зураг төсөл', 'unit': 'багц', 'qty': 1, 'unit_price': round(total_area * min(dsp, 15000)), 'total': round(total_area * min(dsp, 15000))},",
        "        {'name': 'Архитектур, инженерийн зураг төсөл', 'unit': 'багц', 'qty': 1, 'unit_price': min(50000000, round(total_area * 10000)), 'total': min(50000000, round(total_area * 10000))},",
        "Зураг төсөл"
    ),
]

for old, new, name in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        print(f"OK - {name}")
    else:
        print(f"NOT FOUND - {name}")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("\nDONE")