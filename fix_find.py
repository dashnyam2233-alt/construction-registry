path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\templates\registry\budget_calculator.html"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'water_pit' in line or 'eng-depth2' in line or 'eng-diameter' in line:
        print(f"{i+1}: {repr(line)}")