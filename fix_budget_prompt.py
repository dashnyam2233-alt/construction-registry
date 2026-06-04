content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''  "other": [
    {{"name": "Тоног төхөөрөмж түрээс", "unit": "сар", "qty": 4, "unit_price": 500000, "total": 2000000}},
    {{"name": "Зураг төсөл", "unit": "удаа", "qty": 1, "unit_price": 1500000, "total": 1500000}}
  ],
  "summary": {{
    "materials_total": 15000000,
    "labor_total": 10000000,
    "other_total": 3500000,
    "grand_total": 28500000,
    "price_per_'''

new = '''  "other": [
    {{"name": "Тоног төхөөрөмж түрээс", "unit": "сар", "qty": 4, "unit_price": 500000, "total": 2000000}},
    {{"name": "Зураг төсөл", "unit": "удаа", "qty": 1, "unit_price": 1500000, "total": 1500000}}
  ],
  "transport": [
    {{"name": "Материал тээвэр", "unit": "удаа", "qty": 10, "unit_price": 150000, "total": 1500000}},
    {{"name": "Хог зайлуулах", "unit": "удаа", "qty": 5, "unit_price": 80000, "total": 400000}}
  ],
  "summary": {{
    "materials_total": 15000000,
    "labor_total": 10000000,
    "transport_total": 1900000,
    "other_total": 3500000,
    "grand_total": 30400000,
    "price_per_'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK — transport нэмэгдлээ")
else:
    print("NOT FOUND")
    # Яг байгаа текстийг харах
    idx = content.find('"other_total"')
    print(repr(content[idx-200:idx+200]))