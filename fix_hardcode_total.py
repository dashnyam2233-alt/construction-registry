content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''ЧУХАЛ АНХААРУУЛГА — ЗААВАЛ ДАГАХ:
1. НИЙТ ТАЛБАЙ: {area}м² — энэ тоог өөрчлөхгүй ашиглана
2. 1м² БОДИТ ӨРТӨГ (Монгол, 2026):
   - Амины орон сууц эконом: 1,500,000-2,000,000₮/м²
   - Амины орон сууц дунд: 2,000,000-2,800,000₮/м²
   - Олон айлын орон сууц эконом: 1,800,000-2,200,000₮/м²
   - Олон айлын орон сууц дунд: 2,200,000-3,000,000₮/м²
   - Олон айлын орон сууц премиум: 3,000,000-4,500,000₮/м²
   - Оффис дунд: 2,000,000-3,000,000₮/м²
   - Агуулах: 800,000-1,200,000₮/м²
3. grand_total = {area}м² × 1м² өртөг — энэ тооцоог заавал шалгана
4. 500,000₮/м²-аас бага гарвал БУРУУ — дахин тооцоол
5. Материал, ажил, тээвэр, бусад зардлын нийлбэр grand_total-тай таарах ёстой'''

new = '''МАТЕМАТИК ТООЦОО (заавал дагах):
- Нийт талбай: {area}м²
- Барилгын төрөл: {building_type}, чанар: {quality}
- 1м² дундаж өртөг: """ + get_price_per_m2(building_type, quality) + """
- НИЙТ ТӨСӨВ (grand_total) = {area} × 1м² өртөг = """ + calc_grand_total(area, building_type, quality) + """ ₮

Материал 55%, Ажил 25%, Тээвэр 5%, Бусад 15% хуваарилалтаар тооцно.
materials_total = grand_total × 0.55
labor_total = grand_total × 0.25  
transport_total = grand_total × 0.05
other_total = grand_total × 0.15'''

# Энэ арга хэтэрхий нарийн — өөр арга ашиглая
# Prompt-д тооцооллыг Python-д хийж дамжуулах

print("Өөр арга ашиглана...")

# Python-д grand_total-г тооцоолж prompt-д дамжуулах
old2 = '''        prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн. Дараах барилгын төсвийг тооцоолж өгнө үү.'''

new2 = '''        # Grand total-г Python-д урьдчилан тооцоолох
        try:
            area_num = float(area) if area != "мэдэгдэхгүй" else 0
            price_guide = {
                "эконом": {"амины": 1800000, "олон айлын": 2000000, "оффис": 1800000, "агуулах": 900000},
                "дунд":   {"амины": 2500000, "олон айлын": 2500000, "оффис": 2500000, "агуулах": 1100000},
                "премиум":{"амины": 3500000, "олон айлын": 3800000, "оффис": 3500000, "агуулах": 1500000},
            }
            q = quality.lower() if quality else "дунд"
            bt = "олон айлын" if "олон айлын" in building_type.lower() else \
                 "амины" if "амины" in building_type.lower() else \
                 "оффис" if "оффис" in building_type.lower() else \
                 "агуулах" if "агуулах" in building_type.lower() else "олон айлын"
            ppm2 = price_guide.get(q, price_guide["дунд"]).get(bt, 2500000)
            est_grand_total = int(area_num * ppm2)
            est_materials = int(est_grand_total * 0.55)
            est_labor = int(est_grand_total * 0.25)
            est_transport = int(est_grand_total * 0.05)
            est_other = int(est_grand_total * 0.15)
            est_ppm2 = ppm2
        except:
            est_grand_total = 0
            est_materials = 0
            est_labor = 0
            est_transport = 0
            est_other = 0
            est_ppm2 = 2500000

        prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн. Дараах барилгын төсвийг тооцоолж өгнө үү.'''

if old2 in content:
    content = content.replace(old2, new2, 1)
    print("OK 1 — Python тооцоо нэмэгдлээ")
else:
    print("NOT FOUND 1")

# Prompt-д est_ утгуудыг нэмэх
old3 = '''ЧУХАЛ АНХААРУУЛГА — ЗААВАЛ ДАГАХ:
1. НИЙТ ТАЛБАЙ: {area}м² — энэ тоог өөрчлөхгүй ашиглана'''

new3 = '''УРЬДЧИЛСАН ТООЦОО (Python-д бодсон — заавал ашиглах):
- Нийт талбай: {area}м²
- 1м² өртөг: {est_ppm2:,}₮
- Нийт төсөв: {est_grand_total:,}₮
- Материал (55%): {est_materials:,}₮
- Ажил (25%): {est_labor:,}₮
- Тээвэр (5%): {est_transport:,}₮
- Бусад (15%): {est_other:,}₮

Дээрх тооцоог үндэс болгон материал, ажлын жагсаалтыг нарийвчлан гарга.
summary дахь grand_total заавал {est_grand_total:,} орчим байх ёстой.
ЧУХАЛ АНХААРУУЛГА — ЗААВАЛ ДАГАХ:
1. НИЙТ ТАЛБАЙ: {area}м² — энэ тоог өөрчлөхгүй ашиглана'''

if old3 in content:
    content = content.replace(old3, new3, 1)
    print("OK 2 — урьдчилсан тооцоо нэмэгдлээ")
else:
    print("NOT FOUND 2")
    idx = content.find("ЧУХАЛ АНХААРУУЛГА")
    print(repr(content[idx:idx+100]))

open("apps/registry/views.py", "w", encoding="utf-8").write(content)
print("Дууслаа")