import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

views_path = r"apps\registry\views.py"

# calculate_budget функцийн код
CALC_FUNC = '''
def get_material_price(category, name_contains):
    from apps.public.models import MaterialPrice
    items = MaterialPrice.objects.filter(
        is_active=True,
        category=category,
        name__icontains=name_contains
    )
    if items.exists():
        p = items.first()
        return int((p.price_min + p.price_max) / 2)
    return 0

def calculate_budget_norm(data):
    floors = int(str(data.get("floors", 1)).replace("+",""))
    length = float(data.get("length", 10))
    width = float(data.get("width", 10))
    ceiling_h = float(str(data.get("ceiling_height", 2.7)).replace("+",""))

    floor_area = length * width
    total_area = floor_area * floors
    perimeter = 2 * (length + width)
    wall_height = ceiling_h + 0.3
    outer_wall_area = perimeter * wall_height * floors
    inner_wall_area = total_area * 0.35
    roof_area = floor_area * 1.15
    net_wall_area = round(outer_wall_area * 0.85, 1)

    wall_mat = data.get("wall_material", "Мак блок")
    quality = data.get("quality", "дунд").lower()
    foundation_type = data.get("foundation_type", "Шугаман суурь")
    foundation_depth = float(str(data.get("foundation_depth", 2.5)).replace("+","").replace("м",""))
    roof_type = data.get("roof_type", "")
    insulation = data.get("insulation", "")
    facade = data.get("facade", "Шавар штукатур")

    quality_coef = {"эконом": 0.8, "дунд": 1.0, "премиум": 1.35}.get(quality, 1.0)

    materials, labor, transport, other = [], [], [], []

    # 1. СУУРЬ
    if "хавтан" in foundation_type.lower():
        fv = round(floor_area * 0.3, 1)
        rebar_kg = floor_area * 25
        cg = "М300"
    elif "гадсан" in foundation_type.lower() or "нил" in foundation_type.lower():
        fv = round(floor_area * 0.15, 1)
        rebar_kg = floor_area * 20
        cg = "М300"
    else:
        fv = round(perimeter * foundation_depth * 0.5, 1)
        rebar_kg = fv * 80
        cg = "М250"

    rt = round(rebar_kg / 1000, 2)
    cp = get_material_price("mat_cement", "М250") or 270000
    rp = get_material_price("mat_rebar", "A III (d12") or 2500000
    sp = get_material_price("mat_sand", "Дайрга") or 37000
    ep = get_material_price("labor_general", "Газар шорооны") or 27000
    cwp = get_material_price("labor_general", "Бетон цутгалт") or 170000
    rwp = get_material_price("labor_general", "Арматур угсралт") or 1200000

    materials += [
        {"name": f"Бетон зуурмаг {cg} — суурь", "unit": "м³", "qty": fv, "unit_price": cp, "total": round(fv*cp)},
        {"name": "Арматур A III — суурь", "unit": "тонн", "qty": rt, "unit_price": rp, "total": round(rt*rp)},
        {"name": "Дайрга — суурийн доор", "unit": "м³", "qty": round(floor_area*0.1,1), "unit_price": sp, "total": round(floor_area*0.1*sp)},
    ]
    labor += [
        {"name": "Газар ухалт", "unit": "м³", "qty": round(fv*1.3,1), "unit_price": ep, "total": round(fv*1.3*ep)},
        {"name": "Бетон цутгалт — суурь", "unit": "м³", "qty": fv, "unit_price": cwp, "total": round(fv*cwp)},
        {"name": "Арматур угсралт — суурь", "unit": "тонн", "qty": rt, "unit_price": rwp, "total": round(rt*rwp)},
    ]

    # 2. ГАДНА ХАНА
    if "мак блок" in wall_mat.lower():
        bq = round(net_wall_area * 16)
        bp = get_material_price("mat_brick", "Мак блок (25") or 8500
        gp = get_material_price("mat_interior", "Блокны цавуу") or 15000
        wp = get_material_price("labor_general", "Блокон хана өрөх /25") or 25000
        materials += [
            {"name": "Мак блок (25см) — гадна хана", "unit": "ш", "qty": bq, "unit_price": bp, "total": bq*bp},
            {"name": "Блокны цавуу", "unit": "кг", "qty": round(net_wall_area*2), "unit_price": gp, "total": round(net_wall_area*2*gp)},
        ]
        labor.append({"name": "Мак блок хана өрөх", "unit": "м²", "qty": net_wall_area, "unit_price": wp, "total": round(net_wall_area*wp)})
    elif "тоосго" in wall_mat.lower():
        bq = round(net_wall_area * 51)
        bp = get_material_price("mat_brick", "Улаан тоосго") or 515
        wp = get_material_price("labor_general", "Тоосгон хана өрөх /25") or 25000
        materials.append({"name": "Улаан тоосго — гадна хана", "unit": "ш", "qty": bq, "unit_price": bp, "total": bq*bp})
        labor.append({"name": "Тоосгон хана өрөх", "unit": "м²", "qty": net_wall_area, "unit_price": wp, "total": round(net_wall_area*wp)})
    elif "бетон" in wall_mat.lower():
        wv = round(net_wall_area * 0.2, 1)
        cp2 = get_material_price("mat_cement", "М300") or 285000
        wp = get_material_price("labor_general", "Гадна бетон хананы") or 130000
        materials.append({"name": "Бетон зуурмаг М300 — хана", "unit": "м³", "qty": wv, "unit_price": cp2, "total": round(wv*cp2)})
        labor.append({"name": "Бетон хана цутгалт", "unit": "м³", "qty": wv, "unit_price": wp, "total": round(wv*wp)})

    # 3. ДУЛААЛГА
    if insulation and "байхгүй" not in insulation.lower():
        if "шилэн хөвөн" in insulation.lower():
            ip = get_material_price("mat_insulation", "Шилэн хөвөн (100") or 18500
        elif "хөөсөнцөр" in insulation.lower():
            ip = get_material_price("mat_insulation", "Хөөсөнцөр") or 8000
        elif "базальт" in insulation.lower():
            ip = get_material_price("mat_insulation", "Базальт") or 15000
        elif "xps" in insulation.lower():
            ip = get_material_price("mat_insulation", "XPS") or 21000
        else:
            ip = 15000
        iwp = get_material_price("labor_special", "Дулаалга хийх") or 11500
        materials.append({"name": f"Дулаалга ({insulation})", "unit": "м²", "qty": net_wall_area, "unit_price": ip, "total": round(net_wall_area*ip)})
        labor.append({"name": "Дулаалга хийх", "unit": "м²", "qty": net_wall_area, "unit_price": iwp, "total": round(net_wall_area*iwp)})

    # 4. ГАДНА ФАСАД
    plaster_work = get_material_price("labor_special", "Шавардлага") or 23500
    if "тоосго" in facade.lower() or "клинкер" in facade.lower():
        fap = get_material_price("mat_brick", "Өнгөлгөөний тоосго") or 3000
        faq = round(net_wall_area * 51)
        materials.append({"name": "Өнгөлгөөний тоосго — фасад", "unit": "ш", "qty": faq, "unit_price": fap, "total": faq*fap})
        labor.append({"name": "Өнгөлгөөний тоосго өрөх", "unit": "м²", "qty": net_wall_area, "unit_price": 35000, "total": round(net_wall_area*35000)})
    else:
        paint_p = 100000
        paint_q = round(net_wall_area / 8)
        materials += [
            {"name": "Цемент — фасадын шавардлага", "unit": "уут", "qty": round(net_wall_area*0.12), "unit_price": 41500, "total": round(net_wall_area*0.12*41500)},
            {"name": "Гадна фасадын будаг", "unit": "сав", "qty": paint_q, "unit_price": paint_p, "total": paint_q*paint_p},
        ]
        labor.append({"name": "Гадна ханын шавардлага", "unit": "м²", "qty": net_wall_area, "unit_price": plaster_work, "total": round(net_wall_area*plaster_work)})

    # 5. ХУЧИЛТ
    sa = floor_area * (floors-1) if floors > 1 else floor_area
    sv = round(sa * 0.2, 1)
    srt = round(sa * 12 / 1000, 2)
    materials += [
        {"name": "Бетон зуурмаг М250 — хучилт", "unit": "м³", "qty": sv, "unit_price": cp, "total": round(sv*cp)},
        {"name": "Арматур — хучилт", "unit": "тонн", "qty": srt, "unit_price": rp, "total": round(srt*rp)},
    ]
    labor.append({"name": "Бетон цутгалт — хучилт", "unit": "м³", "qty": sv, "unit_price": cwp, "total": round(sv*cwp)})

    # 6. ШАТНЫ БҮТЭЦ
    if floors >= 2:
        stc = round(floors * 2.5, 1)
        str_ = round(floors * 0.2, 2)
        materials += [
            {"name": "Бетон зуурмаг М250 — шат", "unit": "м³", "qty": stc, "unit_price": cp, "total": round(stc*cp)},
            {"name": "Арматур — шат", "unit": "тонн", "qty": str_, "unit_price": rp, "total": round(str_*rp)},
        ]
        labor.append({"name": "Шатны бетон цутгалт", "unit": "м³", "qty": stc, "unit_price": cwp, "total": round(stc*cwp)})

    # 7. ДЭЭВЭР
    if "хавтгай" in roof_type.lower():
        rc = round(roof_area * 0.15, 1)
        rbp = get_material_price("mat_roof", "Рубероид") or 18000
        materials += [
            {"name": "Бетон — хавтгай дээвэр", "unit": "м³", "qty": rc, "unit_price": cp, "total": round(rc*cp)},
            {"name": "Рубероид — ус тусгаарлалт", "unit": "рулон", "qty": round(roof_area/10), "unit_price": rbp, "total": round(roof_area/10*rbp)},
        ]
        labor.append({"name": "Хавтгай дээвэр хийх", "unit": "м²", "qty": round(roof_area,1), "unit_price": 25000, "total": round(roof_area*25000)})
    else:
        if "металл черепица" in roof_type.lower() or "метал" in roof_type.lower():
            rmp = get_material_price("mat_roof", "Металл черепица") or 45000
            rmn = "Металл черепица"
        else:
            rmp = get_material_price("mat_roof", "Профнастил") or 21000
            rmn = "Профнастил"
        wdp = get_material_price("mat_wood", "Тавцан мод") or 5250
        wdq = round(roof_area * 12)
        rwp2 = get_material_price("labor_special", "Төмөр дээвэр") or 26500
        materials += [
            {"name": f"{rmn} — дээвэр", "unit": "м²", "qty": round(roof_area,1), "unit_price": rmp, "total": round(roof_area*rmp)},
            {"name": "Тавцан мод — дээврийн каркас", "unit": "м", "qty": wdq, "unit_price": wdp, "total": wdq*wdp},
        ]
        labor.append({"name": "Дээвэр угсралт", "unit": "м²", "qty": round(roof_area,1), "unit_price": rwp2, "total": round(roof_area*rwp2)})

    # 8. ДОТОР ЗАСАЛ — шал
    wa = round(total_area * 0.25, 1)
    da = round(total_area * 0.75, 1)
    tp = get_material_price("mat_interior", "Керамик плита") or 57000
    tw = get_material_price("labor_general", "Плита наалт") or 40000
    sw = get_material_price("labor_general", "Шалны тэгшилгээ") or 16500
    materials.append({"name": "Керамик плита — ванн, гал тогоо", "unit": "м²", "qty": wa, "unit_price": tp, "total": round(wa*tp)})
    labor.append({"name": "Плита тавих — ванн, гал тогоо", "unit": "м²", "qty": wa, "unit_price": tw, "total": round(wa*tw)})
    floor_mat = data.get("floor_material", "Ламинат")
    if "паркет" in floor_mat.lower():
        fp2 = get_material_price("mat_interior", "Паркет") or 140000
        materials.append({"name": "Паркет — үндсэн өрөө", "unit": "м²", "qty": da, "unit_price": fp2, "total": round(da*fp2)})
        labor.append({"name": "Паркет тавих", "unit": "м²", "qty": da, "unit_price": 26000, "total": round(da*26000)})
    else:
        lp = get_material_price("mat_interior", "Ламинат шал") or 42000
        lw = get_material_price("labor_general", "Ламинат шал тавих") or 19000
        materials.append({"name": "Ламинат шал — үндсэн өрөө", "unit": "м²", "qty": da, "unit_price": lp, "total": round(da*lp)})
        labor.append({"name": "Ламинат шал тавих", "unit": "м²", "qty": da, "unit_price": lw, "total": round(da*lw)})
    labor.append({"name": "Шалны стяжка", "unit": "м²", "qty": total_area, "unit_price": sw, "total": round(total_area*sw)})

    # 9. ДОТОР ХАНЫН ЗАСАЛ
    tis = round((net_wall_area + inner_wall_area * 2) * 0.85)
    zp = get_material_price("mat_interior", "Өнгөлгөөний цагаан замазка") or 12000
    zq = round(tis * 1.2)
    pip = get_material_price("mat_interior", "Дотор будаг") or 7500
    piq = round(tis * 0.3)
    materials += [
        {"name": "Цагаан замазка — дотор хана, тааз", "unit": "кг", "qty": zq, "unit_price": zp, "total": zq*zp},
        {"name": "Дотор эмульс будаг", "unit": "кг", "qty": piq, "unit_price": pip, "total": piq*pip},
    ]
    zwp = get_material_price("labor_special", "Цагаан замаска") or 14000
    pwp = get_material_price("labor_special", "Эмульс хийх") or 6750
    labor += [
        {"name": "Замазка хийх — дотор хана, тааз", "unit": "м²", "qty": tis, "unit_price": zwp, "total": tis*zwp},
        {"name": "Эмульс будаг — дотор хана, тааз", "unit": "м²", "qty": tis, "unit_price": pwp, "total": tis*pwp},
    ]

    # 10. ДОТОР ХУВААЛТ
    ibp = get_material_price("mat_brick", "Мак блок (20") or 7000
    iwp2 = get_material_price("labor_general", "Блокон хана өрөх /25") or 25000
    ibq = round(inner_wall_area * 16)
    materials.append({"name": "Мак блок (20см) — дотор хуваалт", "unit": "ш", "qty": ibq, "unit_price": ibp, "total": ibq*ibp})
    labor.append({"name": "Дотор хуваалт өрөх", "unit": "м²", "qty": round(inner_wall_area,1), "unit_price": iwp2, "total": round(inner_wall_area*iwp2)})

    # 11. ЦОНХ, ХААЛГА
    try:
        wna = int(str(data.get("windows","5")).split("-")[0])
    except:
        wna = 5
    try:
        dna = int(str(data.get("doors","4")).split("-")[0])
    except:
        dna = 4
    upf = int(str(data.get("units_per_floor",1)).replace("+",""))
    tu = max(1, upf * floors)
    tw2 = tu * wna
    td = tu * dna
    wnp = get_material_price("mat_window", "PVC цонх (1.2") or 450000
    dnp = get_material_price("mat_window", "Дотор хаалга") or 420000
    odp = get_material_price("mat_window", "Гадна хаалга (металл)") or 1150000
    wip = get_material_price("labor_special", "Хаалга угсрах (дотор") or 65000
    materials += [
        {"name": "PVC цонх (1.2x1.2м)", "unit": "ш", "qty": tw2, "unit_price": wnp, "total": tw2*wnp},
        {"name": "Дотор хаалга", "unit": "ш", "qty": td, "unit_price": dnp, "total": td*dnp},
        {"name": "Гадна хаалга (металл)", "unit": "ш", "qty": tu, "unit_price": odp, "total": tu*odp},
    ]
    labor.append({"name": "Цонх, хаалга угсралт", "unit": "ш", "qty": tw2+td, "unit_price": wip, "total": (tw2+td)*wip})

    # 12. ЦАХИЛГААНЫ СИСТЕМ
    cbp = get_material_price("mat_electrical", "Кабель ВВГ") or 3600
    cbq = round(total_area * 4)
    swp = get_material_price("mat_electrical", "Унтраалга 1") or 6100
    sop = get_material_price("mat_electrical", "Розетка 1") or 6600
    swq = round(tu * 8)
    soq = round(tu * 12)
    ewp = get_material_price("labor_general", "Цахилгаанчин") or 125000
    edp = round(total_area / 15)
    materials += [
        {"name": "Цахилгааны кабель ВВГ", "unit": "м", "qty": cbq, "unit_price": cbp, "total": cbq*cbp},
        {"name": "Унтраалга", "unit": "ш", "qty": swq, "unit_price": swp, "total": swq*swp},
        {"name": "Розетка", "unit": "ш", "qty": soq, "unit_price": sop, "total": soq*sop},
    ]
    labor.append({"name": "Цахилгааны ажил", "unit": "өдөр", "qty": edp, "unit_price": ewp, "total": edp*ewp})

    # 13. ИНЖЕНЕРИЙН СИСТЕМ
    htp = get_material_price("mat_plumbing", "Халаалтын систем") or 6750000
    wtp = get_material_price("mat_plumbing", "Цэвэр усны систем") or 1025000
    sgp = get_material_price("mat_plumbing", "Бохир усны систем") or 200000
    sap = get_material_price("mat_plumbing", "Ариун цэврийн өрөөний") or 1850000
    materials += [
        {"name": "Халаалтын систем", "unit": "багц", "qty": tu, "unit_price": htp, "total": tu*htp},
        {"name": "Цэвэр усны систем", "unit": "багц", "qty": tu, "unit_price": wtp, "total": tu*wtp},
        {"name": "Бохир усны систем", "unit": "багц", "qty": tu, "unit_price": sgp, "total": tu*sgp},
        {"name": "Ариун цэврийн тоноглол", "unit": "багц", "qty": tu, "unit_price": sap, "total": tu*sap},
    ]

    # 14. ТЭЭВЭР
    trp = get_material_price("transport_material", "Материал тээвэр") or 90000
    wsp = get_material_price("transport_material", "Хог зайлуулах") or 80000
    trt = max(10, round(total_area / 15))
    transport += [
        {"name": "Материал тээвэр", "unit": "удаа", "qty": trt, "unit_price": trp, "total": trt*trp},
        {"name": "Хог зайлуулах", "unit": "удаа", "qty": round(trt/2), "unit_price": wsp, "total": round(trt/2)*wsp},
    ]

    # 15. БУСАД
    duration = max(6, round(total_area / 60))
    dsp = get_material_price("other_design", "Архитектурын") or 25000
    pmp = get_material_price("other_permit", "Барилгын зөвшөөрөл") or 1250000
    inp2 = get_material_price("other_insurance", "Барилгын даатгал") or 1250000
    other += [
        {"name": "Архитектур, инженерийн зураг төсөл", "unit": "м²", "qty": round(total_area), "unit_price": dsp, "total": round(total_area*dsp)},
        {"name": "Барилгын зөвшөөрөл", "unit": "удаа", "qty": 1, "unit_price": pmp, "total": pmp},
        {"name": "Инженер хяналт", "unit": "сар", "qty": duration, "unit_price": 1750000, "total": duration*1750000},
        {"name": "Барилгын даатгал", "unit": "жил", "qty": max(1,round(duration/12)), "unit_price": inp2, "total": max(1,round(duration/12))*inp2},
    ]

    mt = round(sum(i["total"] for i in materials) * quality_coef)
    lt = round(sum(i["total"] for i in labor) * quality_coef)
    tt = sum(i["total"] for i in transport)
    ot = sum(i["total"] for i in other)
    gt = mt + lt + tt + ot
    ppm2 = round(gt / total_area) if total_area > 0 else 0

    return {
        "building_info": {
            "type": data.get("building_type",""),
            "area": f"{total_area:.0f} м²",
            "floors": str(floors),
            "location": data.get("location","Улаанбаатар"),
            "quality": data.get("quality","дунд"),
        },
        "materials": materials,
        "labor": labor,
        "transport": transport,
        "other": other,
        "summary": {
            "materials_total": mt,
            "labor_total": lt,
            "transport_total": tt,
            "other_total": ot,
            "grand_total": gt,
            "price_per_m2": ppm2,
            "duration_months": duration,
        },
        "notes": "⚠️ Энэ тооцоо ойролцоо үнэлгээ бөгөөд мэргэжлийн инженерийн тооцоог орлохгүй. Бодит зардал газрын байршил, ханган нийлүүлэгч, нарийн зураг төслөөс хамаарч өөрчлөгдөж болно. Гэрээ байгуулахаасаа өмнө мэргэжлийн байгууллагаар нарийвчилсан тооцоо гаргуулна уу."
    }
'''

with open(views_path, "r", encoding="utf-8") as f:
    content = f.read()

# budget_calculator функцийн эхэнд нэмэх
old = "def budget_calculator(request):"
new = CALC_FUNC + "\ndef budget_calculator(request):"

if old in content:
    if "calculate_budget_norm" not in content:
        content = content.replace(old, new, 1)
        with open(views_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("DONE - calculate_budget_norm нэмэгдлээ")
    else:
        print("SKIP - аль хэдийн байна")
else:
    print("NOT FOUND")