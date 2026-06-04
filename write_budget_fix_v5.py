import os

path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = """    sub_mat = round(sum(i['total'] for i in materials) * quality_coef)
    sub_lab = round(sum(i['total'] for i in labor) * quality_coef)
    sub_tra = sum(i['total'] for i in transport)
    sub_oth = sum(i['total'] for i in other)
    sub_total = sub_mat + sub_lab  # НӨАТ зөвхөн материал+ажлаас
    vat_amount = round(sub_total * vat_rate)
    other.append({'name': 'НӨАТ (10%)', 'unit': 'хувь', 'qty': 1, 'unit_price': vat_amount, 'total': vat_amount})

    mt = sub_mat
    lt = sub_lab
    tt = sub_tra
    ot = sub_oth + vat_amount
    gt = mt + lt + tt + ot"""

new = """    sub_mat = round(sum(i['total'] for i in materials) * quality_coef)
    sub_lab = round(sum(i['total'] for i in labor) * quality_coef)
    sub_tra = sum(i['total'] for i in transport)
    sub_oth = sum(i['total'] for i in other)
    vat_amount = round((sub_mat + sub_lab) * 0.10)
    other.append({'name': 'НӨАТ (10%)', 'unit': 'хувь', 'qty': 1, 'unit_price': vat_amount, 'total': vat_amount})
    # Санамсаргүй зардал — материал+ажлын 3%
    misc_amount = round((sub_mat + sub_lab) * 0.03)
    # other дотор санамсаргүй зардлыг шинэчлэх
    for item in other:
        if 'Санамсаргүй' in item['name']:
            item['unit_price'] = misc_amount
            item['total'] = misc_amount
            break

    mt = sub_mat
    lt = sub_lab
    tt = sub_tra
    ot = sum(i['total'] for i in other)
    gt = mt + lt + tt + ot"""

if old in content:
    content = content.replace(old, new, 1)
    print("OK - НӨАТ засагдлаа")
else:
    print("NOT FOUND")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("DONE")