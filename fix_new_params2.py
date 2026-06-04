content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = "- Цонх: {windows}, Хаалга: {doors}"
new = """- Нэг давхарт айлын тоо: {units_per_floor}
- 1-р давхар: {ground_floor_units}
- НИЙТ АЙЛЫН ТОО: {total_units_text}
- Нэг айлд цонх: {windows}, хаалга: {doors}
- Нийт цонх (ойролцоо): {total_units} × цонхны тоо"""

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK — prompt шинэчлэгдлээ")
else:
    print("NOT FOUND")