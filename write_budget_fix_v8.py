import os

path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Барилгын төрлөөр ялгах логик нэмэх — хана хэсгийн өмнө
old = """    # ============================================================
    # 2. ГАДНА ХАНА
    # ============================================================
    if 'мак блок' in wall_mat.lower():"""

new = """    # ============================================================
    # БАРИЛГЫН ТӨРЛИЙН ТОДОРХОЙЛОЛТ
    # ============================================================
    bt = building_type.lower()
    is_high_rise = floors >= 5 or 'өндөр давхар' in bt or 'олон айлын' in bt
    is_mid_rise = 3 <= floors <= 4
    is_low_rise = floors <= 2 or 'амины' in bt

    # Олон давхарт барилгад хана материалыг автоматаар солих
    if is_high_rise and 'металл' not in wall_mat.lower():
        # 5+ давхар бол бетон каркас систем
        effective_wall_mat = 'бетон каркас'
    elif is_mid_rise and 'мак блок' in wall_mat.lower():
        effective_wall_mat = 'мак блок'
    else:
        effective_wall_mat = wall_mat.lower()

    # ============================================================
    # 2. ГАДНА ХАНА
    # ============================================================
    if 'бетон каркас' in effective_wall_mat:"""

# Бетон каркас хананы тооцоо нэмэх
old2 = """    elif 'мак блок' in wall_mat.lower():
        bq = round(net_wall_area * 16)"""

new2 = """    elif 'мак блок' in effective_wall_mat:
        bq = round(net_wall_area * 16)"""

old3 = """    elif 'тоосго' in wall_mat.lower():
        bq = round(net_wall_area * 51)"""

new3 = """    elif 'тоосго' in effective_wall_mat:
        bq = round(net_wall_area * 51)"""

old4 = """    elif 'бетон' in wall_mat.lower():
        wv = round(net_wall_area * 0.2, 1)"""

new4 = """    elif 'бетон' in effective_wall_mat and 'каркас' not in effective_wall_mat:
        wv = round(net_wall_area * 0.2, 1)"""

# Бетон каркас хананы тооцоо
beton_karkас = """        # Бетон каркас + дотор блок хаалт
        # Гадна хана: бетон хавтан (prefab) эсвэл монолит
        wall_panel_price = get_price('mat_cement', 'М300') or 285000
        wall_panel_volume = round(net_wall_area * 0.18, 1)
        wall_panel_rebar = round(net_wall_area * 0.02, 2)
        # Гадна хананы дүүргэлт: мак блок (20см)
        infill_block_qty = round(net_wall_area * 12)
        infill_block_price = get_price('mat_brick', 'Мак блок (20') or 7000
        wall_work_price = get_price('labor_general', 'Гадна бетон хананы') or 130000
        materials += [
            {'name': 'Бетон хавтан М300 — гадна хана', 'unit': 'м³',
             'qty': wall_panel_volume, 'unit_price': wall_panel_price,
             'total': round(wall_panel_volume * wall_panel_price)},
            {'name': 'Арматур — гадна хана', 'unit': 'тонн',
             'qty': wall_panel_rebar, 'unit_price': rp,
             'total': round(wall_panel_rebar * rp)},
            {'name': 'Мак блок (20см) — ханын дүүргэлт', 'unit': 'ш',
             'qty': infill_block_qty, 'unit_price': infill_block_price,
             'total': infill_block_qty * infill_block_price},
        ]
        labor.append({'name': 'Гадна хана угсралт', 'unit': 'м²',
                      'qty': net_wall_area, 'unit_price': wall_work_price,
                      'total': round(net_wall_area * wall_work_price)})"""

new = new.replace(
    """    # ============================================================
    # 2. ГАДНА ХАНА
    # ============================================================
    if 'бетон каркас' in effective_wall_mat:""",
    f"""    # ============================================================
    # 2. ГАДНА ХАНА
    # ============================================================
    if 'бетон каркас' in effective_wall_mat:
{beton_karkас}"""
)

# Дотор хуваалт — олон давхарт барилгад бага
old5 = """    ibq = round(inner_wall_area * 16)"""
new5 = """    # Олон давхарт барилгад дотор хуваалт харьцангуй бага
    if is_high_rise:
        inner_wall_density = 10  # блок/м²
    else:
        inner_wall_density = 16
    ibq = round(inner_wall_area * inner_wall_density)"""

fixes = [
    (old, new, "Барилгын төрөл + гадна хана"),
    (old2, new2, "Мак блок нөхцөл"),
    (old3, new3, "Тоосго нөхцөл"),
    (old4, new4, "Бетон нөхцөл"),
    (old5, new5, "Дотор хуваалт"),
]

for o, n, name in fixes:
    if o in content:
        content = content.replace(o, n, 1)
        print(f"OK - {name}")
    else:
        print(f"NOT FOUND - {name}")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("\nDONE")