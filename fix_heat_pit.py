path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\views.py"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old = """        concrete_price = {'B20': 260000, 'B25': 280000, 'B30': 320000}.get(concrete, 280000)
    elif eng_type == 'water_pit':"""

new = """        concrete_price = {'B20': 260000, 'B25': 280000, 'B30': 320000}.get(concrete, 280000)

        materials.append({'name': f'Бетон {concrete}', 'unit': 'м³', 'qty': total_vol,
                          'unit_price': int(concrete_price * quality_coef),
                          'total': int(total_vol * concrete_price * quality_coef)})
        materials.append({'name': 'Арматур φ12 A400', 'unit': 'кг', 'qty': rebar_kg,
                          'unit_price': int(3000 * quality_coef),
                          'total': int(rebar_kg * 3000 * quality_coef)})
        materials.append({'name': 'Хэвлэгч мод', 'unit': 'м³', 'qty': round(total_vol * 0.3, 2),
                          'unit_price': int(450000 * quality_coef),
                          'total': int(total_vol * 0.3 * 450000 * quality_coef)})
        if insulation != 'Байхгүй':
            ins_vol = round((outer_l * outer_w * 2 + 2 * (outer_l + outer_w) * depth) * 0.1 * count, 2)
            materials.append({'name': f'Дулаалга {insulation}', 'unit': 'м²', 'qty': ins_vol,
                              'unit_price': int(25000 * quality_coef),
                              'total': int(ins_vol * 25000 * quality_coef)})
        labor.append({'name': 'Малтлага', 'unit': 'м³', 'qty': exc_vol,
                      'unit_price': int(28000 * loc_coef), 'total': int(exc_vol * 28000 * loc_coef)})
        labor.append({'name': 'Бетон цутгах', 'unit': 'м³', 'qty': total_vol,
                      'unit_price': int(95000 * quality_coef),
                      'total': int(total_vol * 95000 * quality_coef)})
        labor.append({'name': 'Арматур боох', 'unit': 'кг', 'qty': rebar_kg,
                      'unit_price': int(800 * quality_coef),
                      'total': int(rebar_kg * 800 * quality_coef)})
        other.append({'name': 'Тээвэр, бусад', 'unit': 'дүн', 'qty': 1,
                      'unit_price': 350000, 'total': 350000})

    elif eng_type == 'water_pit':"""

content = content.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ heat_pit засагдлаа")