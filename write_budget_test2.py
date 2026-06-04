import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# write_budget_norm.py-аас calculate_budget функцийг import хийх
exec(open('write_budget_norm.py', encoding='utf-8').read().split('# Туршилт')[0])

test1 = {
    'building_type': 'Амины орон сууц (1-2 давхар)',
    'floors': '1', 'length': '10', 'width': '8',
    'ceiling_height': '2.7', 'wall_material': 'Мак блок',
    'insulation': 'Шилэн хөвөн 10см',
    'foundation_type': 'Шугаман суурь', 'foundation_depth': '2.5',
    'roof_type': 'Налуу дээвэр (метал)', 'floor_material': 'Ламинат',
    'facade': 'Шавар штукатур', 'wall_finish': 'Хосолсон',
    'electrical': 'Стандарт 220В',
    'heating': 'Бие даасан зуух', 'windows': '5-6', 'doors': '4-5',
    'quality': 'дунд', 'units_per_floor': '1', 'location': 'Улаанбаатар',
}

test2 = dict(test1)
test2.update({'floors': '2', 'length': '12', 'width': '10'})

for t in [test1, test2]:
    r = calculate_budget(t)
    s = r['summary']
    print(f"Талбай: {r['building_info']['area']:10} | НИЙТ: {s['grand_total']:>15,}₮ | 1м²: {s['price_per_m2']:>12,}₮")