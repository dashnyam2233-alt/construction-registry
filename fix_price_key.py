path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\views.py"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# 'price': xxx → 'unit_price': xxx (total-г хөндөхгүй)
fixed = re.sub(r"'price':", "'unit_price':", content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(fixed)

print("✅ Засагдлаа")