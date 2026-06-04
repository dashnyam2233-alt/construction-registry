path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Яг байгаа текстийг олох
idx = content.find("elif 'мак блок'")
if idx >= 0:
    print(repr(content[idx:idx+60]))
else:
    print("мак блок олдсонгүй")
    # wall_mat хайх
    idx2 = content.find("wall_mat.lower()")
    print(f"wall_mat.lower() байрлал: {idx2}")
    if idx2 >= 0:
        print(repr(content[idx2-20:idx2+80]))