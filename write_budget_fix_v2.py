import os

path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Хугацааны томьёо засах
old1 = "    duration = max(6, round(total_area / 60))"
new1 = """    # Хугацаа — барилгын төрөл, талбайгаар
    if total_area <= 150:
        duration = 6
    elif total_area <= 300:
        duration = 9
    elif total_area <= 600:
        duration = 12
    elif total_area <= 1500:
        duration = 18
    elif total_area <= 3000:
        duration = 24
    elif total_area <= 6000:
        duration = 30
    else:
        duration = 36"""

# 2. Зураг төсөл — тогтмол үнэ (м²-аар биш)
old2 = """        {'name': 'Архитектур, инженерийн зураг төсөл', 'unit': 'м²', 'qty': round(total_area), 'unit_price': dsp, 'total': round(total_area*dsp)},"""
new2 = """        {'name': 'Архитектур, инженерийн зураг төсөл', 'unit': 'багц', 'qty': 1, 'unit_price': round(total_area * min(dsp, 15000)), 'total': round(total_area * min(dsp, 15000))},"""

# 3. Инженер хяналт — сарын үнэ барилгын хэмжээгээр
old3 = """        {'name': 'Инженер хяналт', 'unit': 'сар', 'qty': duration, 'unit_price': 1750000, 'total': duration*1750000},"""
new3 = """        {'name': 'Инженер хяналт', 'unit': 'сар', 'qty': duration, 'unit_price': min(1750000, max(500000, round(total_area * 300))), 'total': duration * min(1750000, max(500000, round(total_area * 300)))},"""

# 4. Ажилчдын тоо засах — том барилгад хэт их болохоос хамгаалах
old4 = """    general_worker_days = round(total_area * 2.5)"""
new4 = """    # Ажилчид — том барилгад хэт их болохоос хамгаалах
    # 1 барилгачин 1 өдөрт 1.5м² — гэхдээ олон ажилчин зэрэг ажилладаг
    # Тиймээс нийт хүн-өдрийг 1.5-2.0-оор тооцно
    general_worker_days = round(total_area * 1.5)"""

old5 = """    helper_days = round(total_area * 1.0)"""
new5 = """    helper_days = round(total_area * 0.6)"""

old6 = """    carpenter_days = round(total_area * 0.5)"""
new6 = """    carpenter_days = round(total_area * 0.3)"""

# 5. НӨАТ — зөвхөн материал+ажлаас авах (бусдаас авахгүй)
old7 = """    sub_total = sub_mat + sub_lab + sub_tra + sub_oth
    vat_amount = round(sub_total * vat_rate)"""
new7 = """    sub_total = sub_mat + sub_lab  # НӨАТ зөвхөн материал+ажлаас
    vat_amount = round(sub_total * vat_rate)"""

fixes = [
    (old1, new1, "Хугацаа"),
    (old2, new2, "Зураг төсөл"),
    (old3, new3, "Инженер хяналт"),
    (old4, new4, "Барилгачид"),
    (old5, new5, "Туслах"),
    (old6, new6, "Мужаан"),
    (old7, new7, "НӨАТ"),
]

for old, new, name in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        print(f"OK - {name}")
    else:
        print(f"NOT FOUND - {name}")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("\nDONE")