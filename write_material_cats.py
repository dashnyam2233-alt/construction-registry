import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()

content = open("apps/public/models.py", "r", encoding="utf-8").read()

MATERIAL_DATA = '''
    MAIN_CATEGORIES = [
        ("material", "Материал"),
        ("house", "Орон сууц, барилга"),
        ("worker", "Ажилтан, бригад"),
        ("repair", "Засвар үйлчилгээ"),
        ("other", "Бусад"),
    ]

    MATERIAL_SUBCATEGORIES = [
        ("foundation", "1. Барилгын үндсэн хийц материал"),
        ("interior", "2. Засал чимэглэл"),
        ("outdoor", "3. Гадна тохижилт"),
        ("plumbing", "4. Сан, халаалт, агааржуулалт"),
        ("electrical", "5. Цахилгаан, холбоо, дохиолол"),
        ("machinery", "6. Машин механизм тоног төхөөрөмж"),
        ("furniture", "7. Тавилга"),
        ("software", "8. Программ хангамж, ном гарын авлага"),
        ("safety", "9. ХАБЭА"),
    ]

    MATERIAL_ITEMS = {
        "foundation": [
            ("rebar", "Арматур төмөр материал"),
            ("metal_structure", "Металь хийц"),
            ("concrete", "Бетон зуурмаг"),
            ("insulation", "Дулаан дуу тусгаарлах материал"),
            ("roof_material", "Дээврийн материал"),
            ("formwork", "Хэв хашмал"),
            ("brick_block", "Тоосго блок"),
            ("wood", "Модон материал"),
            ("door_window", "Цонх хаалга"),
            ("glass", "Шилэн хийц"),
            ("cement_lime", "Цемент шохой"),
            ("sand_gravel", "Элс хайрга дайрга"),
            ("facade", "Гадна фасад"),
        ],
        "interior": [
            ("paint", "Будаг эмульс"),
            ("dry_mix", "Хуурай хольц"),
            ("wallpaper", "Обой хуулга"),
            ("parquet", "Паркет ламинат"),
            ("floor_accessories", "Шал дагалдах"),
            ("tile_stone", "Плита чулуу"),
            ("decoration", "Гоёл чимэглэл"),
            ("curtain", "Хөшиг тюль"),
        ],
        "outdoor": [
            ("paving", "Замын хавтан болон бродюр"),
            ("fence_gate", "Хашаа гадна хаалга"),
            ("playground", "Хүүхдийн тоглоом талбай"),
            ("landscaping", "Мод зүлэгжүүлэлт"),
            ("cleaning", "Цэвэрлэгээ тоног төхөөрөмж"),
        ],
        "plumbing": [
            ("pipe_fitting", "Шугам хоолой холбох хэрэгсэл"),
            ("heating", "Халаах хэрэгсэл"),
            ("sanitary", "Угаалтуур суултуур ванн"),
            ("ventilation", "Агааржуулалт хөргөлт"),
        ],
        "electrical": [
            ("wire_cable", "Цахилгааны утас кабель"),
            ("electrical_fitting", "Цахилгаан холбох хэрэгсэл"),
            ("lighting", "Гэрэл гэрэлтүүлэг"),
            ("generator_meter", "Цахилгааны үүсгүүр тоолуур"),
            ("switch_socket", "Унтраалга залгуур"),
            ("signal", "Холбоо дохиолол"),
            ("fire_alarm", "Галын дохиолол"),
            ("domophone", "Домофон ухаалаг цоож"),
            ("internet_tv", "Интернэт ТВ"),
        ],
        "machinery": [
            ("machine", "Машин механизм"),
            ("construction_equipment", "Барилгын тоног төхөөрөмж"),
            ("tools", "Барилгын багаж хэрэгсэл"),
            ("elevator", "Лифт угсардаг шат"),
        ],
        "furniture": [
            ("office", "Албан тасалгаа"),
            ("household", "Гэр ахуй"),
        ],
        "software": [
            ("software", "Программ хангамж"),
            ("book", "Ном сэтгүүл"),
            ("manual", "Гарын авлага"),
        ],
        "safety": [
            ("safety_equipment", "ХАБЭА хэрэгсэл"),
        ],
    }
'''

