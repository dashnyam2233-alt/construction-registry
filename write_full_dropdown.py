import json

SUBCATS = {
    "foundation": ("🏗 Барилгын үндсэн хийц материал", [
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
    ]),
    "interior": ("🎨 Засал чимэглэл", [
        ("paint", "Будаг эмульс"),
        ("dry_mix", "Хуурай хольц"),
        ("wallpaper", "Обой хуулга"),
        ("parquet", "Паркет ламинат"),
        ("floor_accessories", "Шал дагалдах"),
        ("tile_stone", "Плита чулуу"),
        ("decoration", "Гоёл чимэглэл"),
        ("curtain", "Хөшиг тюль"),
    ]),
    "outdoor": ("🌿 Гадна тохижилт", [
        ("paving", "Замын хавтан болон бродюр"),
        ("fence_gate", "Хашаа гадна хаалга"),
        ("playground", "Хүүхдийн тоглоом талбай"),
        ("landscaping", "Мод зүлэгжүүлэлт"),
        ("cleaning", "Цэвэрлэгээ түүний тоног төхөөрөмж"),
    ]),
    "plumbing": ("🚿 Сан, халаалт, агааржуулалт", [
        ("pipe_fitting", "Шугам хоолой холбох хэрэгсэл"),
        ("heating", "Халаах хэрэгсэл"),
        ("sanitary", "Угаалтуур суултуур ванн"),
        ("ventilation", "Агааржуулалт хөргөлт"),
    ]),
    "electrical": ("⚡ Цахилгаан, холбоо, дохиолол", [
        ("wire_cable", "Цахилгааны утас кабель"),
        ("electrical_fitting", "Цахилгаан холбох хэрэгсэл"),
        ("lighting", "Гэрэл гэрэлтүүлэг"),
        ("generator_meter", "Цахилгааны үүсгүүр тоолуур"),
        ("switch_socket", "Унтраалга залгуур"),
        ("signal", "Холбоо дохиолол"),
        ("fire_alarm", "Галын дохиолол"),
        ("domophone", "Домофон ухаалаг цоож"),
        ("internet_tv", "Интернэт ТВ"),
    ]),
    "machinery": ("🔩 Машин механизм тоног төхөөрөмж", [
        ("machine", "Машин механизм"),
        ("construction_equipment", "Барилгын тоног төхөөрөмж"),
        ("tools", "Барилгын багаж хэрэгсэл"),
        ("elevator", "Лифт угсардаг шат"),
    ]),
    "furniture": ("🪑 Тавилга", [
        ("office", "Албан тасалгаа"),
        ("household", "Гэр ахуй"),
    ]),
    "software": ("💻 Программ хангамж ном гарын авлага", [
        ("software_item", "Программ хангамж"),
        ("book", "Ном сэтгүүл"),
        ("manual", "Гарын авлага"),
    ]),
    "safety": ("🦺 ХАБЭА", [
        ("safety_equipment", "ХАБЭА хэрэгсэл"),
    ]),
}

# material_items.json шинэчлэх
items_dict = {k: dict(v[1]) for k, v in SUBCATS.items()}
with open("material_items.json", "w", encoding="utf-8") as f:
    json.dump(items_dict, f, ensure_ascii=False, indent=2)
print("OK — material_items.json шинэчлэгдлээ")

# Template-д optgroup бүхий dropdown үүсгэх
options = '      <option value="">📋 Бүх дэд ангилал</option>\n'
for code, (label, items) in SUBCATS.items():
    options += f'      <optgroup label="{label}">\n'
    options += f'        <option value="{code}" {{% if subcat == "{code}" %}}selected{{% endif %}}>— Бүгд —</option>\n'
    for icode, ilabel in items:
        options += f'        <option value="{code}__{icode}" {{% if item == "{icode}" and subcat == "{code}" %}}selected{{% endif %}}>{ilabel}</option>\n'
    options += '      </optgroup>\n'

content = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").read()

# subcat-sel-ийн option хэсгийг олж солих
import re
pattern = r'(<select class="search-sel" name="subcat"[^>]*>)(.*?)(</select>)'
replacement = r'\1\n' + options + r'    \3'
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if new_content != content:
    open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(new_content)
    print("OK — dropdown шинэчлэгдлээ")
else:
    print("NOT FOUND — гараар засна")