content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''        # Талбай тооцоолох
        try:
            area = str(float(length) * float(width)) if length and width else "мэдэгдэхгүй"
        except:
            area = "мэдэгдэхгүй"'''

new = '''        # Талбай тооцоолох — нийт давхрын талбай
        try:
            one_floor_area = float(length) * float(width) if length and width else 0
            total_floors = int(floors) if floors else 1
            total_area = one_floor_area * total_floors
            area = f"{total_area:.0f}" if total_area > 0 else "мэдэгдэхгүй"
            area_detail = f"{one_floor_area:.0f}м² × {total_floors} давхар = {total_area:.0f}м²"
        except:
            area = "мэдэгдэхгүй"
            area_detail = ""'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK — талбай засагдлаа")
else:
    print("NOT FOUND 1")

# Prompt-д area_detail нэмэх
old2 = '''- Зориулалт: {building_type}
- Давхар: {floors}
- Байршил: {location}
- Чанар: {quality}
- Барилгын жил: {build_year}

Хэмжээс:
- Урт x Өргөн: {length}м x {width}м
- Нийт өндөр: {total_height}м
- Тааз өндөр: {ceiling_height}м
- Нийт талбай: {area} м²'''

new2 = '''- Зориулалт: {building_type}
- Давхар: {floors}
- Байршил: {location}
- Чанар: {quality}
- Барилгын жил: {build_year}

Хэмжээс:
- Урт x Өргөн: {length}м x {width}м
- Нийт өндөр: {total_height}м
- Тааз өндөр: {ceiling_height}м
- Нэг давхрын талбай: {one_floor_area:.0f}м²
- Нийт давхрын тоо: {total_floors}
- НИЙТ ТАЛБАЙ: {area}м² ({area_detail})

АНХААРУУЛГА: Нийт талбай нь {area}м² байна. 1м²-ийн өртөг Монголд дунд чанарын барилгад 1,500,000-2,500,000₮ байдаг. Энэ дүнгээс бага гарвал буруу!'''

if old2 in content:
    content = content.replace(old2, new2, 1)
    print("OK — prompt засагдлаа")
else:
    print("NOT FOUND 2")

# f-string-д one_floor_area, total_floors нэмэгдсэн тул format засах
old3 = 'Монголын 2024-2025 оны үнийн мэдээлэлд үндэслэн ЗӨВХӨН JSON форматаар хариу өгнө үү.'
new3 = '''Монголын 2025-2026 оны үнийн мэдээлэлд үндэслэн ЗӨВХӨН JSON форматаар хариу өгнө үү.
ЧУХАЛ: 
- Нийт талбай {area}м² байна — энийг заавал ашиглана
- 1м² өртөг {quality} чанарт: эконом=1,200,000-1,500,000₮, дунд=1,500,000-2,200,000₮, премиум=2,500,000-4,000,000₮
- grand_total = нийт талбай × 1м² өртөг байх ёстой'''

if old3 in content:
    content = content.replace(old3, new3, 1)
    print("OK — үнийн чиглэл нэмэгдлээ")
else:
    print("NOT FOUND 3")

open("apps/registry/views.py", "w", encoding="utf-8").write(content)
print("Дууслаа")