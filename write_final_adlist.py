html = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Зарууд — БНБ</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f1f5f9;}
    a{text-decoration:none;color:inherit;}
    .nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;gap:12px;}
    .logo-box{width:32px;height:32px;background:#f59e0b;border-radius:7px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
    .logo-box svg{width:18px;height:18px;fill:none;stroke:#fff;stroke-width:2;}
    .logo-t{color:#fff;font-size:13px;font-weight:700;margin-left:8px;}
    .nav-r{margin-left:auto;display:flex;gap:6px;}
    .nb{padding:5px 12px;border-radius:6px;font-size:12px;font-weight:500;border:none;cursor:pointer;}
    .nb-o{background:transparent;color:#cbd5e1;border:1px solid #2d4f63;}
    .nb-y{background:#f59e0b;color:#1e3a4a;}
    .hero{background:#1e3a4a;padding:16px 20px;}
    .hero-t{color:#fff;font-size:16px;font-weight:700;margin-bottom:10px;}
    .search-wrap{display:flex;gap:8px;flex-wrap:wrap;max-width:700px;}
    .search-inp{flex:2;min-width:160px;padding:8px 14px;border:none;outline:none;font-size:13px;border-radius:8px;}
    .search-sel{flex:1;min-width:160px;padding:8px 10px;border:none;outline:none;font-size:12px;color:#1e293b;background:#fff;border-radius:8px;}
    .search-btn{padding:8px 18px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;}
    .filter-bar{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:8px 20px;display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
    .filter-tag{display:inline-flex;align-items:center;gap:4px;background:#fef3c7;color:#854d0e;font-size:11px;padding:3px 10px;border-radius:20px;}
    .cats{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:0 20px;display:flex;overflow-x:auto;}
    .cat{display:flex;align-items:center;gap:5px;padding:10px 14px;font-size:12px;color:#64748b;border-bottom:2px solid transparent;white-space:nowrap;}
    .cat:hover{color:#1e3a4a;}
    .cat.on{color:#1e3a4a;border-bottom-color:#f59e0b;font-weight:600;}
    .page-wrap{max-width:1100px;margin:16px auto;padding:0 20px;display:grid;grid-template-columns:220px 1fr;gap:16px;}
    .sidebar{display:flex;flex-direction:column;gap:8px;}
    .sb-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;overflow:hidden;}
    .sb-hd{padding:10px 14px;border-bottom:0.5px solid #e2e8f0;font-size:13px;font-weight:600;color:#1e293b;}
    .sb-body{padding:8px;}
    .subcat-link{display:flex;align-items:center;padding:7px 8px;border-radius:6px;font-size:12px;color:#374151;gap:6px;}
    .subcat-link:hover{background:#f8fafc;}
    .subcat-link.on{background:#fef3c7;color:#854d0e;font-weight:500;}
    .acc-item{margin-bottom:2px;}
    .acc-hd{display:flex;align-items:center;justify-content:space-between;padding:7px 8px;border-radius:6px;font-size:12px;color:#374151;cursor:pointer;font-weight:500;user-select:none;}
    .acc-hd:hover{background:#f8fafc;}
    .acc-hd.on{color:#854d0e;background:#fef9ec;}
    .acc-arr{font-size:10px;color:#94a3b8;flex-shrink:0;transition:transform 0.2s;}
    .acc-body{display:none;flex-direction:column;padding-left:8px;margin-top:2px;gap:1px;}
    .acc-body.show{display:flex;}
    .item-link{font-size:11px;color:#64748b;padding:4px 8px;border-radius:5px;display:block;}
    .item-link:hover{background:#f1f5f9;color:#1e293b;}
    .item-link.on{color:#854d0e;background:#fef9ec;font-weight:500;}
    .main-content{min-width:0;}
    .top-bar{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;flex-wrap:wrap;gap:8px;}
    .top-t{font-size:14px;font-weight:600;color:#1e293b;}
    .ads-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;}
    .ad-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;overflow:hidden;display:block;}
    .ad-card:hover{border-color:#f59e0b;}
    .ad-img{height:130px;background:#f8fafc;display:flex;align-items:center;justify-content:center;font-size:40px;border-bottom:0.5px solid #e2e8f0;overflow:hidden;}
    .ad-img img{width:100%;height:100%;object-fit:cover;}
    .ad-body{padding:10px 12px;}
    .ad-cat{display:inline-block;background:#fef3c7;color:#854f0b;font-size:10px;padding:1px 7px;border-radius:20px;margin-bottom:5px;}
    .ad-t{font-size:13px;font-weight:600;color:#1e293b;line-height:1.35;margin-bottom:5px;}
    .ad-p{font-size:13px;font-weight:700;color:#f59e0b;margin-bottom:4px;}
    .ad-m{font-size:11px;color:#94a3b8;display:flex;gap:8px;}
    .empty{text-align:center;padding:40px;color:#94a3b8;background:#fff;border-radius:10px;border:0.5px dashed #e2e8f0;grid-column:1/-1;}
    @media(max-width:900px){.page-wrap{grid-template-columns:1fr;}.sidebar{display:none;}.ads-grid{grid-template-columns:1fr 1fr;}}
    @media(max-width:480px){.ads-grid{grid-template-columns:1fr;}.search-wrap{flex-direction:column;}}
  </style>
</head>
<body>

<nav class="nav">
  <a href="/public/" style="display:flex;align-items:center;gap:8px;">
    <div class="logo-box"><svg viewBox="0 0 24 24"><path d="M3 21h18M3 7l9-4 9 4M4 7v14M20 7v14M9 21v-6h6v6"/></svg></div>
    <span class="logo-t">БНБ — Барилгын нэгдсэн бааз</span>
  </a>
  <div class="nav-r">
    <a href="/public/" class="nb nb-o">Нүүр</a>
    <a href="/ads/create/" class="nb nb-y">+ Зар оруулах</a>
  </div>
</nav>

<div class="hero">
  <div class="hero-t">📢 Зарууд</div>
  <form method="get" action="/ads/" class="search-wrap">
    <input class="search-inp" name="q" placeholder="Зар хайх..." value="{{ q }}">
    <select class="search-sel" name="cat" onchange="this.form.submit()">
      <option value="">📂 Бүх ангилал</option>
      <option value="material" {% if category == "material" %}selected{% endif %}>🧱 Материал</option>
      <option value="equipment" {% if category == "equipment" %}selected{% endif %}>🔩 Тоног төхөөрөмж</option>
      <option value="rental" {% if category == "rental" %}selected{% endif %}>🔑 Түрээс</option>
      <option value="realestate" {% if category == "realestate" %}selected{% endif %}>🏠 Үл хөдлөх хөрөнгө</option>
      <option value="service" {% if category == "service" %}selected{% endif %}>🏗 Барилгын үйлчилгээ</option>
      <option value="design" {% if category == "design" %}selected{% endif %}>📐 Зураг төсөв, дизайн</option>
      <option value="worker" {% if category == "worker" %}selected{% endif %}>👷 Ажилтан, ажлын зар</option>
      <option value="tender" {% if category == "tender" %}selected{% endif %}>📋 Тендер, төсөл</option>
      <option value="company" {% if category == "company" %}selected{% endif %}>🏢 Компаниуд</option>
      <option value="other" {% if category == "other" %}selected{% endif %}>📦 Бусад</option>
    </select>
    <button type="submit" class="search-btn">🔍 Хайх</button>
  </form>
</div>

{% if category or subcat or q %}
<div class="filter-bar">
  <span style="font-size:12px;color:#64748b;">Шүүлтүүр:</span>
  {% if category %}<span class="filter-tag">{{ category }}</span>{% endif %}
  {% if subcat %}<span class="filter-tag">{{ subcat_label }}</span>{% endif %}
  {% if q %}<span class="filter-tag">🔍 "{{ q }}"</span>{% endif %}
  <a href="/ads/" style="font-size:12px;color:#e53e3e;">✕ Цэвэрлэх</a>
</div>
{% endif %}

<div class="cats">
  <a href="/ads/" class="cat {% if not category %}on{% endif %}">🏠 Бүгд</a>
  <a href="/ads/?cat=material" class="cat {% if category == "material" %}on{% endif %}">🧱 Материал</a>
  <a href="/ads/?cat=equipment" class="cat {% if category == "equipment" %}on{% endif %}">🔩 Тоног</a>
  <a href="/ads/?cat=rental" class="cat {% if category == "rental" %}on{% endif %}">🔑 Түрээс</a>
  <a href="/ads/?cat=realestate" class="cat {% if category == "realestate" %}on{% endif %}">🏠 Үл хөдлөх</a>
  <a href="/ads/?cat=service" class="cat {% if category == "service" %}on{% endif %}">🏗 Үйлчилгээ</a>
  <a href="/ads/?cat=design" class="cat {% if category == "design" %}on{% endif %}">📐 Зураг</a>
  <a href="/ads/?cat=worker" class="cat {% if category == "worker" %}on{% endif %}">👷 Ажилтан</a>
  <a href="/ads/?cat=tender" class="cat {% if category == "tender" %}on{% endif %}">📋 Тендер</a>
  <a href="/ads/?cat=company" class="cat {% if category == "company" %}on{% endif %}">🏢 Компани</a>
  <a href="/ads/?cat=other" class="cat {% if category == "other" %}on{% endif %}">📦 Бусад</a>
</div>

<div class="page-wrap">
  <div class="sidebar">
    {% if category == "material" %}
    <div class="sb-card">
      <div class="sb-hd">🧱 Материалын ангилал</div>
      <div class="sb-body">
        <a href="/ads/?cat=material" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "foundation" %}on{% endif %}" onclick="toggleAcc(this)"><span>🏗 Барилгын үндсэн хийц</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=foundation" class="item-link {% if subcat == "foundation" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=foundation&item=rebar" class="item-link {% if item == "rebar" %}on{% endif %}">Арматур төмөр</a>
            <a href="/ads/?cat=material&subcat=foundation&item=metal_structure" class="item-link {% if item == "metal_structure" %}on{% endif %}">Металь хийц</a>
            <a href="/ads/?cat=material&subcat=foundation&item=concrete" class="item-link {% if item == "concrete" %}on{% endif %}">Бетон зуурмаг</a>
            <a href="/ads/?cat=material&subcat=foundation&item=insulation" class="item-link {% if item == "insulation" %}on{% endif %}">Дулаан дуу тусгаарлах</a>
            <a href="/ads/?cat=material&subcat=foundation&item=roof_material" class="item-link {% if item == "roof_material" %}on{% endif %}">Дээврийн материал</a>
            <a href="/ads/?cat=material&subcat=foundation&item=formwork" class="item-link {% if item == "formwork" %}on{% endif %}">Хэв хашмал</a>
            <a href="/ads/?cat=material&subcat=foundation&item=brick_block" class="item-link {% if item == "brick_block" %}on{% endif %}">Тоосго блок</a>
            <a href="/ads/?cat=material&subcat=foundation&item=wood" class="item-link {% if item == "wood" %}on{% endif %}">Модон материал</a>
            <a href="/ads/?cat=material&subcat=foundation&item=door_window" class="item-link {% if item == "door_window" %}on{% endif %}">Цонх хаалга</a>
            <a href="/ads/?cat=material&subcat=foundation&item=glass" class="item-link {% if item == "glass" %}on{% endif %}">Шилэн хийц</a>
            <a href="/ads/?cat=material&subcat=foundation&item=cement_lime" class="item-link {% if item == "cement_lime" %}on{% endif %}">Цемент шохой</a>
            <a href="/ads/?cat=material&subcat=foundation&item=sand_gravel" class="item-link {% if item == "sand_gravel" %}on{% endif %}">Элс хайрга дайрга</a>
            <a href="/ads/?cat=material&subcat=foundation&item=facade" class="item-link {% if item == "facade" %}on{% endif %}">Гадна фасад</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "interior" %}on{% endif %}" onclick="toggleAcc(this)"><span>🎨 Засал чимэглэл</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=interior" class="item-link {% if subcat == "interior" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=interior&item=paint" class="item-link {% if item == "paint" %}on{% endif %}">Будаг эмульс</a>
            <a href="/ads/?cat=material&subcat=interior&item=dry_mix" class="item-link {% if item == "dry_mix" %}on{% endif %}">Хуурай хольц</a>
            <a href="/ads/?cat=material&subcat=interior&item=wallpaper" class="item-link {% if item == "wallpaper" %}on{% endif %}">Обой хуулга</a>
            <a href="/ads/?cat=material&subcat=interior&item=parquet" class="item-link {% if item == "parquet" %}on{% endif %}">Паркет ламинат</a>
            <a href="/ads/?cat=material&subcat=interior&item=tile_stone" class="item-link {% if item == "tile_stone" %}on{% endif %}">Плита чулуу</a>
            <a href="/ads/?cat=material&subcat=interior&item=decoration" class="item-link {% if item == "decoration" %}on{% endif %}">Гоёл чимэглэл</a>
            <a href="/ads/?cat=material&subcat=interior&item=curtain" class="item-link {% if item == "curtain" %}on{% endif %}">Хөшиг тюль</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "outdoor" %}on{% endif %}" onclick="toggleAcc(this)"><span>🌿 Гадна тохижилт</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=outdoor" class="item-link {% if subcat == "outdoor" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=paving" class="item-link {% if item == "paving" %}on{% endif %}">Замын хавтан болон бродюр</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=fence_gate" class="item-link {% if item == "fence_gate" %}on{% endif %}">Хашаа гадна хаалга</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=landscaping" class="item-link {% if item == "landscaping" %}on{% endif %}">Мод зүлэгжүүлэлт</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=cleaning" class="item-link {% if item == "cleaning" %}on{% endif %}">Цэвэрлэгээ тоног төхөөрөмж</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "plumbing" %}on{% endif %}" onclick="toggleAcc(this)"><span>🚿 Сан, халаалт</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=plumbing" class="item-link {% if subcat == "plumbing" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=pipe_fitting" class="item-link {% if item == "pipe_fitting" %}on{% endif %}">Шугам хоолой холбох хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=heating" class="item-link {% if item == "heating" %}on{% endif %}">Халаах хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=sanitary" class="item-link {% if item == "sanitary" %}on{% endif %}">Угаалтуур суултуур ванн</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=ventilation" class="item-link {% if item == "ventilation" %}on{% endif %}">Агааржуулалт хөргөлт</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "electrical" %}on{% endif %}" onclick="toggleAcc(this)"><span>⚡ Цахилгаан, холбоо</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=electrical" class="item-link {% if subcat == "electrical" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=electrical&item=wire_cable" class="item-link {% if item == "wire_cable" %}on{% endif %}">Цахилгааны утас кабель</a>
            <a href="/ads/?cat=material&subcat=electrical&item=lighting" class="item-link {% if item == "lighting" %}on{% endif %}">Гэрэл гэрэлтүүлэг</a>
            <a href="/ads/?cat=material&subcat=electrical&item=switch_socket" class="item-link {% if item == "switch_socket" %}on{% endif %}">Унтраалга залгуур</a>
            <a href="/ads/?cat=material&subcat=electrical&item=fire_alarm" class="item-link {% if item == "fire_alarm" %}on{% endif %}">Галын дохиолол</a>
            <a href="/ads/?cat=material&subcat=electrical&item=internet_tv" class="item-link {% if item == "internet_tv" %}on{% endif %}">Интернэт ТВ</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "safety" %}on{% endif %}" onclick="toggleAcc(this)"><span>🦺 ХАБЭА</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=safety" class="item-link {% if subcat == "safety" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=safety&item=safety_equipment" class="item-link {% if item == "safety_equipment" %}on{% endif %}">ХАБЭА хэрэгсэл</a>
          </div>
        </div>
      </div>
    </div>
    {% elif category == "equipment" %}
    <div class="sb-card">
      <div class="sb-hd">🔩 Тоног төхөөрөмж</div>
      <div class="sb-body">
        <a href="/ads/?cat=equipment" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=equipment&subcat=excavator" class="subcat-link {% if subcat == "excavator" %}on{% endif %}">Экскаватор</a>
        <a href="/ads/?cat=equipment&subcat=crane" class="subcat-link {% if subcat == "crane" %}on{% endif %}">Кран</a>
        <a href="/ads/?cat=equipment&subcat=concrete_mixer" class="subcat-link {% if subcat == "concrete_mixer" %}on{% endif %}">Бетон зуурагч</a>
        <a href="/ads/?cat=equipment&subcat=generator" class="subcat-link {% if subcat == "generator" %}on{% endif %}">Генератор</a>
        <a href="/ads/?cat=equipment&subcat=compressor" class="subcat-link {% if subcat == "compressor" %}on{% endif %}">Компрессор</a>
        <a href="/ads/?cat=equipment&subcat=welding" class="subcat-link {% if subcat == "welding" %}on{% endif %}">Гагнуурын төхөөрөмж</a>
        <a href="/ads/?cat=equipment&subcat=lifting" class="subcat-link {% if subcat == "lifting" %}on{% endif %}">Өргөх төхөөрөмж</a>
        <a href="/ads/?cat=equipment&subcat=tools" class="subcat-link {% if subcat == "tools" %}on{% endif %}">Барилгын багаж</a>
        <a href="/ads/?cat=equipment&subcat=measuring" class="subcat-link {% if subcat == "measuring" %}on{% endif %}">Хэмжилтийн багаж</a>
        <a href="/ads/?cat=equipment&subcat=other_eq" class="subcat-link {% if subcat == "other_eq" %}on{% endif %}">Бусад</a>
      </div>
    </div>
    {% elif category == "rental" %}
    <div class="sb-card">
      <div class="sb-hd">🔑 Түрээс</div>
      <div class="sb-body">
        <a href="/ads/?cat=rental" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=rental&subcat=tech_rent" class="subcat-link {% if subcat == "tech_rent" %}on{% endif %}">Техник түрээс</a>
        <a href="/ads/?cat=rental&subcat=tool_rent" class="subcat-link {% if subcat == "tool_rent" %}on{% endif %}">Багаж түрээс</a>
        <a href="/ads/?cat=rental&subcat=scaffold_rent" class="subcat-link {% if subcat == "scaffold_rent" %}on{% endif %}">Скафольд түрээс</a>
        <a href="/ads/?cat=rental&subcat=crane_rent" class="subcat-link {% if subcat == "crane_rent" %}on{% endif %}">Кран түрээс</a>
        <a href="/ads/?cat=rental&subcat=container_rent" class="subcat-link {% if subcat == "container_rent" %}on{% endif %}">Контейнер түрээс</a>
        <a href="/ads/?cat=rental&subcat=office_rent" class="subcat-link {% if subcat == "office_rent" %}on{% endif %}">Оффис түрээс</a>
        <a href="/ads/?cat=rental&subcat=warehouse_rent" class="subcat-link {% if subcat == "warehouse_rent" %}on{% endif %}">Агуулах түрээс</a>
        <a href="/ads/?cat=rental&subcat=machine_rent" class="subcat-link {% if subcat == "machine_rent" %}on{% endif %}">Машин механизм түрээс</a>
        <a href="/ads/?cat=rental&subcat=other_rent" class="subcat-link {% if subcat == "other_rent" %}on{% endif %}">Бусад түрээс</a>
      </div>
    </div>
    {% elif category == "realestate" %}
    <div class="sb-card">
      <div class="sb-hd">🏠 Үл хөдлөх хөрөнгө</div>
      <div class="sb-body">
        <a href="/ads/?cat=realestate" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "rooms" %}on{% endif %}" onclick="toggleAcc(this)"><span>🛏 Өрөөний тоо</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=realestate&subcat=rooms&item=r1" class="item-link {% if item == "r1" %}on{% endif %}">1 өрөө</a>
            <a href="/ads/?cat=realestate&subcat=rooms&item=r2" class="item-link {% if item == "r2" %}on{% endif %}">2 өрөө</a>
            <a href="/ads/?cat=realestate&subcat=rooms&item=r3" class="item-link {% if item == "r3" %}on{% endif %}">3 өрөө</a>
            <a href="/ads/?cat=realestate&subcat=rooms&item=r3plus" class="item-link {% if item == "r3plus" %}on{% endif %}">3-аас дээш</a>
            <a href="/ads/?cat=realestate&subcat=rooms&item=studio" class="item-link {% if item == "studio" %}on{% endif %}">Студи</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "ub" %}on{% endif %}" onclick="toggleAcc(this)"><span>🏙 Улаанбаатар</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=realestate&subcat=ub&item=bgd" class="item-link {% if item == "bgd" %}on{% endif %}">Баянгол</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=bzd" class="item-link {% if item == "bzd" %}on{% endif %}">Баянзүрх</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=sbd" class="item-link {% if item == "sbd" %}on{% endif %}">Сүхбаатар</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=hud" class="item-link {% if item == "hud" %}on{% endif %}">Хан-Уул</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=chd" class="item-link {% if item == "chd" %}on{% endif %}">Чингэлтэй</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=shd" class="item-link {% if item == "shd" %}on{% endif %}">Сонгинохайрхан</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "province" %}on{% endif %}" onclick="toggleAcc(this)"><span>🗺 Орон нутаг</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=realestate&subcat=province&item=darkhan" class="item-link {% if item == "darkhan" %}on{% endif %}">Дархан-Уул</a>
            <a href="/ads/?cat=realestate&subcat=province&item=orkhon" class="item-link {% if item == "orkhon" %}on{% endif %}">Орхон</a>
            <a href="/ads/?cat=realestate&subcat=province&item=tuv" class="item-link {% if item == "tuv" %}on{% endif %}">Төв</a>
            <a href="/ads/?cat=realestate&subcat=province&item=selenge" class="item-link {% if item == "selenge" %}on{% endif %}">Сэлэнгэ</a>
            <a href="/ads/?cat=realestate&subcat=province&item=other_province" class="item-link {% if item == "other_province" %}on{% endif %}">Бусад аймаг</a>
          </div>
        </div>
      </div>
    </div>
    {% elif category == "service" %}
    <div class="sb-card">
      <div class="sb-hd">🏗 Барилгын үйлчилгээ</div>
      <div class="sb-body">
        <a href="/ads/?cat=service" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=service&subcat=interior_svc" class="subcat-link {% if subcat == "interior_svc" %}on{% endif %}">Интерьер</a>
        <a href="/ads/?cat=service&subcat=carpenter" class="subcat-link {% if subcat == "carpenter" %}on{% endif %}">Мужаан</a>
        <a href="/ads/?cat=service&subcat=tiler" class="subcat-link {% if subcat == "tiler" %}on{% endif %}">Плитачин</a>
        <a href="/ads/?cat=service&subcat=electrician" class="subcat-link {% if subcat == "electrician" %}on{% endif %}">Цахилгаанчин</a>
        <a href="/ads/?cat=service&subcat=plumber" class="subcat-link {% if subcat == "plumber" %}on{% endif %}">Сантехник</a>
        <a href="/ads/?cat=service&subcat=welder" class="subcat-link {% if subcat == "welder" %}on{% endif %}">Гагнуур</a>
        <a href="/ads/?cat=service&subcat=roofing" class="subcat-link {% if subcat == "roofing" %}on{% endif %}">Дээвэр</a>
        <a href="/ads/?cat=service&subcat=road_svc" class="subcat-link {% if subcat == "road_svc" %}on{% endif %}">Зам талбай</a>
        <a href="/ads/?cat=service&subcat=demolition" class="subcat-link {% if subcat == "demolition" %}on{% endif %}">Нураалт</a>
        <a href="/ads/?cat=service&subcat=crane_svc" class="subcat-link {% if subcat == "crane_svc" %}on{% endif %}">Өргөлт кран</a>
        <a href="/ads/?cat=service&subcat=consulting" class="subcat-link {% if subcat == "consulting" %}on{% endif %}">Хяналт зөвлөх</a>
        <a href="/ads/?cat=service&subcat=other_svc" class="subcat-link {% if subcat == "other_svc" %}on{% endif %}">Бусад</a>
      </div>
    </div>
    {% elif category == "design" %}
    <div class="sb-card">
      <div class="sb-hd">📐 Зураг төсөв, дизайн</div>
      <div class="sb-body">
        <a href="/ads/?cat=design" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=design&subcat=architecture" class="subcat-link {% if subcat == "architecture" %}on{% endif %}">Архитектур</a>
        <a href="/ads/?cat=design&subcat=interior_design" class="subcat-link {% if subcat == "interior_design" %}on{% endif %}">Интерьер дизайн</a>
        <a href="/ads/?cat=design&subcat=structure" class="subcat-link {% if subcat == "structure" %}on{% endif %}">Конструкц</a>
        <a href="/ads/?cat=design&subcat=visualization" class="subcat-link {% if subcat == "visualization" %}on{% endif %}">3D визуал</a>
        <a href="/ads/?cat=design&subcat=landscape" class="subcat-link {% if subcat == "landscape" %}on{% endif %}">Ландшафт дизайн</a>
        <a href="/ads/?cat=design&subcat=budget" class="subcat-link {% if subcat == "budget" %}on{% endif %}">Төсөв</a>
        <a href="/ads/?cat=design&subcat=render" class="subcat-link {% if subcat == "render" %}on{% endif %}">Render</a>
        <a href="/ads/?cat=design&subcat=other_design" class="subcat-link {% if subcat == "other_design" %}on{% endif %}">Бусад</a>
      </div>
    </div>
    {% elif category == "worker" %}
    <div class="sb-card">
      <div class="sb-hd">👷 Ажилтан, ажлын зар</div>
      <div class="sb-body">
        <a href="/ads/?cat=worker" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <div class="acc-item">
          <div class="acc-hd" onclick="toggleAcc(this)"><span>🙋 Ажил хайгч</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=worker&subcat=jobseeker_engineer" class="item-link {% if subcat == "jobseeker_engineer" %}on{% endif %}">Инженер</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_architect" class="item-link {% if subcat == "jobseeker_architect" %}on{% endif %}">Архитектор</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_welder" class="item-link {% if subcat == "jobseeker_welder" %}on{% endif %}">Гагнуурчин</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_carpenter" class="item-link {% if subcat == "jobseeker_carpenter" %}on{% endif %}">Мужаан</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_brigade" class="item-link {% if subcat == "jobseeker_brigade" %}on{% endif %}">Бригад</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_other" class="item-link {% if subcat == "jobseeker_other" %}on{% endif %}">Бусад</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd" onclick="toggleAcc(this)"><span>💼 Ажлын байр</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=worker&subcat=job_engineer" class="item-link {% if subcat == "job_engineer" %}on{% endif %}">Инженер</a>
            <a href="/ads/?cat=worker&subcat=job_pm" class="item-link {% if subcat == "job_pm" %}on{% endif %}">Project manager</a>
            <a href="/ads/?cat=worker&subcat=job_safety" class="item-link {% if subcat == "job_safety" %}on{% endif %}">Safety officer</a>
            <a href="/ads/?cat=worker&subcat=job_other" class="item-link {% if subcat == "job_other" %}on{% endif %}">Бусад</a>
          </div>
        </div>
      </div>
    </div>
    {% elif category == "tender" %}
    <div class="sb-card">
      <div class="sb-hd">📋 Тендер, төсөл</div>
      <div class="sb-body">
        <a href="/ads/?cat=tender" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=tender&subcat=tender_item" class="subcat-link {% if subcat == "tender_item" %}on{% endif %}">Тендер</a>
        <a href="/ads/?cat=tender&subcat=contractor" class="subcat-link {% if subcat == "contractor" %}on{% endif %}">Гүйцэтгэгч хайх</a>
        <a href="/ads/?cat=tender&subcat=subcontractor" class="subcat-link {% if subcat == "subcontractor" %}on{% endif %}">Туслан гүйцэтгэгч</a>
        <a href="/ads/?cat=tender&subcat=investment" class="subcat-link {% if subcat == "investment" %}on{% endif %}">Хөрөнгө оруулалт</a>
        <a href="/ads/?cat=tender&subcat=partnership" class="subcat-link {% if subcat == "partnership" %}on{% endif %}">Хамтран ажиллах</a>
        <a href="/ads/?cat=tender&subcat=new_project" class="subcat-link {% if subcat == "new_project" %}on{% endif %}">Шинэ төсөл</a>
      </div>
    </div>
    {% elif category == "company" %}
    <div class="sb-card">
      <div class="sb-hd">🏢 Компаниуд</div>
      <div class="sb-body">
        <a href="/ads/?cat=company" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=company&subcat=construction_company" class="subcat-link {% if subcat == "construction_company" %}on{% endif %}">Барилгын компани</a>
        <a href="/ads/?cat=company&subcat=material_supplier" class="subcat-link {% if subcat == "material_supplier" %}on{% endif %}">Материал нийлүүлэгч</a>
        <a href="/ads/?cat=company&subcat=equipment_supplier" class="subcat-link {% if subcat == "equipment_supplier" %}on{% endif %}">Тоног нийлүүлэгч</a>
        <a href="/ads/?cat=company&subcat=engineering_co" class="subcat-link {% if subcat == "engineering_co" %}on{% endif %}">Инженеринг</a>
        <a href="/ads/?cat=company&subcat=architecture_co" class="subcat-link {% if subcat == "architecture_co" %}on{% endif %}">Архитектур</a>
        <a href="/ads/?cat=company&subcat=factory" class="subcat-link {% if subcat == "factory" %}on{% endif %}">Үйлдвэр</a>
        <a href="/ads/?cat=company&subcat=other_company" class="subcat-link {% if subcat == "other_company" %}on{% endif %}">Бусад</a>
      </div>
    </div>
    {% elif category == "other" %}
    <div class="sb-card">
      <div class="sb-hd">📦 Бусад</div>
      <div class="sb-body">
        <a href="/ads/?cat=other" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=other&subcat=leftover" class="subcat-link {% if subcat == "leftover" %}on{% endif %}">Үлдэгдэл материал</a>
        <a href="/ads/?cat=other&subcat=used_goods" class="subcat-link {% if subcat == "used_goods" %}on{% endif %}">Хэрэглэсэн бараа</a>
        <a href="/ads/?cat=other&subcat=training" class="subcat-link {% if subcat == "training" %}on{% endif %}">Сургалт</a>
        <a href="/ads/?cat=other&subcat=other_misc" class="subcat-link {% if subcat == "other_misc" %}on{% endif %}">Бусад</a>
      </div>
    </div>
    {% else %}
    <div class="sb-card">
      <div class="sb-hd">📂 Ангилалууд</div>
      <div class="sb-body">
        <a href="/ads/?cat=material" class="subcat-link">🧱 Материал</a>
        <a href="/ads/?cat=equipment" class="subcat-link">🔩 Тоног төхөөрөмж</a>
        <a href="/ads/?cat=rental" class="subcat-link">🔑 Түрээс</a>
        <a href="/ads/?cat=realestate" class="subcat-link">🏠 Үл хөдлөх хөрөнгө</a>
        <a href="/ads/?cat=service" class="subcat-link">🏗 Барилгын үйлчилгээ</a>
        <a href="/ads/?cat=design" class="subcat-link">📐 Зураг төсөв</a>
        <a href="/ads/?cat=worker" class="subcat-link">👷 Ажилтан</a>
        <a href="/ads/?cat=tender" class="subcat-link">📋 Тендер</a>
        <a href="/ads/?cat=company" class="subcat-link">🏢 Компаниуд</a>
        <a href="/ads/?cat=other" class="subcat-link">📦 Бусад</a>
      </div>
    </div>
    {% endif %}
    <div class="sb-card">
      <div class="sb-hd">⚡ Хурдан</div>
      <div class="sb-body">
        <a href="/ads/create/" class="subcat-link">📢 Зар оруулах</a>
        <a href="/tender/" class="subcat-link">📋 Тендерүүд</a>
        <a href="/public/" class="subcat-link">🏠 Нүүр хуудас</a>
      </div>
    </div>
  </div>

  <div class="main-content">
    <div class="top-bar">
      <div class="top-t">{{ ads|length }} зар{% if subcat_label %} — {{ subcat_label }}{% endif %}</div>
      <a href="/ads/create/" class="nb nb-y">+ Зар оруулах</a>
    </div>
    {% if ads %}
    <div class="ads-grid">
      {% for ad in ads %}
      <a href="/ads/{{ ad.pk }}/" class="ad-card">
        <div class="ad-img">
          {% if ad.image1 %}<img src="{{ ad.image1.url }}" alt="{{ ad.title }}">
          {% elif ad.category == "realestate" %}🏠
          {% elif ad.category == "material" %}🧱
          {% elif ad.category == "equipment" %}🔩
          {% elif ad.category == "rental" %}🔑
          {% elif ad.category == "service" %}🏗
          {% elif ad.category == "design" %}📐
          {% elif ad.category == "worker" %}👷
          {% elif ad.category == "tender" %}📋
          {% elif ad.category == "company" %}🏢
          {% else %}📦{% endif %}
        </div>
        <div class="ad-body">
          <span class="ad-cat">{{ ad.get_category_display }}</span>
          <div class="ad-t">{{ ad.title|truncatechars:50 }}</div>
          <div class="ad-p">{{ ad.get_price_display_full }}</div>
          <div class="ad-m"><span>📍 {{ ad.city }}</span><span>🕐 {{ ad.created_at|date:"m-d" }}</span></div>
        </div>
      </a>
      {% endfor %}
    </div>
    {% else %}
    <div class="ads-grid">
      <div class="empty">
        <div style="font-size:40px;margin-bottom:12px;">📭</div>
        <div>Зар байхгүй байна.</div>
        <a href="/ads/create/" style="display:inline-block;margin-top:12px;padding:8px 18px;background:#f59e0b;color:#1e3a4a;border-radius:7px;font-size:13px;font-weight:600;">+ Зар оруулах</a>
      </div>
    </div>
    {% endif %}
  </div>
</div>

<script>
function toggleAcc(el) {
  var body = el.nextElementSibling;
  var arr = el.querySelector('.acc-arr');
  var isOpen = body.classList.contains('show');
  document.querySelectorAll('.acc-body').forEach(function(b){b.classList.remove('show');});
  document.querySelectorAll('.acc-arr').forEach(function(a){a.style.transform='';});
  if (!isOpen) {
    body.classList.add('show');
    if (arr) arr.style.transform = 'rotate(90deg)';
  }
}
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.acc-hd.on').forEach(function(hd) {
    var body = hd.nextElementSibling;
    var arr = hd.querySelector('.acc-arr');
    if (body) body.classList.add('show');
    if (arr) arr.style.transform = 'rotate(90deg)';
  });
});
</script>
</body>
</html>"""

with open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK")