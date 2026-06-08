path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\views.py"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# sewer блокийг хай
for i, line in enumerate(lines):
    if 'sewer' in line and ('append' in line or 'materials' in line or 'labor' in line):
        for j in range(i, min(i+3, len(lines))):
            print(f"{j+1}: {lines[j]}", end='')
        print()