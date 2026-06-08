path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\views.py"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1270, 1305):
    print(f"{i+1}: {lines[i]}", end='')