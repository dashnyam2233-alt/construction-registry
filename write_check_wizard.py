path = r"apps\registry\templates\registry\budget_calculator.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
print(f"Нийт урт: {len(content)}")
# Барилгын төрлийн option-уудыг харах
idx = content.find('building_type')
print(content[idx:idx+500])