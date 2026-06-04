import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

exec(open('write_budget_norm.py', encoding='utf-8').read().split('# Туршилт')[0])

# Олон айлын орон сууц том барилга туршилт
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
print(f"Талбай: {r['building_info']['area']}")
print(f"НИЙТ:   {s['grand_total']:,}₮")
print(f"1м²:    {s['price_per_m2']:,}₮")
print(f"Хугацаа: {s['duration_months']} сар")
print(f"\nЗураг төсөл: {round(float(r['building_info']['area'].replace(' м²',''))*25000):,}₮")
print(f"Инженер хяналт: {s['duration_months']} сар × 1,750,000₮ = {s['duration_months']*1750000:,}₮")