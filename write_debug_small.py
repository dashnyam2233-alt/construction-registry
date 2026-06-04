import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

exec(open('write_budget_norm.py', encoding='utf-8').read().split('# Туршилт')[0])

tests = [
    ('Амины 80м²', {'building_type':'Амины орон сууц (1-2 давхар)','floors':'1','length':'10','width':'8','ceiling_height':'2.7','wall_material':'Мак блок','insulation':'Шилэн хөвөн 10см','foundation_type':'Шугаман суурь','foundation_depth':'2.5','roof_type':'Налуу дээвэр (метал)','floor_material':'Ламинат','facade':'Шавар штукатур','wall_finish':'Хосолсон','electrical':'Стандарт 220В','heating':'Бие даасан зуух','windows':'5-6','doors':'4-5','quality':'дунд','units_per_floor':'1','location':'Улаанбаатар'}),
    ('Амины 240м² 2давхар', {'building_type':'Амины орон сууц (1-2 давхар)','floors':'2','length':'12','width':'10','ceiling_height':'2.7','wall_material':'Мак блок','insulation':'Шилэн хөвөн 10см','foundation_type':'Шугаман суурь','foundation_depth':'2.5','roof_type':'Налуу дээвэр (метал)','floor_material':'Ламинат','facade':'Шавар штукатур','wall_finish':'Хосолсон','electrical':'Стандарт 220В','heating':'Бие даасан зуух','windows':'5-6','doors':'4-5','quality':'дунд','units_per_floor':'1','location':'Улаанбаатар'}),
    ('Олон айлын 4давхар', {'building_type':'Олон айлын орон сууц','floors':'4','length':'40','width':'18','ceiling_height':'2.7','wall_material':'Мак блок','insulation':'Шилэн хөвөн 10см','foundation_type':'Хавтан суурь','foundation_depth':'2.5','roof_type':'Хавтгай дээвэр','floor_material':'Ламинат','facade':'Шавар штукатур','wall_finish':'Хосолсон','electrical':'Гурван фаз 380В','heating':'Төвийн халаалт','windows':'5-6','doors':'4-5','quality':'дунд','units_per_floor':'4','location':'Улаанбаатар'}),
    ('Олон айлын 8давхар', {'building_type':'Олон айлын орон сууц','floors':'8','length':'40','width':'18','ceiling_height':'2.7','wall_material':'Мак блок','insulation':'Шилэн хөвөн 10см','foundation_type':'Нил суурь','foundation_depth':'3.0','roof_type':'Хавтгай дээвэр','floor_material':'Ламинат','facade':'Шавар штукатур','wall_finish':'Хосолсон','electrical':'Гурван фаз 380В','heating':'Төвийн халаалт','windows':'5-6','doors':'4-5','quality':'дунд','units_per_floor':'4','location':'Улаанбаатар'}),
]

print(f"\n{'='*65}")
print(f"{'Барилга':25} {'Талбай':8} {'Нийт':18} {'1м²':12} {'OK?'}")
print(f"{'='*65}")
for name, d in tests:
    r = calculate_budget(d)
    s = r['summary']
    ok = 'OK' if 1800000 <= s['price_per_m2'] <= 4500000 else 'БУРУУ'
    print(f"{name:25} {r['building_info']['area']:8} {s['grand_total']:>18,} {s['price_per_m2']:>12,} {ok}")
print(f"{'='*65}")
print("Зорилт: 1,800,000-4,500,000/м²")