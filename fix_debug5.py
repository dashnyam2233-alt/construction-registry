path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\views.py"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'get_material_price' in line or 'AdminDB' in line or 'MaterialPrice' in line:
        print(f"{i+1}: {line}", end='')