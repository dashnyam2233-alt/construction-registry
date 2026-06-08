path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\templates\registry\budget_calculator.html"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1805-р мөрийг харах (index 1804)
start = max(0, 1800)
end = min(len(lines), 1812)
for i in range(start, end):
    print(f"{i+1}: {lines[i]}", end='')