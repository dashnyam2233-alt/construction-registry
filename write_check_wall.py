path = r"write_budget_norm.py"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines[80:130], start=81):
    print(f"{i}: {line}", end="")