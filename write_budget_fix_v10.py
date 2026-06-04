path = r"write_budget_norm.py"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 126-140 мөрүүдийг харах
for i, line in enumerate(lines[124:145], start=125):
    print(f"{i}: {line}", end="")