path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\templates\registry\budget_calculator.html"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# return гэсэн бүх мөрийг хай
for i, line in enumerate(lines):
    if 'return' in line.lower() and i > 1700:
        print(f"{i+1}: {line}", end='')