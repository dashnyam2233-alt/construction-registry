path = r"write_budget_norm.py"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 460-470 мөрүүдийг харах
for i, line in enumerate(lines[455:475], start=456):
    print(f"{i}: {line}", end="")