path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\views.py"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# calculate_engineering_budget функцийг хай
for i, line in enumerate(lines):
    if 'calculate_engineering_budget' in line or 'heat_pit' in line:
        print(f"{i+1}: {line}", end='')