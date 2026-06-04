import os

template = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Тендерүүд — БНБ</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f1f5f9;}
    a{text-decoration:none;color:inherit;}
    .nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;gap:12px;}
    .logo-box{width:32px;height:32px;background:#f59e0b;border-radius:7px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
    .logo-box svg{width:18px;height:18px;fill:none;stroke:#fff;stroke-width:2;}
    .logo-t{color:#fff;font-size:13px;font-weight:700;margin-left:8px;}
    .nav-links{display:flex;gap:2px;margin-left:12px;}
    .nl{color:#cbd5e1;font-size:12px;padding:5px 9px;border-radius:5px;}
    .nl:hover,.nl.on{background:#f59e0b;color:#1e3a4a;font-weight:600;}
    .nav-r{margin-left:auto;display:flex;gap:6px;align-items:center;}
    .nb{padding:5px 12px;border-radius:6px;font-size:12px;font-weight:500;border:none;cursor:pointer;}
    .nb-o{background:transparent;color:#cbd5e1;border:1px solid #2d4f63;}
    .nb-y{background:#f59e0b;color:#1e3a4a;}
    .hero{background:#1e3a4a;padding:24px 20px;}
    .hero-t{color:#fff;font-size:18px;font-weight:700;margin-bottom:6px;}
    .hero-s{color:#94a3b8;font-size:13px;margin-bottom:14px;}
    .search-box{max-width:600px;background:#fff;border-radius:10px;padding:5px;display:flex;gap:6px;}
    .search-inp{flex:1;padding:8px 14px;border:none;outline:none;font-size:13px;border-radius:7px;}
    .search-btn{padding:8px 16px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:7px;font-size:13px;font-weight:700;cursor:pointer;}
    .stats{display:flex;gap:16px;margin-top:14px;flex-wrap:wrap;}
    .stat{background:#2d4f63;border-radius:8px;padding:8px 14px;text-align:center;}
    .stat-n{font-size:18px;font-weight:700;color:#f59e0b;}
    .stat-l{font-size:10px;color:#94a3b8;margin-top:1px;}
    .cats{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:0 20px;display:flex;overflow-x:auto;gap:0;}
    .cat{display:flex;align-items:center;gap:5px;padding:10px 14px;font-size:12px;color:#64748b;border-bottom:2px solid transparent;white-space:nowrap;cursor:pointer;}
    .cat:hover{color:#1e3a4a;}
    .cat.on{color:#1e3a4a;border-bottom-color:#f59e0b;font-weight:600;}
    .wrap{max-width:1000px;margin:16px auto;padding:0 20px;}
    .top-bar{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
    .top-t{font-size:14px;font-weight:600;color:#1e293b;}
    .tender-list{display:flex;flex-direction:column;gap:10px;}
    .tender-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;padding:14px 16px;display:flex;gap:14px;align-items:flex-start;}
    .tender-card:hover{border-color:#f59e0b;box-shadow:0 2px 8px rgba(0,0,0,0.06);}
    .tender-date{background:#1e3a4a;color:#fff;border-radius:8px;padding:8px 10px;text-align:center;min-width:54px;flex-shrink:0;}
    .date-y{font-size:9px;color:#94a3b8;}
    .date-d{font-size:22px;font-weight:700;line-height:1;}
    .date-m{font-size:10px;color:#f59e0b;margin-top:2px;}
    .tender-body{flex:1;min-width:0;}
    .tender-badges{display:flex;gap:6px;margin-bottom:5px;flex-wrap:wrap;}
    .badge{font-size:10px;padding:2px 8px;border-radius:20px;display:inline-block;}
    .badge-construction{background:#fef3c7;color:#854d0e;}
    .badge-repair{background:#fee2e2;color:#991b1b;}
    .badge-design{background:#e0e7ff;color:#3730a3;}
    .badge-road{background:#d1fae5;color:#065f46;}
    .badge-engineering{background:#dbeafe;color:#1e40af;}
    .badge-material{background:#fce7f3;color:#9d174d;}
    .badge-equipment{background:#f3f4f6;color:#374151;}
    .badge-consulting{background:#ede9fe;color:#5b21b6;}
    .badge-service{background:#ecfdf5;color:#065f46;}
    .badge-other{background:#f1f5f9;color:#64748b;}
    .tender-title{font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px;line-height:1.4;}
    .tender-org{font-size:12px;color:#64748b;margin-bottom:5px;}
    .tender-meta{display:flex;gap:10px;flex-wrap:wrap;}
    .tender-meta span{font-size:11px;color:#94a3b8;}
    .tender-price{font-size:15px;font-weight:700;color:#f59e0b;white-space:nowrap;flex-shrink:0;}
    .empty{text-align:center;padding:40px;color:#94a3b8;background:#fff;border-radius:10px;border:0.5px dashed #e2e8f0;}
    .footer{background:#1e3a4a;padding:14px 20px;text-align:center;color:#64748b;font-size:11px;margin-top:20px;}
    @media(max-width:600px){.tender-card{flex-direction:column;}.tender-price{margin-top:6px;}}
  </style>
</head>
<body>

<nav class="nav">
  <a href="/public/" style="display:flex;align-items:center;gap:8px;">
    <div class="logo-box"><svg viewBox="0 0 24 24"><path d="M3 21h18M3 7l9-4 9 4M4 7v14M20 7v14M9 21v-6h6v6"/></svg></div>
    <span class="logo-t">БНБ — Барилгын нэгдсэн бааз</span>
  </a>
  <div class="nav-links">
    <a href="/public/" class="nl">Нүүр</a>
    <a href="/ads/" class="nl">Зарууд</a>
    <a href="/tender/" class="nl on">Тендер</a>
    <a href="/news/" class="nl">Мэдээ</a>
  </div>
  <div class="nav-r">
    {% if user.is_authenticated %}
      <span style="color:#cbd5e1;font-size:12px;">{{ display_name }}</span>
      <a href="/profile/" class="nb nb-o">Профайл</a>
      <form method="post" action="/logout/" style="display:inline;">{% csrf_token %}<button type="submit" class="nb nb-o">Гарах</button></form>
    {% else %}
      <a href="/login/" class="nb nb-o">Нэвтрэх</a>
      <a href="/register/" class="nb nb-y">Бүртгүүлэх</a>
    {% endif %}
  </div>
</nav>

<div class="hero">
  <div class="hero-t">📋 Тендерүүд</div>
  <div class="hero-s">tender.gov.mn-аас өдөр бүр шинэчлэгддэг · Нийт {{ total }} тендер</div>
  <form method="get" action="/tender/" class="search-box">
    <input class="search-inp" name="q" placeholder="Тендер хайх... (нэр, байгууллага, дугаар)" value="{{ q }}">
    {% if cat %}<input type="hidden" name="cat" value="{{ cat }}">{% endif %}
    <button type="submit" class="search-btn">🔍 Хайх</button>
  </form>
  <div class="stats">
    <div class="stat"><div class="stat-n">{{ counts.construction|default:0 }}</div><div class="stat-l">🏗 Барилга</div></div>
    <div class="stat"><div class="stat-n">{{ counts.repair|default:0 }}</div><div class="stat-l">🔧 Засвар</div></div>
    <div class="stat"><div class="stat-n">{{ counts.road|default:0 }}</div><div class="stat-l">🛣 Зам</div></div>
    <div class="stat"><div class="stat-n">{{ counts.engineering|default:0 }}</div><div class="stat-l">⚡ Инженер</div></div>
    <div class="stat"><div class="stat-n">{{ counts.material|default:0 }}</div><div class="stat-l">🧱 Материал</div></div>
    <div class="stat"><div class="stat-n">{{ counts.design|default:0 }}</div><div class="stat-l">📐 Зураг</div></div>
  </div>
</div>

<div class="cats">
  <a href="/tender/" class="cat {% if not cat %}on{% endif %}">📋 Бүгд ({{ total }})</a>
  <a href="/tender/?cat=construction" class="cat {% if cat == 'construction' %}on{% endif %}">🏗 Барилга</a>
  <a href="/tender/?cat=repair" class="cat {% if cat == 'repair' %}on{% endif %}">🔧 Засвар</a>
  <a href="/tender/?cat=road" class="cat {% if cat == 'road' %}on{% endif %}">🛣 Зам, гүүр</a>
  <a href="/tender/?cat=engineering" class="cat {% if cat == 'engineering' %}on{% endif %}">⚡ Инженер</a>
  <a href="/tender/?cat=material" class="cat {% if cat == 'material' %}on{% endif %}">🧱 Материал</a>
  <a href="/tender/?cat=design" class="cat {% if cat == 'design' %}on{% endif %}">📐 Зураг төсөл</a>
  <a href="/tender/?cat=equipment" class="cat {% if cat == 'equipment' %}on{% endif %}">🔩 Тоног</a>
  <a href="/tender/?cat=consulting" class="cat {% if cat == 'consulting' %}on{% endif %}">💼 Зөвлөх</a>
  <a href="/tender/?cat=other" class="cat {% if cat == 'other' %}on{% endif %}">📦 Бусад</a>
</div>

<div class="wrap">
  <div class="top-bar">
    <div class="top-t">{{ tenders|length }} тендер харагдаж байна{% if q %} — "{{ q }}"{% endif %}</div>
    <a href="https://tender.gov.mn" target="_blank" style="font-size:12px;color:#2f6477;">tender.gov.mn →</a>
  </div>

  {% if tenders %}
  <div class="tender-list">
    {% for t in tenders %}
    <a href="{{ t.url }}" target="_blank" class="tender-card">
      <div class="tender-date">
        <div class="date-y">{{ t.deadline|slice:":4" }}</div>
        <div class="date-d">{{ t.deadline|slice:"8:10"|default:"—" }}</div>
        <div class="date-m">{{ t.deadline|slice:"5:7" }}</div>
      </div>
      <div class="tender-body">
        <div class="tender-badges">
          <span class="badge badge-{{ t.category }}">
            {% if t.category == 'construction' %}🏗 Барилга
            {% elif t.category == 'repair' %}🔧 Засвар
            {% elif t.category == 'design' %}📐 Зураг төсөл
            {% elif t.category == 'road' %}🛣 Зам, гүүр
            {% elif t.category == 'engineering' %}⚡ Инженер
            {% elif t.category == 'material' %}🧱 Материал
            {% elif t.category == 'equipment' %}🔩 Тоног
            {% elif t.category == 'consulting' %}💼 Зөвлөх
            {% elif t.category == 'service' %}🛎 Үйлчилгээ
            {% else %}📦 Бусад{% endif %}
          </span>
        </div>
        <div class="tender-title">{{ t.title }}</div>
        <div class="tender-org">🏛 {{ t.organization }}</div>
        <div class="tender-meta">
          {% if t.method %}<span>📜 {{ t.method|truncatechars:50 }}</span>{% endif %}
          {% if t.tender_code %}<span>🔢 {{ t.tender_code }}</span>{% endif %}
        </div>
      </div>
      {% if t.price %}
      <div class="tender-price">{{ t.price }}</div>
      {% endif %}
    </a>
    {% endfor %}
  </div>
  {% else %}
  <div class="empty">
    <div style="font-size:36px;margin-bottom:10px;">📭</div>
    <div>Тендер олдсонгүй.</div>
    {% if q %}<div style="margin-top:6px;font-size:12px;"><a href="/tender/" style="color:#2f6477;">Бүгдийг харах</a></div>{% endif %}
  </div>
  {% endif %}
</div>

<footer class="footer">
  <div>© 2026 barilgainfo.mn · Тендерийн мэдээлэл tender.gov.mn-аас өдөр бүр шинэчлэгддэг</div>
</footer>
</body>
</html>"""

with open("apps/registry/templates/registry/tender_list.html", "w", encoding="utf-8") as f:
    f.write(template)
print("OK — template бэлэн")