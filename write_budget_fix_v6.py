path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = """        {'name': 'Санамсаргүй зардал (3%)', 'unit': 'хувь', 'qty': 1, 'unit_price': round((sub_mat+sub_lab)*0.03), 'total': round((sub_mat+sub_lab)*0.03)},
    ]

    # НӨАТ тооцоо
    sub_mat = round(sum(i['total'] for i in materials) * quality_coef)
    sub_lab = round(sum(i['total'] for i in labor) * quality_coef)"""

new = """    ]

    # НИЙТ ТООЦОО — эхлээд sub_mat, sub_lab тодорхойлно
    sub_mat = round(sum(i['total'] for i in materials) * quality_coef)
    sub_lab = round(sum(i['total'] for i in labor) * quality_coef)

    # Санамсаргүй зардал — материал+ажлын 3%
    other.append({'name': 'Санамсаргүй зардал (3%)', 'unit': 'хувь', 'qty': 1, 'unit_price': round((sub_mat+sub_lab)*0.03), 'total': round((sub_mat+sub_lab)*0.03)})"""

if old in content:
    content = content.replace(old, new, 1)
    print("OK")
else:
    print("NOT FOUND")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("DONE")