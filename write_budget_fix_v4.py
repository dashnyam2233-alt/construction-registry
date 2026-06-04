import os

path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

fixes = [
    # 1. Нил/гадсан суурийн бетон, арматур засах
    (
        """    elif 'гадсан' in foundation_type.lower() or 'нил' in foundation_type.lower():
        fv = round(floor_area * 0.15, 1)
        rebar_kg = floor_area * 20
        cg = 'М300'""",
        """    elif 'гадсан' in foundation_type.lower() or 'нил' in foundation_type.lower():
        fv = round(floor_area * 0.4, 1)
        rebar_kg = floor_area * 35
        cg = 'М300'""",
        "Нил/гадсан суурь"
    ),
    # 2. Хучилтын арматур 12кг → 25кг/м²
    (
        "    srt = round(sa * 12 / 1000, 2)",
        "    srt = round(sa * 25 / 1000, 2)",
        "Хучилтын арматур"
    ),
    # 3. Колонн, дам нуруу — олон давхарт барилгад нэмэх
    (
        "    # 6. ШАТНЫ БҮТЭЦ",
        """    # 5б. КОЛОНН, ДАМ НУРУУ — олон давхарт барилгад
    if floors >= 3:
        # Колонн: нэг давхарт 1 колонн = 0.3x0.3x3м = 0.27м³, 80кг арматур
        # Нэг давхарт колонны тоо ойролцоо: floor_area / 25
        column_count = round(floor_area / 25)
        column_concrete = round(column_count * floors * 0.27, 1)
        column_rebar = round(column_count * floors * 0.08, 2)
        beam_concrete = round(floor_area * (floors-1) * 0.05, 1)
        beam_rebar = round(floor_area * (floors-1) * 15 / 1000, 2)
        col_cp = get_price('mat_cement', 'М300') or 285000
        materials += [
            {'name': 'Бетон зуурмаг М300 — колонн', 'unit': 'м³',
             'qty': column_concrete, 'unit_price': col_cp,
             'total': round(column_concrete * col_cp)},
            {'name': 'Арматур — колонн', 'unit': 'тонн',
             'qty': column_rebar, 'unit_price': rp,
             'total': round(column_rebar * rp)},
            {'name': 'Бетон зуурмаг М300 — дам нуруу', 'unit': 'м³',
             'qty': beam_concrete, 'unit_price': col_cp,
             'total': round(beam_concrete * col_cp)},
            {'name': 'Арматур — дам нуруу', 'unit': 'тонн',
             'qty': beam_rebar, 'unit_price': rp,
             'total': round(beam_rebar * rp)},
        ]
        labor += [
            {'name': 'Бетон цутгалт — колонн', 'unit': 'м³',
             'qty': column_concrete, 'unit_price': cwp,
             'total': round(column_concrete * cwp)},
            {'name': 'Арматур угсралт — колонн, дам нуруу', 'unit': 'тонн',
             'qty': column_rebar + beam_rebar, 'unit_price': rwp,
             'total': round((column_rebar + beam_rebar) * rwp)},
        ]

    # 6. ШАТНЫ БҮТЭЦ""",
        "Колонн, дам нуруу"
    ),
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