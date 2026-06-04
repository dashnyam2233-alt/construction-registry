import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def get_price(category, name_contains):
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

def calculate_budget(data):
    floors = int(str(data.get('floors', 1)).replace('+',''))
    length = float(data.get('length', 10))
    width = float(data.get('width', 10))
    ceiling_h = float(str(data.get('ceiling_height', 2.7)).replace('+',''))

    floor_area = length * width
    total_area = floor_area * floors
    perimeter = 2 * (length + width)
    wall_height = ceiling_h + 0.3
    outer_wall_area = perimeter * wall_height * floors
    inner_wall_area = total_area * 0.35
    roof_area = floor_area * 1.15
    net_wall_area = round(outer_wall_area * 0.85, 1)
    total_inner_surface = round((net_wall_area + inner_wall_area * 2) * 0.85)

    building_type = data.get('building_type', '')
    wall_mat = data.get('wall_material', 'Мак блок')
    quality = data.get('quality', 'дунд').lower()
    foundation_type = data.get('foundation_type', 'Шугаман суурь')
    foundation_depth = float(str(data.get('foundation_depth', 2.5)).replace('+','').replace('м',''))
    roof_type = data.get('roof_type', '')
    insulation = data.get('insulation', '')
    facade = data.get('facade', 'Шавар штукатур')

    quality_coef = {'эконом': 0.8, 'дунд': 1.0, 'премиум': 1.35}.get(quality, 1.0)

    materials, labor, transport, other = [], [], [], []

    # ============================================================
    # 1. СУУРЬ
    # ============================================================
    if 'хавтан' in foundation_type.lower():
        fv = round(floor_area * 0.3, 1)
        rebar_kg = floor_area * 25
        cg = 'М300'
    elif 'гадсан' in foundation_type.lower() or 'нил' in foundation_type.lower():
        fv = round(floor_area * 0.4, 1)
        rebar_kg = floor_area * 35
        cg = 'М300'
    else:
        fv = round(perimeter * foundation_depth * 0.5, 1)
        rebar_kg = fv * 80
        cg = 'М250'

    rt = round(rebar_kg / 1000, 2)
    cp = get_price('mat_cement', 'М250') or 270000
    rp = get_price('mat_rebar', 'A III (d12') or 2500000
    sp = get_price('mat_sand', 'Дайрга') or 37000
    ep = get_price('labor_general', 'Газар шорооны') or 27000
    cwp = get_price('labor_general', 'Бетон цутгалт') or 170000
    rwp = get_price('labor_general', 'Арматур угсралт') or 1200000

    materials += [
        {'name': f'Бетон зуурмаг {cg} — суурь', 'unit': 'м³', 'qty': fv, 'unit_price': cp, 'total': round(fv*cp)},
        {'name': 'Арматур A III — суурь', 'unit': 'тонн', 'qty': rt, 'unit_price': rp, 'total': round(rt*rp)},
        {'name': 'Дайрга — суурийн доор', 'unit': 'м³', 'qty': round(floor_area*0.1,1), 'unit_price': sp, 'total': round(floor_area*0.1*sp)},
    ]
    labor += [
        {'name': 'Газар ухалт', 'unit': 'м³', 'qty': round(fv*1.3,1), 'unit_price': ep, 'total': round(fv*1.3*ep)},
        {'name': 'Бетон цутгалт — суурь', 'unit': 'м³', 'qty': fv, 'unit_price': cwp, 'total': round(fv*cwp)},
        {'name': 'Арматур угсралт — суурь', 'unit': 'тонн', 'qty': rt, 'unit_price': rwp, 'total': round(rt*rwp)},
    ]

    # ============================================================
    # БАРИЛГЫН ТӨРЛИЙН ТОДОРХОЙЛОЛТ
    # ============================================================
    bt = building_type.lower()
    is_high_rise = floors >= 5 or 'өндөр давхар' in bt or 'олон айлын' in bt
    is_mid_rise = 3 <= floors <= 4
    is_low_rise = floors <= 2 or 'амины' in bt

    # Олон давхарт барилгад хана материалыг автоматаар солих
    if is_high_rise and 'металл' not in wall_mat.lower():
        # 5+ давхар бол бетон каркас систем
        effective_wall_mat = 'бетон каркас'
    elif is_mid_rise and 'мак блок' in wall_mat.lower():
        effective_wall_mat = 'мак блок'
    else:
        effective_wall_mat = wall_mat.lower()

    # ============================================================
    # 2. ГАДНА ХАНА
    # ============================================================
    if 'бетон каркас' in effective_wall_mat:
        # Бетон каркас + дотор блок хаалт
        # Гадна хана: бетон хавтан (prefab) эсвэл монолит
        wall_panel_price = get_price('mat_cement', 'М300') or 285000
        wall_panel_volume = round(net_wall_area * 0.18, 1)
        wall_panel_rebar = round(net_wall_area * 0.02, 2)
        # Гадна хананы дүүргэлт: мак блок (20см)
        infill_block_qty = round(net_wall_area * 12)
        infill_block_price = get_price('mat_brick', 'Мак блок (20') or 7000
        wall_work_price = get_price('labor_general', 'Гадна бетон хананы') or 130000
        materials += [
            {'name': 'Бетон хавтан М300 — гадна хана', 'unit': 'м³',
             'qty': wall_panel_volume, 'unit_price': wall_panel_price,
             'total': round(wall_panel_volume * wall_panel_price)},
            {'name': 'Арматур — гадна хана', 'unit': 'тонн',
             'qty': wall_panel_rebar, 'unit_price': rp,
             'total': round(wall_panel_rebar * rp)},
            {'name': 'Мак блок (20см) — ханын дүүргэлт', 'unit': 'ш',
             'qty': infill_block_qty, 'unit_price': infill_block_price,
             'total': infill_block_qty * infill_block_price},
        ]
        labor.append({'name': 'Гадна хана угсралт', 'unit': 'м²',
                      'qty': net_wall_area, 'unit_price': wall_work_price,
                      'total': round(net_wall_area * wall_work_price)})
    elif 'тоосго' in effective_wall_mat:
        bq = round(net_wall_area * 51)
        bp = get_price('mat_brick', 'Улаан тоосго') or 515
        wp = get_price('labor_general', 'Тоосгон хана өрөх /25') or 25000
        materials.append({'name': 'Улаан тоосго — гадна хана', 'unit': 'ш', 'qty': bq, 'unit_price': bp, 'total': bq*bp})
        labor.append({'name': 'Тоосгон хана өрөх', 'unit': 'м²', 'qty': net_wall_area, 'unit_price': wp, 'total': round(net_wall_area*wp)})
    elif 'бетон' in effective_wall_mat and 'каркас' not in effective_wall_mat:
        wv = round(net_wall_area * 0.2, 1)
        cp2 = get_price('mat_cement', 'М300') or 285000
        wp = get_price('labor_general', 'Гадна бетон хананы') or 130000
        materials.append({'name': 'Бетон зуурмаг М300 — хана', 'unit': 'м³', 'qty': wv, 'unit_price': cp2, 'total': round(wv*cp2)})
        labor.append({'name': 'Бетон хана цутгалт', 'unit': 'м³', 'qty': wv, 'unit_price': wp, 'total': round(wv*wp)})

    # ============================================================
    # 3. ДУЛААЛГА
    # ============================================================
    if insulation and 'байхгүй' not in insulation.lower():
        if 'шилэн хөвөн' in insulation.lower():
            ip = get_price('mat_insulation', 'Шилэн хөвөн (100') or 18500
        elif 'хөөсөнцөр' in insulation.lower():
            ip = get_price('mat_insulation', 'Хөөсөнцөр') or 8000
        elif 'базальт' in insulation.lower():
            ip = get_price('mat_insulation', 'Базальт') or 15000
        elif 'xps' in insulation.lower():
            ip = get_price('mat_insulation', 'XPS') or 21000
        else:
            ip = 15000
        iwp = get_price('labor_special', 'Дулаалга хийх') or 11500
        materials.append({'name': f'Дулаалга ({insulation})', 'unit': 'м²', 'qty': net_wall_area, 'unit_price': ip, 'total': round(net_wall_area*ip)})
        labor.append({'name': 'Дулаалга хийх', 'unit': 'м²', 'qty': net_wall_area, 'unit_price': iwp, 'total': round(net_wall_area*iwp)})

    # ============================================================
    # 4. ГАДНА ФАСАД
    # ============================================================
    plaster_work = get_price('labor_special', 'Шавардлага') or 23500
    if 'тоосго' in facade.lower() or 'клинкер' in facade.lower():
        fap = get_price('mat_brick', 'Өнгөлгөөний тоосго') or 3000
        faq = round(net_wall_area * 51)
        materials.append({'name': 'Өнгөлгөөний тоосго — фасад', 'unit': 'ш', 'qty': faq, 'unit_price': fap, 'total': faq*fap})
        labor.append({'name': 'Өнгөлгөөний тоосго өрөх', 'unit': 'м²', 'qty': net_wall_area, 'unit_price': 35000, 'total': round(net_wall_area*35000)})
    else:
        cement_qty = round(net_wall_area * 0.12)
        paint_qty = round(net_wall_area / 8)
        materials += [
            {'name': 'Цемент — фасадын шавардлага', 'unit': 'уут', 'qty': cement_qty, 'unit_price': 41500, 'total': cement_qty*41500},
            {'name': 'Гадна фасадын будаг', 'unit': 'сав', 'qty': paint_qty, 'unit_price': 100000, 'total': paint_qty*100000},
        ]
        labor.append({'name': 'Гадна ханын шавардлага', 'unit': 'м²', 'qty': net_wall_area, 'unit_price': plaster_work, 'total': round(net_wall_area*plaster_work)})

    # ============================================================
    # 5. ХУЧИЛТ
    # ============================================================
    sa = floor_area * (floors-1) if floors > 1 else floor_area
    sv = round(sa * 0.2, 1)
    srt = round(sa * 25 / 1000, 2)
    materials += [
        {'name': 'Бетон зуурмаг М250 — хучилт', 'unit': 'м³', 'qty': sv, 'unit_price': cp, 'total': round(sv*cp)},
        {'name': 'Арматур — хучилт', 'unit': 'тонн', 'qty': srt, 'unit_price': rp, 'total': round(srt*rp)},
    ]
    labor.append({'name': 'Бетон цутгалт — хучилт', 'unit': 'м³', 'qty': sv, 'unit_price': cwp, 'total': round(sv*cwp)})

    # ============================================================
    # 5б. КОЛОНН, ДАМ НУРУУ — олон давхарт барилгад
    if floors >= 3:
        # Колонн: нэг давхарт 1 колонн = 0.3x0.3x3м = 0.27м³, 80кг арматур
        # Нэг давхарт колонны тоо ойролцоо: floor_area / 25
        column_count = round(floor_area / 25)
        column_concrete = round(column_count * floors * 0.27, 1)
        column_rebar = round(column_count * floors * 0.08, 2)
        beam_concrete = round(floor_area * (floors-1) * 0.05, 1)
        beam_rebar = round(floor_area * (floors-1) * 15 / 1000, 2)
        col_cp = get_price('mat_cement', 'М300') or 285000
        materials += [
            {'name': 'Бетон зуурмаг М300 — колонн', 'unit': 'м³',
             'qty': column_concrete, 'unit_price': col_cp,
             'total': round(column_concrete * col_cp)},
            {'name': 'Арматур — колонн', 'unit': 'тонн',
             'qty': column_rebar, 'unit_price': rp,
             'total': round(column_rebar * rp)},
            {'name': 'Бетон зуурмаг М300 — дам нуруу', 'unit': 'м³',
             'qty': beam_concrete, 'unit_price': col_cp,
             'total': round(beam_concrete * col_cp)},
            {'name': 'Арматур — дам нуруу', 'unit': 'тонн',
             'qty': beam_rebar, 'unit_price': rp,
             'total': round(beam_rebar * rp)},
        ]
        labor += [
            {'name': 'Бетон цутгалт — колонн', 'unit': 'м³',
             'qty': column_concrete, 'unit_price': cwp,
             'total': round(column_concrete * cwp)},
            {'name': 'Арматур угсралт — колонн, дам нуруу', 'unit': 'тонн',
             'qty': column_rebar + beam_rebar, 'unit_price': rwp,
             'total': round((column_rebar + beam_rebar) * rwp)},
        ]

    # 6. ШАТНЫ БҮТЭЦ
    # ============================================================
    if floors >= 2:
        stc = round(floors * 2.5, 1)
        str2 = round(floors * 0.2, 2)
        materials += [
            {'name': 'Бетон зуурмаг М250 — шат', 'unit': 'м³', 'qty': stc, 'unit_price': cp, 'total': round(stc*cp)},
            {'name': 'Арматур — шат', 'unit': 'тонн', 'qty': str2, 'unit_price': rp, 'total': round(str2*rp)},
        ]
        labor.append({'name': 'Шатны бетон цутгалт', 'unit': 'м³', 'qty': stc, 'unit_price': cwp, 'total': round(stc*cwp)})

    # ============================================================
    # 7. ДЭЭВЭР
    # ============================================================
    if 'хавтгай' in roof_type.lower():
        rc = round(roof_area * 0.15, 1)
        rbp = get_price('mat_roof', 'Рубероид') or 18000
        ins_roof_price = get_price('mat_insulation', 'Шилэн хөвөн (100') or 18500
        materials += [
            {'name': 'Бетон — хавтгай дээвэр', 'unit': 'м³', 'qty': rc, 'unit_price': cp, 'total': round(rc*cp)},
            {'name': 'Рубероид — ус тусгаарлалт', 'unit': 'рулон', 'qty': round(roof_area/10), 'unit_price': rbp, 'total': round(roof_area/10*rbp)},
            {'name': 'Дулаалга — дээвэр', 'unit': 'м²', 'qty': round(roof_area,1), 'unit_price': ins_roof_price, 'total': round(roof_area*ins_roof_price)},
        ]
        labor.append({'name': 'Хавтгай дээвэр хийх', 'unit': 'м²', 'qty': round(roof_area,1), 'unit_price': 28000, 'total': round(roof_area*28000)})
    else:
        if 'металл черепица' in roof_type.lower() or 'метал' in roof_type.lower():
            rmp = get_price('mat_roof', 'Металл черепица') or 45000
            rmn = 'Металл черепица'
        else:
            rmp = get_price('mat_roof', 'Профнастил') or 21000
            rmn = 'Профнастил'
        wdp = get_price('mat_wood', 'Тавцан мод') or 5250
        wdq = round(roof_area * 12)
        rwp2 = get_price('labor_special', 'Төмөр дээвэр') or 26500
        ins_roof_price = get_price('mat_insulation', 'Шилэн хөвөн (100') or 18500
        materials += [
            {'name': f'{rmn} — дээвэр', 'unit': 'м²', 'qty': round(roof_area,1), 'unit_price': rmp, 'total': round(roof_area*rmp)},
            {'name': 'Тавцан мод — дээврийн каркас', 'unit': 'м', 'qty': wdq, 'unit_price': wdp, 'total': wdq*wdp},
            {'name': 'Дулаалга — дээврийн доторлогоо', 'unit': 'м²', 'qty': round(roof_area,1), 'unit_price': ins_roof_price, 'total': round(roof_area*ins_roof_price)},
        ]
        labor.append({'name': 'Дээвэр угсралт', 'unit': 'м²', 'qty': round(roof_area,1), 'unit_price': rwp2, 'total': round(roof_area*rwp2)})

    # ============================================================
    # 8. ДОТОР ЗАСАЛ — шал
    # ============================================================
    wa = round(total_area * 0.25, 1)
    da = round(total_area * 0.75, 1)
    tp = get_price('mat_interior', 'Керамик плита') or 57000
    tw = get_price('labor_general', 'Плита наалт') or 40000
    sw = get_price('labor_general', 'Шалны тэгшилгээ') or 16500

    # Ванн өрөөний ханын плита
    wet_wall_area = round(wa * 1.5)  # ванн өрөөний хана
    materials += [
        {'name': 'Керамик плита — шал (ванн, гал тогоо)', 'unit': 'м²', 'qty': wa, 'unit_price': tp, 'total': round(wa*tp)},
        {'name': 'Керамик плита — ханын (ванн, гал тогоо)', 'unit': 'м²', 'qty': wet_wall_area, 'unit_price': tp, 'total': round(wet_wall_area*tp)},
    ]
    labor += [
        {'name': 'Плита тавих — шал', 'unit': 'м²', 'qty': wa, 'unit_price': tw, 'total': round(wa*tw)},
        {'name': 'Плита наах — хана', 'unit': 'м²', 'qty': wet_wall_area, 'unit_price': get_price('labor_special','Плита наах (хана)') or 29000, 'total': round(wet_wall_area*29000)},
    ]

    floor_mat = data.get('floor_material', 'Ламинат')
    if 'паркет' in floor_mat.lower():
        fp2 = get_price('mat_interior', 'Паркет') or 140000
        materials.append({'name': 'Паркет — үндсэн өрөө', 'unit': 'м²', 'qty': da, 'unit_price': fp2, 'total': round(da*fp2)})
        labor.append({'name': 'Паркет тавих', 'unit': 'м²', 'qty': da, 'unit_price': 26000, 'total': round(da*26000)})
    else:
        lp = get_price('mat_interior', 'Ламинат шал') or 42000
        lw = get_price('labor_general', 'Ламинат шал тавих') or 19000
        materials.append({'name': 'Ламинат шал — үндсэн өрөө', 'unit': 'м²', 'qty': da, 'unit_price': lp, 'total': round(da*lp)})
        labor.append({'name': 'Ламинат шал тавих', 'unit': 'м²', 'qty': da, 'unit_price': lw, 'total': round(da*lw)})

    labor.append({'name': 'Шалны стяжка', 'unit': 'м²', 'qty': total_area, 'unit_price': sw, 'total': round(total_area*sw)})

    # ============================================================
    # 9. ДОТОР ХАНЫН ЗАСАЛ + ТААЗ
    # ============================================================
    zp = get_price('mat_interior', 'Өнгөлгөөний цагаан замазка') or 12000
    zq = round(total_inner_surface * 1.2)
    pip2 = get_price('mat_interior', 'Дотор будаг') or 7500
    piq = round(total_inner_surface * 0.3)
    materials += [
        {'name': 'Цагаан замазка — дотор хана, тааз', 'unit': 'кг', 'qty': zq, 'unit_price': zp, 'total': zq*zp},
        {'name': 'Дотор эмульс будаг', 'unit': 'кг', 'qty': piq, 'unit_price': pip2, 'total': piq*pip2},
    ]
    zwp = get_price('labor_special', 'Цагаан замаска') or 14000
    pwp = get_price('labor_special', 'Эмульс хийх') or 6750
    labor += [
        {'name': 'Замазка хийх — дотор хана, тааз', 'unit': 'м²', 'qty': total_inner_surface, 'unit_price': zwp, 'total': total_inner_surface*zwp},
        {'name': 'Эмульс будаг — дотор хана, тааз', 'unit': 'м²', 'qty': total_inner_surface, 'unit_price': pwp, 'total': total_inner_surface*pwp},
    ]

    # ============================================================
    # 10. ТААЗ — ГИПРОК
    # ============================================================
    gypsum_price = get_price('mat_wood', 'Гипсэн хавтан KNAUF 12') or 29000
    gypsum_profile = 3500  # металл профиль м²-д
    gypsum_qty = round(total_area * 1.1)  # 10% нэмэлт
    gypsum_work = get_price('labor_general', 'Ханын каркас угсралт') or 21500
    materials += [
        {'name': 'Гипрок хавтан — тааз', 'unit': 'ш', 'qty': round(total_area/3), 'unit_price': gypsum_price, 'total': round(total_area/3)*gypsum_price},
        {'name': 'Металл профиль — таазны каркас', 'unit': 'м²', 'qty': total_area, 'unit_price': gypsum_profile, 'total': round(total_area*gypsum_profile)},
    ]
    labor.append({'name': 'Гипрок тааз хийх', 'unit': 'м²', 'qty': total_area, 'unit_price': gypsum_work, 'total': total_area*gypsum_work})

    # ============================================================
    # 11. ДОТОР ХУВААЛТ
    # ============================================================
    ibp = get_price('mat_brick', 'Мак блок (20') or 7000
    iwp3 = get_price('labor_general', 'Блокон хана өрөх /25') or 25000
    # Олон давхарт барилгад дотор хуваалт харьцангуй бага
    if is_high_rise:
        inner_wall_density = 10  # блок/м²
    else:
        inner_wall_density = 16
    ibq = round(inner_wall_area * inner_wall_density)
    materials.append({'name': 'Мак блок (20см) — дотор хуваалт', 'unit': 'ш', 'qty': ibq, 'unit_price': ibp, 'total': ibq*ibp})
    labor.append({'name': 'Дотор хуваалт өрөх', 'unit': 'м²', 'qty': round(inner_wall_area,1), 'unit_price': iwp3, 'total': round(inner_wall_area*iwp3)})

    # ============================================================
    # 12. ЦОНХ, ХААЛГА
    # ============================================================
    try:
        wna = int(str(data.get('windows','5')).split('-')[0])
    except:
        wna = 5
    try:
        dna = int(str(data.get('doors','4')).split('-')[0])
    except:
        dna = 4
    upf = int(str(data.get('units_per_floor',1)).replace('+',''))
    tu = max(1, upf * floors)
    tw2 = tu * wna
    td = tu * dna
    wnp = get_price('mat_window', 'PVC цонх (1.2') or 450000
    dnp = get_price('mat_window', 'Дотор хаалга') or 420000
    odp = get_price('mat_window', 'Гадна хаалга (металл)') or 1150000
    wip = get_price('labor_special', 'Хаалга угсрах (дотор') or 65000
    materials += [
        {'name': 'PVC цонх (1.2x1.2м)', 'unit': 'ш', 'qty': tw2, 'unit_price': wnp, 'total': tw2*wnp},
        {'name': 'Дотор хаалга', 'unit': 'ш', 'qty': td, 'unit_price': dnp, 'total': td*dnp},
        {'name': 'Гадна хаалга (металл)', 'unit': 'ш', 'qty': tu, 'unit_price': odp, 'total': tu*odp},
    ]
    labor.append({'name': 'Цонх, хаалга угсралт', 'unit': 'ш', 'qty': tw2+td, 'unit_price': wip, 'total': (tw2+td)*wip})

    # ============================================================
    # 13. ЦАХИЛГААНЫ СИСТЕМ
    # ============================================================
    cbp = get_price('mat_electrical', 'Кабель ВВГ') or 3600
    cbq = round(total_area * 5)
    swp2 = get_price('mat_electrical', 'Унтраалга 1') or 6100
    sop = get_price('mat_electrical', 'Розетка 1') or 6600
    swq = round(tu * 10)
    soq = round(tu * 15)
    ewp = get_price('labor_general', 'Цахилгаанчин') or 125000
    edp = round(total_area / 6)  # 1 цахилгаанчин 10м²/өдөр
    materials += [
        {'name': 'Цахилгааны кабель ВВГ', 'unit': 'м', 'qty': cbq, 'unit_price': cbp, 'total': cbq*cbp},
        {'name': 'Унтраалга', 'unit': 'ш', 'qty': swq, 'unit_price': swp2, 'total': swq*swp2},
        {'name': 'Розетка', 'unit': 'ш', 'qty': soq, 'unit_price': sop, 'total': soq*sop},
    ]
    labor.append({'name': 'Цахилгааны ажил', 'unit': 'өдөр', 'qty': edp, 'unit_price': ewp, 'total': edp*ewp})

    # ============================================================
    # 14. ИНЖЕНЕРИЙН СИСТЕМ
    # ============================================================
    htp = get_price('mat_plumbing', 'Халаалтын систем') or 6750000
    wtp = get_price('mat_plumbing', 'Цэвэр усны систем') or 1025000
    sgp = get_price('mat_plumbing', 'Бохир усны систем') or 200000
    sap = get_price('mat_plumbing', 'Ариун цэврийн өрөөний') or 1850000
    materials += [
        {'name': 'Халаалтын систем', 'unit': 'багц', 'qty': tu, 'unit_price': htp, 'total': tu*htp},
        {'name': 'Цэвэр усны систем', 'unit': 'багц', 'qty': tu, 'unit_price': wtp, 'total': tu*wtp},
        {'name': 'Бохир усны систем', 'unit': 'багц', 'qty': tu, 'unit_price': sgp, 'total': tu*sgp},
        {'name': 'Ариун цэврийн тоноглол', 'unit': 'багц', 'qty': tu, 'unit_price': sap, 'total': tu*sap},
    ]

    # ============================================================
    # 15. ЕРӨНХИЙ БАРИЛГЫН АЖИЛЧИД
    # ============================================================
    # Барилгачид — нийт талбайгаар тооцоолно
    # 1 барилгачин өдөрт дунджаар 1.5м² дуусгадаг (бетон, хана, засал хамт)
    # Ажилчид — том барилгад хэт их болохоос хамгаалах
    # 1 барилгачин 1 өдөрт 1.5м² — гэхдээ олон ажилчин зэрэг ажилладаг
    # Тиймээс нийт хүн-өдрийг 1.5-2.0-оор тооцно
    # Барилгачид — зэрэг ажилладаг тул хүн-өдөр хязгаарлах
    # Жижиг барилга (≤200м²): 1.5өдөр/м²
    # Том барилга: багасдаг — зэрэг ажиллах коэффициент
    if total_area <= 200:
        worker_coef = 1.5
    elif total_area <= 500:
        worker_coef = 1.8
    elif total_area <= 1500:
        worker_coef = 2.0
    elif total_area <= 3000:
        worker_coef = 1.8
    else:
        worker_coef = 1.5
    general_worker_days = round(total_area * worker_coef)
    general_worker_price = get_price('labor_general', 'Барилгачин (ерөнхий)') or 75000
    labor.append({
        'name': 'Барилгачид (ерөнхий ажил)',
        'unit': 'өдөр', 'qty': general_worker_days,
        'unit_price': general_worker_price,
        'total': general_worker_days * general_worker_price
    })

    # Туслах ажилтан
    if total_area <= 200:
        helper_coef = 0.6
    elif total_area <= 1500:
        helper_coef = 0.7
    else:
        helper_coef = 0.6
    helper_days = round(total_area * helper_coef)
    helper_price = get_price('labor_general', 'Туслах ажилтан') or 125000
    labor.append({
        'name': 'Туслах ажилтан',
        'unit': 'өдөр', 'qty': helper_days,
        'unit_price': helper_price,
        'total': helper_days * helper_price
    })

    # Мужаан (хэв хашмал, дээвэр)
    if total_area <= 200:
        carp_coef = 0.3
    elif total_area <= 1500:
        carp_coef = 0.35
    else:
        carp_coef = 0.3
    carpenter_days = round(total_area * carp_coef)
    carpenter_price = get_price('labor_general', 'Мужаан') or 100000
    labor.append({
        'name': 'Мужаан',
        'unit': 'өдөр', 'qty': carpenter_days,
        'unit_price': carpenter_price,
        'total': carpenter_days * carpenter_price
    })

    # Сантехникч
    plumber_days = round(total_area / 5)
    plumber_price = get_price('labor_general', 'Сантехникч') or 125000
    labor.append({
        'name': 'Сантехникч',
        'unit': 'өдөр', 'qty': plumber_days,
        'unit_price': plumber_price,
        'total': plumber_days * plumber_price
    })

    # ============================================================
    # 16. МАШИН ТЕХНИК
    # ============================================================
    scaffold_price = get_price('machine_other', 'Скафольд') or 4000
    duration_prelim = max(6, round(total_area / 60))
    scaffold_area = net_wall_area
    crane_price = get_price('machine_crane', 'Кран (25') or 200000
    crane_hours = min(200, round(total_area / 20))
    excavator_price = get_price('machine_excavator', 'Экскаватор') or 160000
    excavator_hours = min(100, round(fv * 0.3))
    concrete_pump_price = get_price('machine_concrete', 'Бетон насос') or 200000
    concrete_pump_hours = min(80, round((fv + sv) / 15))

    transport += [
        {'name': 'Скафольд түрээс', 'unit': 'м²/сар', 'qty': round(scaffold_area), 'unit_price': scaffold_price * 3, 'total': round(scaffold_area * scaffold_price * 3)},
        {'name': 'Кран үйлчилгээ', 'unit': 'цаг', 'qty': crane_hours, 'unit_price': crane_price, 'total': crane_hours * crane_price},
        {'name': 'Экскаватор', 'unit': 'цаг', 'qty': excavator_hours, 'unit_price': excavator_price, 'total': excavator_hours * excavator_price},
        {'name': 'Бетон насос', 'unit': 'цаг', 'qty': concrete_pump_hours, 'unit_price': concrete_pump_price, 'total': concrete_pump_hours * concrete_pump_price},
    ]

    trp = get_price('transport_material', 'Материал тээвэр') or 90000
    wsp = get_price('transport_material', 'Хог зайлуулах') or 80000
    trt = max(10, round(total_area / 15))
    transport += [
        {'name': 'Материал тээвэр', 'unit': 'удаа', 'qty': trt, 'unit_price': trp, 'total': trt*trp},
        {'name': 'Хог зайлуулах', 'unit': 'удаа', 'qty': round(trt/2), 'unit_price': wsp, 'total': round(trt/2)*wsp},
    ]

    # ============================================================
    # 17. БУСАД
    # ============================================================
    # Хугацаа — барилгын төрөл, талбайгаар
    if total_area <= 150:
        duration = 6
    elif total_area <= 300:
        duration = 9
    elif total_area <= 600:
        duration = 12
    elif total_area <= 1500:
        duration = 18
    elif total_area <= 3000:
        duration = 24
    elif total_area <= 6000:
        duration = 30
    else:
        duration = 36
    dsp = get_price('other_design', 'Архитектурын') or 25000
    pmp = get_price('other_permit', 'Барилгын зөвшөөрөл') or 1250000
    inp2 = get_price('other_insurance', 'Барилгын даатгал') or 1250000
    vat_rate = 0.10  # НӨАТ 10%

    other += [
        {'name': 'Архитектур, инженерийн зураг төсөл', 'unit': 'багц', 'qty': 1, 'unit_price': min(50000000, round(total_area * 10000)), 'total': min(50000000, round(total_area * 10000))},
        {'name': 'Барилгын зөвшөөрөл', 'unit': 'удаа', 'qty': 1, 'unit_price': pmp, 'total': pmp},
        {'name': 'Инженер хяналт', 'unit': 'сар', 'qty': duration, 'unit_price': 1750000, 'total': duration * 1750000},
        {'name': 'Барилгын даатгал', 'unit': 'жил', 'qty': max(1,round(duration/12)), 'unit_price': inp2, 'total': max(1,round(duration/12))*inp2},
        {'name': 'Туршилт, шинжилгээ', 'unit': 'удаа', 'qty': 1, 'unit_price': 350000, 'total': 350000},
    ]

    # НИЙТ ТООЦОО — эхлээд sub_mat, sub_lab тодорхойлно
    sub_mat = round(sum(i['total'] for i in materials) * quality_coef)
    sub_lab = round(sum(i['total'] for i in labor) * quality_coef)

    # Санамсаргүй зардал — материал+ажлын 3%
    other.append({'name': 'Санамсаргүй зардал (3%)', 'unit': 'хувь', 'qty': 1, 'unit_price': round((sub_mat+sub_lab)*0.03), 'total': round((sub_mat+sub_lab)*0.03)})
    sub_tra = sum(i['total'] for i in transport)
    sub_oth = sum(i['total'] for i in other)
    vat_amount = round((sub_mat + sub_lab) * 0.10)
    other.append({'name': 'НӨАТ (10%)', 'unit': 'хувь', 'qty': 1, 'unit_price': vat_amount, 'total': vat_amount})
    # Санамсаргүй зардал — материал+ажлын 3%
    misc_amount = round((sub_mat + sub_lab) * 0.03)
    # other дотор санамсаргүй зардлыг шинэчлэх
    for item in other:
        if 'Санамсаргүй' in item['name']:
            item['unit_price'] = misc_amount
            item['total'] = misc_amount
            break

    mt = sub_mat
    lt = sub_lab
    tt = sub_tra
    ot = sum(i['total'] for i in other)
    gt = mt + lt + tt + ot
    ppm2 = round(gt / total_area) if total_area > 0 else 0

    return {
        'building_info': {
            'type': data.get('building_type',''),
            'area': f'{total_area:.0f} м²',
            'floors': str(floors),
            'location': data.get('location','Улаанбаатар'),
            'quality': data.get('quality','дунд'),
        },
        'materials': materials,
        'labor': labor,
        'transport': transport,
        'other': other,
        'summary': {
            'materials_total': mt,
            'labor_total': lt,
            'transport_total': tt,
            'other_total': ot,
            'grand_total': gt,
            'price_per_m2': ppm2,
            'duration_months': duration,
        },
        'notes': '⚠️ Энэ тооцоо ойролцоо үнэлгээ бөгөөд мэргэжлийн инженерийн тооцоог орлохгүй. Бодит зардал газрын байршил, ханган нийлүүлэгч, нарийн зураг төслөөс хамаарч өөрчлөгдөж болно. Гэрээ байгуулахаасаа өмнө мэргэжлийн байгууллагаар нарийвчилсан тооцоо гаргуулна уу.'
    }

