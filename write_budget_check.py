import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

exec(open('write_budget_norm.py', encoding='utf-8').read().split('# Туршилт')[0])

test = {
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

r = calculate_budget(test)
s = r['summary']

print(f"\nТалбай: 80м²")
print(f"Зорилтот үнэ: 200,000,000-280,000,000₮ (2.5-3.5 сая/м²)")
print(f"Одоогийн дүн: {s['grand_total']:,}₮  ({s['price_per_m2']:,}₮/м²)")
print(f"\nЗөрүү: {200000000 - s['grand_total']:,}₮ дутуу байна")
print(f"\n--- Бүлэг бүрийн дүн ---")
print(f"Материал: {s['materials_total']:>15,}₮  ({s['materials_total']*100//s['grand_total']}%)")
print(f"Ажил:     {s['labor_total']:>15,}₮  ({s['labor_total']*100//s['grand_total']}%)")
print(f"Тээвэр:   {s['transport_total']:>15,}₮  ({s['transport_total']*100//s['grand_total']}%)")
print(f"Бусад:    {s['other_total']:>15,}₮  ({s['other_total']*100//s['grand_total']}%)")
print(f"\n--- Дутуу зүйлс шалгах ---")
# Барилгын бодит зардлын харьцаа
# Материал 50-55%, Ажил 25-30%, Тээвэр 5%, Бусад 15-20%
target = 250000000  # 80м² × 3,000,000₮/м²
print(f"\nХэрэв 3,000,000₮/м² байвал:")
print(f"  Материал (52%): {int(target*0.52):,}₮")
print(f"  Ажил (28%):     {int(target*0.28):,}₮")
print(f"  Тээвэр (5%):    {int(target*0.05):,}₮")
print(f"  Бусад (15%):    {int(target*0.15):,}₮")
print(f"  НИЙТ:           {target:,}₮")
print(f"\nОдоогийн материал: {s['materials_total']:,}₮  (зорилт: {int(target*0.52):,}₮)")
print(f"Зөрүү:             {int(target*0.52) - s['materials_total']:,}₮")