path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\templates\registry\budget_calculator.html"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1885, 1915):
    print(f"{i+1}: {lines[i]}", end='')