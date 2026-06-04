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
    .search-wrap{display:flex;gap:8px;flex-wrap:wrap;max-width:900px;}
    .search-inp{flex:2;min-width:160px;padding:8px 14px;border:none;outline:none;font-size:13px;border-radius:8px;}
    .search-sel{flex:1;min-width:140px;padding:8px 10px;border:none;outline:none;font-size:12px;color:#1e293b;background:#fff;border-radius:8px;}
    .search-btn{padding:8px 18px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;}
    .filter-bar{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:8px 20px;display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
    .filter-tag{display:inline-flex;align-items:center;gap:4px;background:#fef3c7;color:#854d0e;font-size:11px;padding:3px 10px;border-radius:20px;}
    .cats{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:0 20px;display:flex;overflow-x:auto;}
    .cat{display:flex;align-items:center;gap:5px;padding:10px 14px;font-size:12px;color:#64748b;border-bottom:2px solid transparent;white-space:nowrap;}
    .cat:hover{color:#1e3a4a;}
    .cat.on{color:#1e3a4a;border-bottom-color:#f59e0b;font-weight:600;}
    .wrap{max-width:1100px;margin:16px auto;padding:0 20px;display:grid;grid-template-columns:220px 1fr;gap:16px;}
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
    @media(max-width:900px){.wrap{grid-template-columns:1fr;}.sidebar{display:none;}.ads-grid{grid-template-columns:1fr 1fr;}}
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
      <option value="house" {% if category == "house" %}selected{% endif %}>🏠 Орон сууц</option>
      <option value="worker" {% if category == "worker" %}selected{% endif %}>👷 Ажилтан</option>
      <option value="repair" {% if category == "repair" %}selected{% endif %}>🔧 Засвар</option>
      <option value="design" {% if category == "design" %}selected{% endif %}>📐 Зураг төсөл</option>
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
  {% if item_label %}<span class="filter-tag">{{ item_label }}</span>{% endif %}
  {% if q %}<span class="filter-tag">🔍 "{{ q }}"</span>{% endif %}
  <a href="/ads/" style="font-size:12px;color:#e53e3e;">✕ Цэвэрлэх</a>
</div>
{% endif %}

<div class="cats">
  <a href="/ads/" class="cat {% if not category %}on{% endif %}">🏠 Бүгд</a>
  <a href="/ads/?cat=material" class="cat {% if category == "material" %}on{% endif %}">🧱 Материал</a>
  <a href="/ads/?cat=house" class="cat {% if category == "house" %}on{% endif %}">🏠 Орон сууц</a>
  <a href="/ads/?cat=worker" class="cat {% if category == "worker" %}on{% endif %}">👷 Ажилтан</a>
  <a href="/ads/?cat=repair" class="cat {% if category == "repair" %}on{% endif %}">🔧 Засвар</a>
  <a href="/ads/?cat=design" class="cat {% if category == "design" %}on{% endif %}">📐 Зураг төсөл</a>
  <a href="/ads/?cat=other" class="cat {% if category == "other" %}on{% endif %}">📦 Бусад</a>
</div>

<div class="wrap">
  <div class="sidebar">
    {% if category == "material" %}
    <div class="sb-card">
      <div class="sb-hd">🧱 Материалын ангилал</div>
      <div class="sb-body">
        <a href="/ads/?cat=material" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "foundation" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🏗 Барилгын үндсэн хийц</span><span class="acc-arr">▶</span>
          </div>
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
          <div class="acc-hd {% if subcat == "interior" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🎨 Засал чимэглэл</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=interior" class="item-link {% if subcat == "interior" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=interior&item=paint" class="item-link {% if item == "paint" %}on{% endif %}">Будаг эмульс</a>
            <a href="/ads/?cat=material&subcat=interior&item=dry_mix" class="item-link {% if item == "dry_mix" %}on{% endif %}">Хуурай хольц</a>
            <a href="/ads/?cat=material&subcat=interior&item=wallpaper" class="item-link {% if item == "wallpaper" %}on{% endif %}">Обой хуулга</a>
            <a href="/ads/?cat=material&subcat=interior&item=parquet" class="item-link {% if item == "parquet" %}on{% endif %}">Паркет ламинат</a>
            <a href="/ads/?cat=material&subcat=interior&item=floor_accessories" class="item-link {% if item == "floor_accessories" %}on{% endif %}">Шал дагалдах</a>
            <a href="/ads/?cat=material&subcat=interior&item=tile_stone" class="item-link {% if item == "tile_stone" %}on{% endif %}">Плита чулуу</a>
            <a href="/ads/?cat=material&subcat=interior&item=decoration" class="item-link {% if item == "decoration" %}on{% endif %}">Гоёл чимэглэл</a>
            <a href="/ads/?cat=material&subcat=interior&item=curtain" class="item-link {% if item == "curtain" %}on{% endif %}">Хөшиг тюль</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "outdoor" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🌿 Гадна тохижилт</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=outdoor" class="item-link {% if subcat == "outdoor" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=paving" class="item-link {% if item == "paving" %}on{% endif %}">Замын хавтан болон бродюр</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=fence_gate" class="item-link {% if item == "fence_gate" %}on{% endif %}">Хашаа гадна хаалга</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=playground" class="item-link {% if item == "playground" %}on{% endif %}">Хүүхдийн тоглоом талбай</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=landscaping" class="item-link {% if item == "landscaping" %}on{% endif %}">Мод зүлэгжүүлэлт</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=cleaning" class="item-link {% if item == "cleaning" %}on{% endif %}">Цэвэрлэгээ тоног төхөөрөмж</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "plumbing" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🚿 Сан, халаалт</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=plumbing" class="item-link {% if subcat == "plumbing" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=pipe_fitting" class="item-link {% if item == "pipe_fitting" %}on{% endif %}">Шугам хоолой холбох хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=heating" class="item-link {% if item == "heating" %}on{% endif %}">Халаах хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=sanitary" class="item-link {% if item == "sanitary" %}on{% endif %}">Угаалтуур суултуур ванн</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=ventilation" class="item-link {% if item == "ventilation" %}on{% endif %}">Агааржуулалт хөргөлт</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "electrical" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>⚡ Цахилгаан, холбоо</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=electrical" class="item-link {% if subcat == "electrical" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=electrical&item=wire_cable" class="item-link {% if item == "wire_cable" %}on{% endif %}">Цахилгааны утас кабель</a>
            <a href="/ads/?cat=material&subcat=electrical&item=electrical_fitting" class="item-link {% if item == "electrical_fitting" %}on{% endif %}">Цахилгаан холбох хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=electrical&item=lighting" class="item-link {% if item == "lighting" %}on{% endif %}">Гэрэл гэрэлтүүлэг</a>
            <a href="/ads/?cat=material&subcat=electrical&item=generator_meter" class="item-link {% if item == "generator_meter" %}on{% endif %}">Цахилгааны үүсгүүр тоолуур</a>
            <a href="/ads/?cat=material&subcat=electrical&item=switch_socket" class="item-link {% if item == "switch_socket" %}on{% endif %}">Унтраалга залгуур</a>
            <a href="/ads/?cat=material&subcat=electrical&item=signal" class="item-link {% if item == "signal" %}on{% endif %}">Холбоо дохиолол</a>
            <a href="/ads/?cat=material&subcat=electrical&item=fire_alarm" class="item-link {% if item == "fire_alarm" %}on{% endif %}">Галын дохиолол</a>
            <a href="/ads/?cat=material&subcat=electrical&item=domophone" class="item-link {% if item == "domophone" %}on{% endif %}">Домофон ухаалаг цоож</a>
            <a href="/ads/?cat=material&subcat=electrical&item=internet_tv" class="item-link {% if item == "internet_tv" %}on{% endif %}">Интернэт ТВ</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "machinery" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🔩 Машин, тоног</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=machinery" class="item-link {% if subcat == "machinery" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=machinery&item=machine" class="item-link {% if item == "machine" %}on{% endif %}">Машин механизм</a>
            <a href="/ads/?cat=material&subcat=machinery&item=construction_equipment" class="item-link {% if item == "construction_equipment" %}on{% endif %}">Барилгын тоног төхөөрөмж</a>
            <a href="/ads/?cat=material&subcat=machinery&item=tools" class="item-link {% if item == "tools" %}on{% endif %}">Барилгын багаж хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=machinery&item=elevator" class="item-link {% if item == "elevator" %}on{% endif %}">Лифт угсардаг шат</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "furniture" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🪑 Тавилга</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=furniture" class="item-link {% if subcat == "furniture" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=furniture&item=office" class="item-link {% if item == "office" %}on{% endif %}">Албан тасалгаа</a>
            <a href="/ads/?cat=material&subcat=furniture&item=household" class="item-link {% if item == "household" %}on{% endif %}">Гэр ахуй</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "software" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>💻 Программ хангамж, ном</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=software" class="item-link {% if subcat == "software" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=software&item=software_item" class="item-link {% if item == "software_item" %}on{% endif %}">Программ хангамж</a>
            <a href="/ads/?cat=material&subcat=software&item=book" class="item-link {% if item == "book" %}on{% endif %}">Ном сэтгүүл</a>
            <a href="/ads/?cat=material&subcat=software&item=manual" class="item-link {% if item == "manual" %}on{% endif %}">Гарын авлага</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "safety" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🦺 ХАБЭА</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=safety" class="item-link {% if subcat == "safety" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=safety&item=safety_equipment" class="item-link {% if item == "safety_equipment" %}on{% endif %}">ХАБЭА хэрэгсэл</a>
          </div>
        </div>
      </div>
    </div>
    {% else %}
    <div class="sb-card">
      <div class="sb-hd">📂 Ангилалууд</div>
      <div class="sb-body">
        <a href="/ads/?cat=material" class="subcat-link">🧱 Материал</a>
        <a href="/ads/?cat=house" class="subcat-link">🏠 Орон сууц</a>
        <a href="/ads/?cat=worker" class="subcat-link">👷 Ажилтан</a>
        <a href="/ads/?cat=repair" class="subcat-link">🔧 Засвар</a>
        <a href="/ads/?cat=design" class="subcat-link">📐 Зураг төсөл</a>
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
      <div class="top-t">
        {{ ads|length }} зар
        {% if subcat_label %} — {{ subcat_label }}{% endif %}
        {% if item_label %} / {{ item_label }}{% endif %}
      </div>
      <a href="/ads/create/" class="nb nb-y">+ Зар оруулах</a>
    </div>
    {% if ads %}
    <div class="ads-grid">
      {% for ad in ads %}
      <a href="/ads/{{ ad.pk }}/" class="ad-card">
        <div class="ad-img">
          {% if ad.image1 %}<img src="{{ ad.image1.url }}" alt="{{ ad.title }}">
          {% elif ad.category == "house" %}🏠
          {% elif ad.category == "material" %}🧱
          {% elif ad.category == "worker" %}👷
          {% elif ad.category == "repair" %}🔧
          {% else %}📢{% endif %}
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