# Ad model-д талбарууд нэмэх
addon = '''    material_subcategory = models.CharField(
        "Материалын үндсэн ангилал", max_length=30, blank=True, default=""
    )
    material_item = models.CharField(
        "Материалын дэд ангилал", max_length=30, blank=True, default=""
    )
    price_unit = models.CharField(
        "Үнийн нэгж", max_length=20, blank=True, default="",
        choices=[
            ("ton", "₮ / тонн"),
            ("piece", "₮ / ш"),
            ("m2", "₮ / м²"),
            ("m3", "₮ / м³"),
            ("kg", "₮ / кг"),
            ("meter", "₮ / м"),
            ("negotiable", "Тохиролцоно"),
        ]
    )
'''

if "material_subcategory" not in content:
    content = content.replace(
        '    contact_name = models.CharField("Холбоо барих нэр"',
        addon + '    contact_name = models.CharField("Холбоо барих нэр"'
    )
    open("apps/public/models.py", "w", encoding="utf-8").write(content)
    print("OK — талбарууд нэмэгдлээ")
else:
    print("Аль хэдийн байна")

# MATERIAL_ITEMS-г JSON файлд хадгалах — template-д ашиглана
import json

MATERIAL_ITEMS = {
    "foundation": [
        ("rebar", "Арматур төмөр материал"),
        ("metal_structure", "Металь хийц"),
        ("concrete", "Бетон зуурмаг"),
        ("insulation", "Дулаан дуу тусгаарлах материал"),
        ("roof_material", "Дээврийн материал"),
        ("formwork", "Хэв хашмал"),
        ("brick_block", "Тоосго блок"),
        ("wood", "Модон материал"),
        ("door_window", "Цонх хаалга"),
        ("glass", "Шилэн хийц"),
        ("cement_lime", "Цемент шохой"),
        ("sand_gravel", "Элс хайрга дайрга"),
        ("facade", "Гадна фасад"),
    ],
    "interior": [
        ("paint", "Будаг эмульс"),
        ("dry_mix", "Хуурай хольц"),
        ("wallpaper", "Обой хуулга"),
        ("parquet", "Паркет ламинат"),
        ("floor_accessories", "Шал дагалдах"),
        ("tile_stone", "Плита чулуу"),
        ("decoration", "Гоёл чимэглэл"),
        ("curtain", "Хөшиг тюль"),
    ],
    "outdoor": [
        ("paving", "Замын хавтан болон бродюр"),
        ("fence_gate", "Хашаа гадна хаалга"),
        ("playground", "Хүүхдийн тоглоом талбай"),
        ("landscaping", "Мод зүлэгжүүлэлт"),
        ("cleaning", "Цэвэрлэгээ тоног төхөөрөмж"),
    ],
    "plumbing": [
        ("pipe_fitting", "Шугам хоолой холбох хэрэгсэл"),
        ("heating", "Халаах хэрэгсэл"),
        ("sanitary", "Угаалтуур суултуур ванн"),
        ("ventilation", "Агааржуулалт хөргөлт"),
    ],
    "electrical": [
        ("wire_cable", "Цахилгааны утас кабель"),
        ("electrical_fitting", "Цахилгаан холбох хэрэгсэл"),
        ("lighting", "Гэрэл гэрэлтүүлэг"),
        ("generator_meter", "Цахилгааны үүсгүүр тоолуур"),
        ("switch_socket", "Унтраалга залгуур"),
        ("signal", "Холбоо дохиолол"),
        ("fire_alarm", "Галын дохиолол"),
        ("domophone", "Домофон ухаалаг цоож"),
        ("internet_tv", "Интернэт ТВ"),
    ],
    "machinery": [
        ("machine", "Машин механизм"),
        ("construction_equipment", "Барилгын тоног төхөөрөмж"),
        ("tools", "Барилгын багаж хэрэгсэл"),
        ("elevator", "Лифт угсардаг шат"),
    ],
    "furniture": [
        ("office", "Албан тасалгаа"),
        ("household", "Гэр ахуй"),
    ],
    "software": [
        ("software_item", "Программ хангамж"),
        ("book", "Ном сэтгүүл"),
        ("manual", "Гарын авлага"),
    ],
    "safety": [
        ("safety_equipment", "ХАБЭА хэрэгсэл"),
    ],
}

# dict болгон хөрвүүлэх
items_dict = {k: dict(v) for k, v in MATERIAL_ITEMS.items()}
with open("material_items.json", "w", encoding="utf-8") as f:
    json.dump(items_dict, f, ensure_ascii=False, indent=2)
print("OK — material_items.json үүслээ")