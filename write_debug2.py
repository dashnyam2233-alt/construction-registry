import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

exec(open('write_budget_norm.py', encoding='utf-8').read().split('# Туршилт')[0])

test = {
    'building_type': 'Олон айлын орон сууц',
    'floors': '8', 'length': '40', 'width': '18',
    'ceiling_height': '2.7', 'wall_material': 'Мак блок',
    'insulation': 'Шилэн хөвөн 10см',
    'foundation_type': 'Нил суурь', 'foundation_depth': '3.0',
    'roof_type': 'Хавтгай дээвэр', 'floor_material': 'Ламинат',
    'facade': 'Шавар штукатур', 'wall_finish': 'Хосолсон',
    'electrical': 'Гурван фаз 380В',
    'heating': 'Төвийн халаалт', 'windows': '5-6', 'doors': '4-5',
    'quality': 'дунд', 'units_per_floor': '4', 'location': 'Улаанбаатар',
}

r = calculate_budget(test)
s = r['summary']
print(f"Талбай: {r['building_info']['area']}, Хугацаа: {s['duration_months']} сар")
print(f"НИЙТ: {s['grand_total']:,}  |  1м²: {s['price_per_m2']:,}")
print(f"\n--- Бүлэг ---")
print(f"Материал: {s['materials_total']:,}  ({s['materials_total']*100//s['grand_total']}%)")
print(f"Ажил:     {s['labor_total']:,}  ({s['labor_total']*100//s['grand_total']}%)")
print(f"Тээвэр:   {s['transport_total']:,}  ({s['transport_total']*100//s['grand_total']}%)")
print(f"Бусад:    {s['other_total']:,}  ({s['other_total']*100//s['grand_total']}%)")
print(f"\n--- Том зардлууд (Top 15) ---")
all_items = r['materials'] + r['labor'] + r['transport'] + r['other']
for i in sorted(all_items, key=lambda x: x['total'], reverse=True)[:15]:
    print(f"  {i['name']:45} {i['total']:>15,}")