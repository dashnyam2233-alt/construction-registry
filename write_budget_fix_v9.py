path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = "    wall_mat = data.get('wall_material', 'Мак блок')"
new = """    building_type = data.get('building_type', '')
    wall_mat = data.get('wall_material', 'Мак блок')"""

if old in content:
    content = content.replace(old, new, 1)
    print("OK")
else:
    print("NOT FOUND")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("DONE")