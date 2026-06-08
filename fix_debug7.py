path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\views.py"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "eng_type == 'sewer'" in line:
        for j in range(i, min(i+50, len(lines))):
            print(f"{j+1}: {lines[j]}", end='')
        break