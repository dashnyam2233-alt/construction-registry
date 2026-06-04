path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = """        labor.append({'name': 'Гадна хана угсралт', 'unit': 'м²',
                      'qty': net_wall_area, 'unit_price': wall_work_price,
                      'total': round(net_wall_area * wall_work_price)})
        bq = round(net_wall_area * 16)
        bp = get_price('mat_brick', 'Мак блок (25') or 8500
        gp = get_price('mat_interior', 'Блокны цавуу') or 15000
        wp = get_price('labor_general', 'Блокон хана өрөх /25') or 25000
        materials += [
            {'name': 'Мак блок (25см) — гадна хана', 'unit': 'ш', 'qty': bq, 'unit_price': bp, 'total': bq*bp},
            {'name': 'Блокны цавуу', 'unit': 'кг', 'qty': round(net_wall_area*2), 'unit_price': gp, 'total': round(net_wall_area*2*gp)},
        ]
        labor.append({'name': 'Мак блок хана өрөх', 'unit': 'м²', 'qty': net_wall_area, 'unit_price': wp, 'total': round(net_wall_area*wp)})
    elif 'тоосго' in effective_wall_mat:"""

new = """        labor.append({'name': 'Гадна хана угсралт', 'unit': 'м²',
                      'qty': net_wall_area, 'unit_price': wall_work_price,
                      'total': round(net_wall_area * wall_work_price)})
    elif 'тоосго' in effective_wall_mat:"""

if old in content:
    content = content.replace(old, new, 1)
    print("OK - мак блок хэсэг бетон каркасаас хасагдлаа")
else:
    print("NOT FOUND")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("DONE")