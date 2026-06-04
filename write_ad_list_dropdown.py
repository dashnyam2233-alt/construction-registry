import json

items = json.load(open("material_items.json", encoding="utf-8"))

SUBCATS = [
    ("foundation", "🏗 Барилгын үндсэн хийц материал"),
    ("interior", "🎨 Засал чимэглэл"),
    ("outdoor", "🌿 Гадна тохижилт"),
    ("plumbing", "🚿 Сан, халаалт, агааржуулалт"),
    ("electrical", "⚡ Цахилгаан, холбоо, дохиолол"),
    ("machinery", "🔩 Машин механизм, тоног"),
    ("furniture", "🪑 Тавилга"),
    ("software", "💻 Программ хангамж, ном"),
    ("safety", "🦺 ХАБЭА"),
]

subcat_options = "\n".join(
    f'<option value="{code}" {{%if subcat=="{code}"%}}selected{{%endif%}}>{label}</option>'
    for code, label in SUBCATS
)

items_js = json.dumps({k: list(v.items()) for k, v in items.items()}, ensure_ascii=False)

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
    @media(max-width:900px){
      .wrap{grid-template-columns:1fr;}
      .sidebar{display:none;}
      .ads-grid{grid-template-columns:1fr 1fr;}
    }
    @media(max-width:480px){
      .ads-grid{grid-template-columns:1fr;}
      .search-wrap{flex-direction:column;}
    }
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
  <form method="get" action="/ads/" class="search-wrap" id="filter-form">
    <input class="search-inp" name="q" placeholder="Зар хайх..." value="{{ q }}">
    <select class="search-sel" name="cat" id="cat-sel" onchange="onCatChange(this)">
      <option value="">📂 Бүх ангилал</option>
      <option value="material" {% if category == 'material' %}selected{% endif %}>🧱 Материал</option>
      <option value="house" {% if category == 'house' %}selected{% endif %}>🏠 Орон сууц</option>
      <option value="worker" {% if category == 'worker' %}selected{% endif %}>👷 Ажилтан</option>
      <option value="repair" {% if category == 'repair' %}selected{% endif %}>🔧 Засвар</option>
      <option value="design" {% if category == 'design' %}selected{% endif %}>📐 Зураг төсөл</option>
      <option value="other" {% if category == 'other' %}selected{% endif %}>📦 Бусад</option>
    </select>
    <select class="search-sel" name="subcat" id="subcat-sel" style="display:{% if category == 'material' %}block{% else %}none{% endif %};">
      <option value="">📋 Бүх дэд ангилал</option>
      """ + subcat_options + """
    </select>
    <select class="search-sel" name="item" id="item-sel" style="display:{% if subcat %}block{% else %}none{% endif %};">
      <option value="">— Дэд төрөл —</option>
      {% for code, label in item_choices %}
      <option value="{{ code }}" {% if item == code %}selected{% endif %}>{{ label }}</option>
      {% endfor %}
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
  <a href="/ads/" style="font-size:12px;color:#e53e3e;margin-left:4px;">✕ Цэвэрлэх</a>
</div>
{% endif %}

<div class="cats">
  <a href="/ads/" class="cat {% if not category %}on{% endif %}">🏠 Бүгд</a>
  <a href="/ads/?cat=material" class="cat {% if category == 'material' %}on{% endif %}">🧱 Материал</a>
  <a href="/ads/?cat=house" class="cat {% if category == 'house' %}on{% endif %}">🏠 Орон сууц</a>
  <a href="/ads/?cat=worker" class="cat {% if category == 'worker' %}on{% endif %}">👷 Ажилтан</a>
  <a href="/ads/?cat=repair" class="cat {% if category == 'repair' %}on{% endif %}">🔧 Засвар</a>
  <a href="/ads/?cat=design" class="cat {% if category == 'design' %}on{% endif %}">📐 Зураг төсөл</a>
  <a href="/ads/?cat=other" class="cat {% if category == 'other' %}on{% endif %}">📦 Бусад</a>
</div>

<div class="wrap">
  <div class="sidebar">
    {% if category == 'material' %}
    <div class="sb-card">
      <div class="sb-hd">🧱 Материалын ангилал</div>
      <div class="sb-body">
        <a href="/ads/?cat=material" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=material&subcat=foundation" class="subcat-link {% if subcat == 'foundation' %}on{% endif %}">🏗 Барилгын үндсэн хийц</a>
        <a href="/ads/?cat=material&subcat=interior" class="subcat-link {% if subcat == 'interior' %}on{% endif %}">🎨 Засал чимэглэл</a>
        <a href="/ads/?cat=material&subcat=outdoor" class="subcat-link {% if subcat == 'outdoor' %}on{% endif %}">🌿 Гадна тохижилт</a>
        <a href="/ads/?cat=material&subcat=plumbing" class="subcat-link {% if subcat == 'plumbing' %}on{% endif %}">🚿 Сан, халаалт</a>
        <a href="/ads/?cat=material&subcat=electrical" class="subcat-link {% if subcat == 'electrical' %}on{% endif %}">⚡ Цахилгаан, холбоо</a>
        <a href="/ads/?cat=material&subcat=machinery" class="subcat-link {% if subcat == 'machinery' %}on{% endif %}">🔩 Машин, тоног</a>
        <a href="/ads/?cat=material&subcat=furniture" class="subcat-link {% if subcat == 'furniture' %}on{% endif %}">🪑 Тавилга</a>
        <a href="/ads/?cat=material&subcat=software" class="subcat-link {% if subcat == 'software' %}on{% endif %}">💻 Программ, ном</a>
        <a href="/ads/?cat=material&subcat=safety" class="subcat-link {% if subcat == 'safety' %}on{% endif %}">🦺 ХАБЭА</a>
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
          {% elif ad.category == 'house' %}🏠
          {% elif ad.category == 'material' %}🧱
          {% elif ad.category == 'worker' %}👷
          {% elif ad.category == 'repair' %}🔧
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
const ITEMS = """ + items_js + """;

function onCatChange(sel) {
  const subSel = document.getElementById('subcat-sel');
  const itemSel = document.getElementById('item-sel');
  if (sel.value === 'material') {
    subSel.style.display = 'block';
  } else {
    subSel.style.display = 'none';
    subSel.value = '';
    itemSel.style.display = 'none';
    itemSel.value = '';
  }
}

function onSubcatChange(sel) {
  const itemSel = document.getElementById('item-sel');
  const code = sel.value;
  if (code && ITEMS[code]) {
    itemSel.innerHTML = '<option value="">— Бүх дэд төрөл —</option>';
    ITEMS[code].forEach(([icode, ilabel]) => {
      const opt = document.createElement('option');
      opt.value = icode;
      opt.textContent = ilabel;
      itemSel.appendChild(opt);
    });
    itemSel.style.display = 'block';
  } else {
    itemSel.style.display = 'none';
    itemSel.value = '';
  }
}

document.getElementById('subcat-sel').addEventListener('change', function() {
  onSubcatChange(this);
});
</script>
</body>
</html>"""

with open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK — ad_list.html бэлэн")