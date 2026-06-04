import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

exec(open('write_budget_norm.py', encoding='utf-8').read().split('# Туршилт')[0])

# 40x18, 8 давхар
floors, length, width = 8, 40, 18
floor_area = length * width  # 720м²
total_area = floor_area * floors  # 5760м²
perimeter = 2 * (length + width)  # 116м

print(f"Нийт талбай: {total_area}м²")
print(f"Нэг давхрын талбай: {floor_area}м²")
print(f"Периметр: {perimeter}м")
print()

# Нил суурь
fv_nil = round(floor_area * 0.15, 1)
rebar_nil = floor_area * 20
print(f"НИЛ СУУРЬ:")
print(f"  Бетон: {fv_nil}м³  (floor_area × 0.15)")
print(f"  Арматур: {rebar_nil/1000:.2f}тонн")
print(f"  → Хэт бага! 720м² барилгад дор хаяж 200м³ бетон хэрэгтэй")
print()

# Хавтан суурь
fv_hvt = round(floor_area * 0.3, 1)
rebar_hvt = floor_area * 25
print(f"ХАВТАН СУУРЬ:")
print(f"  Бетон: {fv_hvt}м³")
print(f"  Арматур: {rebar_hvt/1000:.2f}тонн")
print()

# Хучилт — 8 давхар
slab_area = floor_area * (floors - 1)  # 7 давхар хоорондын
sv = round(slab_area * 0.2, 1)
srt = round(slab_area * 12 / 1000, 2)
print(f"ХУЧИЛТ (7 давхар × {floor_area}м²):")
print(f"  Нийт хучилтын талбай: {slab_area}м²")
print(f"  Бетон: {sv}м³  (× 0.2)")
print(f"  Арматур: {srt}тонн  (12кг/м²)")
print(f"  → Бетон зөв, арматур хэт бага (25кг/м² байх ёстой)")
print()

# Зөв тооцоо
print(f"ЗӨВЛӨМЖ:")
print(f"  Нил суурь: floor_area × 0.4 = {floor_area*0.4:.0f}м³ бетон")
print(f"  Хучилтын арматур: 25кг/м² = {slab_area*25/1000:.1f}тонн")
print(f"  Колонн, дам нуруу (олон давхарт): {floor_area*floors*0.05:.0f}тонн арматур нэмэх")