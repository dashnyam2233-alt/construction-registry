path = r"apps\registry\templates\registry\budget_calculator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split('\n')
for i, line in enumerate(lines):
    if 'intcomma' in line or 'floatformat' in line:
        print(f"Мөр {i+1}: {line.strip()}")