# Туршилт
test_data = {
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

r = calculate_budget(test_data)
s = r['summary']

print(f"\n{'='*60}")
print(f"Барилга: {r['building_info']['type']}")
print(f"Талбай:  {r['building_info']['area']}")
print(f"{'='*60}")
for sec, items in [('МАТЕРИАЛ', r['materials']), ('АЖИЛ', r['labor']),
                   ('ТЭЭВЭР/МАШИН', r['transport']), ('БУСАД', r['other'])]:
    print(f"\n--- {sec} ---")
    for i in items:
        print(f"  {i['name']:48} {i['qty']:>8} {i['unit']:8} x {i['unit_price']:>10,}₮ = {i['total']:>15,}₮")
print(f"\n{'='*60}")
print(f"  Материал:   {s['materials_total']:>15,}₮  ({s['materials_total']*100//s['grand_total']}%)")
print(f"  Ажил:       {s['labor_total']:>15,}₮  ({s['labor_total']*100//s['grand_total']}%)")
print(f"  Тээвэр:     {s['transport_total']:>15,}₮  ({s['transport_total']*100//s['grand_total']}%)")
print(f"  Бусад:      {s['other_total']:>15,}₮  ({s['other_total']*100//s['grand_total']}%)")
print(f"{'='*60}")
print(f"  НИЙТ ТӨСӨВ: {s['grand_total']:>15,}₮")
print(f"  1м² үнэ:    {s['price_per_m2']:>15,}₮")
print(f"  Хугацаа:    {s['duration_months']} сар")
print(f"{'='*60}")
print(f"\nЗорилт: 2,000,000-3,500,000₮/м²")