path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\views.py"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1236, 1320):
    print(f"{i+1}: {lines[i]}", end='')