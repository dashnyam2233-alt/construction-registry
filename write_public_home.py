html = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>БНБ — Барилгын нэгдсэн бааз | barilgainfo.mn</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f1f5f9;color:#1e293b;}
    a{text-decoration:none;color:inherit;}

    .nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;gap:12px;position:sticky;top:0;z-index:100;}
    .logo{display:flex;align-items:center;gap:8px;}
    .logo-box{width:32px;height:32px;background:#f59e0b;border-radius:7px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
    .logo-box svg{width:18px;height:18px;fill:none;stroke:#fff;stroke-width:2;}
    .logo-t{color:#fff;font-size:13px;font-weight:700;}
    .logo-s{color:#94a3b8;font-size:10px;}
    .nav-links{display:flex;gap:2px;margin-left:12px;}
    .nl{color:#cbd5e1;font-size:12px;padding:5px 9px;border-radius:5px;}
    .nl:hover,.nl.on{background:#f59e0b;color:#1e3a4a;font-weight:600;}
    .nav-r{margin-left:auto;display:flex;gap:6px;align-items:center;}
    .nb{padding:5px 12px;border-radius:6px;font-size:12px;font-weight:500;cursor:pointer;border:none;}
    .nb-o{background:transparent;color:#cbd5e1;border:1px solid #2d4f63;}
    .nb-y{background:#f59e0b;color:#1e3a4a;}

    .hero{background:linear-gradient(135deg,#1e3a4a 0%,#2d5a72 100%);padding:36px 20px;}
    .hero-title{text-align:center;color:#fff;font-size:22px;font-weight:700;margin-bottom:6px;}
    .hero-sub{text-align:center;color:#94a3b8;font-size:13px;margin-bottom:20px;}
    .search-box{max-width:640px;margin:0 auto;background:#fff;border-radius:10px;padding:6px;display:flex;gap:6px;}
    .search-inp{flex:1;padding:9px 14px;border:none;outline:none;font-size:14px;color:#1e293b;border-radius:7px;}
    .search-sel{padding:9px 10px;border:none;border-left:1px solid #e2e8f0;outline:none;font-size:13px;color:#475569;background:#fff;}
    .search-btn{padding:9px 20px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:7px;font-size:13px;font-weight:700;cursor:pointer;}
    .hero-stats{display:flex;justify-content:center;gap:32px;margin-top:20px;}
    .hs .n{font-size:20px;font-weight:700;color:#f59e0b;text-align:center;}
    .hs .l{font-size:11px;color:#94a3b8;text-align:center;margin-top:2px;}

    .cats{background:#fff;border-bottom:1px solid #e2e8f0;padding:0 20px;display:flex;overflow-x:auto;}
    .cat{display:flex;align-items:center;gap:6px;padding:12px 14px;font-size:13px;color:#64748b;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;}
    .cat:hover{color:#1e3a4a;}
    .cat.on{color:#1e3a4a;border-bottom-color:#f59e0b;font-weight:600;}

    .wrap{max-width:1100px;margin:0 auto;padding:16px 20px;display:grid;grid-template-columns:1fr 260px;gap:16px;}

    .sec-hd{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
    .sec-t{font-size:14px;font-weight:600;color:#1e293b;}
    .sec-more{font-size:12px;color:#2f6477;}

    .ads-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:20px;}
    .ad{background:#fff;border:0.5px solid #e2e8f0;border-radius:9px;overflow:hidden;}
    .ad:hover{border-color:#f59e0b;}
    .ad-top{background:#f8fafc;height:80px;display:flex;align-items:center;justify-content:center;font-size:36px;border-bottom:0.5px solid #e2e8f0;}
    .ad-body{padding:10px 12px;}
    .ad-cat{display:inline-block;background:#fef3c7;color:#854f0b;font-size:10px;padding:1px 7px;border-radius:20px;margin-bottom:4px;}
    .ad-t{font-size:13px;font-weight:600;color:#1e293b;line-height:1.35;margin-bottom:4px;}
    .ad-p{font-size:13px;font-weight:700;color:#f59e0b;}
    .ad-m{font-size:11px;color:#94a3b8;margin-top:4px;display:flex;gap:8px;}

    .comp-list{display:flex;flex-direction:column;gap:8px;margin-bottom:20px;}
    .comp-row{background:#fff;border:0.5px solid #e2e8f0;border-radius:9px;padding:12px;display:flex;align-items:center;gap:12px;}
    .comp-row:hover{border-color:#2f6477;}
    .comp-av{width:42px;height:42px;background:#dbeafe;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0;}
    .comp-n{font-size:13px;font-weight:600;color:#1e293b;}
    .comp-t{font-size:11px;color:#64748b;margin-top:2px;}
    .comp-badge{background:#f0fdf4;color:#166534;font-size:10px;padding:1px 7px;border-radius:20px;margin-left:auto;}
    .comp-stars{color:#f59e0b;font-size:11px;text-align:right;}

    .news-list{display:flex;flex-direction:column;gap:8px;margin-bottom:20px;}
    .news-row{background:#fff;border:0.5px solid #e2e8f0;border-radius:9px;padding:12px;display:flex;gap:12px;}
    .news-row:hover{border-color:#2f6477;}
    .news-img{width:56px;height:56px;background:#f8fafc;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0;border:0.5px solid #e2e8f0;}
    .news-tag{display:inline-block;background:#eff6ff;color:#1d4ed8;font-size:10px;padding:1px 7px;border-radius:20px;margin-bottom:3px;}
    .news-t{font-size:13px;font-weight:600;color:#1e293b;line-height:1.4;margin-bottom:3px;}
    .news-m{font-size:11px;color:#94a3b8;}

    .sb{display:flex;flex-direction:column;gap:12px;}
    .sb-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:9px;overflow:hidden;}
    .sb-hd{padding:10px 14px;border-bottom:0.5px solid #e2e8f0;font-size:13px;font-weight:600;}
    .sb-body{padding:12px 14px;}
    .cat-links{display:grid;grid-template-columns:1fr 1fr;gap:6px;}
    .cl{background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:7px;padding:8px;text-align:center;font-size:11px;color:#374151;}
    .cl:hover{background:#fef3c7;border-color:#f59e0b;}
    .cl-ic{font-size:18px;display:block;margin-bottom:3px;}
    .ql-list{display:flex;flex-direction:column;gap:4px;}
    .ql{display:flex;align-items:center;gap:8px;padding:8px 10px;background:#f8fafc;border-radius:7px;font-size:12px;color:#374151;}
    .ql:hover{background:#f1f5f9;}
    .hot-list{display:flex;flex-direction:column;gap:8px;}
    .hot-item{display:flex;gap:8px;}
    .hot-dot{width:6px;height:6px;background:#f59e0b;border-radius:50%;margin-top:5px;flex-shrink:0;}
    .hot-t{font-size:12px;color:#374151;line-height:1.4;}
    .hot-m{font-size:10px;color:#94a3b8;margin-top:1px;}

    .footer{background:#1e3a4a;padding:16px 20px;text-align:center;color:#64748b;font-size:11px;margin-top:0;}
    .footer a{color:#94a3b8;}
    @media(max-width:768px){.wrap{grid-template-columns:1fr;}.sb{display:none;}.hero-stats{gap:16px;}.ads-grid{grid-template-columns:1fr;}}
  </style>
</head>
<body>

<nav class="nav">
  <a href="/public/" class="logo">
    <div class="logo-box"><svg viewBox="0 0 24 24"><path d="M3 21h18M3 7l9-4 9 4M4 7v14M20 7v14M9 21v-6h6v6"/></svg></div>
    <div><div class="logo-t">БНБ — Барилгын нэгдсэн бааз</div><div class="logo-s">barilgainfo.mn</div></div>
  </a>
  <div class="nav-links">
    <a href="/public/" class="nl {% if not tab or tab == 'home' %}on{% endif %}">Нүүр</a>
    <a href="/public/?tab=ads" class="nl {% if tab == 'ads' %}on{% endif %}">Зарууд</a>
    <a href="/public/?tab=companies" class="nl {% if tab == 'companies' %}on{% endif %}">Компаниуд</a>
    <a href="/public/?tab=workers" class="nl {% if tab == 'workers' %}on{% endif %}">Ажилтан</a>
    <a href="/public/?tab=news" class="nl {% if tab == 'news' %}on{% endif %}">Мэдээ</a>
  </div>
  <div class="nav-r">
    {% if user.is_authenticated %}
      <span style="color:#cbd5e1;font-size:12px;">{{ display_name }}</span>
      <a href="/profile/" class="nb nb-o">Профайл</a>
      <form method="post" action="/logout/" style="display:inline;">{% csrf_token %}<button type="submit" class="nb nb-o">Гарах</button></form>
    {% else %}
      <a href="/login/" class="nb nb-o">Нэвтрэх</a>
    {% endif %}
    <a href="/register/" class="nb nb-y">+ Зар оруулах</a>
  </div>
</nav>

<div class="hero">
  <div class="hero-title">Монголын барилгын нэгдсэн платформ</div>
  <div class="hero-sub">Зар, компани, ажилтан, материал — бүгд нэг дороос</div>
  <form method="get" action="/public/" class="search-box">
    <input class="search-inp" name="q" placeholder="Юу хайж байна вэ? Жишээ: тоосго, инженер, барилга компани..." value="{{ request.GET.q|default:'' }}">
    <select class="search-sel" name="cat">
      <option value="">Бүх ангилал</option>
      <option value="house">Орон сууц</option>
      <option value="construction">Барилга ажил</option>
      <option value="material">Материал</option>
      <option value="worker">Ажилтан</option>
      <option value="repair">Засвар</option>
    </select>
    <button type="submit" class="search-btn">🔍 Хайх</button>
  </form>
  <div class="hero-stats">
    <div class="hs"><div class="n">{{ companies_count }}</div><div class="l">Компани</div></div>
    <div class="hs"><div class="n">{{ workers_count }}</div><div class="l">Ажилтан</div></div>
    <div class="hs"><div class="n">{{ slider_ads|length }}</div><div class="l">Зар</div></div>
    <div class="hs"><div class="n">{{ chat_stream|length }}</div><div class="l">Мэдээ</div></div>
  </div>
</div>

<div class="cats">
  <a href="/public/" class="cat {% if not tab or tab == 'home' %}on{% endif %}">🏠 Бүгд</a>
  <a href="/public/?tab=house" class="cat {% if tab == 'house' %}on{% endif %}">🏘️ Орон сууц & Барилга</a>
  <a href="/public/?tab=material" class="cat {% if tab == 'material' %}on{% endif %}">🧱 Материал & Тоног</a>
  <a href="/public/?tab=worker" class="cat {% if tab == 'worker' %}on{% endif %}">👷 Бригад & Ажилчид</a>
  <a href="/public/?tab=repair" class="cat {% if tab == 'repair' %}on{% endif %}">🔧 Засвар & Үйлчилгээ</a>
  <a href="/public/?tab=design" class="cat {% if tab == 'design' %}on{% endif %}">📐 Зураг төсөл</a>
  <a href="/public/?tab=ads" class="cat {% if tab == 'ads' %}on{% endif %}">📢 Бүх зар</a>
</div>

<div class="wrap">
  <div>

    <div class="sec-hd"><div class="sec-t">🔥 Онцлох зарууд</div><a href="/public/?tab=ads" class="sec-more">Бүгдийг харах →</a></div>
    <div class="ads-grid">
      {% for ad in slider_ads|slice:":4" %}
      <div class="ad">
        <div class="ad-top">📢</div>
        <div class="ad-body">
          <span class="ad-cat">Зар</span>
          <div class="ad-t">{{ ad.title }}</div>
          <div class="ad-p">{{ ad.description|default:"Үнийг тохиролцоно" }}</div>
          <div class="ad-m"><span>📍 УБ</span></div>
        </div>
      </div>
      {% empty %}
      <div style="grid-column:1/-1;background:#fff;border:0.5px dashed #e2e8f0;border-radius:9px;padding:24px;text-align:center;color:#94a3b8;font-size:13px;">
        Одоогоор зар байхгүй байна.
        {% if is_admin_like %}<br><a href="/admin/public/sliderad/add/" style="color:#2f6477;font-size:12px;margin-top:6px;display:inline-block;">+ Зар нэмэх</a>{% endif %}
      </div>
      {% endfor %}
    </div>

    <div class="sec-hd"><div class="sec-t">🏢 Бүртгэлтэй компаниуд</div><a href="/public/?tab=companies" class="sec-more">Бүгдийг харах →</a></div>
    <div class="comp-list">
      {% for c in recent_companies %}
      <a href="/company/{{ c.slug }}/" class="comp-row">
        <div class="comp-av">🏢</div>
        <div><div class="comp-n">{{ c.name }}</div><div class="comp-t">{{ c.get_activity_type_display|default:"Барилга" }} · {{ c.get_city_display|default:"УБ" }}</div></div>
        <div style="text-align:right;margin-left:auto;"><div class="comp-stars">★★★★★</div><span class="comp-badge">Идэвхтэй</span></div>
      </a>
      {% empty %}
      <div style="background:#fff;border:0.5px dashed #e2e8f0;border-radius:9px;padding:20px;text-align:center;color:#94a3b8;font-size:13px;">Компани байхгүй байна.</div>
      {% endfor %}
    </div>

    <div class="sec-hd"><div class="sec-t">📰 Барилгын мэдээ</div><a href="/public/?tab=news" class="sec-more">Бүгдийг харах →</a></div>
    <div class="news-list">
      {% for post in chat_stream|slice:":4" %}
      <div class="news-row">
        <div class="news-img">📰</div>
        <div>
          <span class="news-tag">Мэдээ</span>
          <div class="news-t">{{ post.title|default:"Мэдээлэл" }}</div>
          <div class="news-m">📅 {{ post.created_at|date:"Y-m-d" }} · {{ post.author|default:"" }}</div>
        </div>
      </div>
      {% empty %}
      <div style="background:#fff;border:0.5px dashed #e2e8f0;border-radius:9px;padding:20px;text-align:center;color:#94a3b8;font-size:13px;">Мэдээ байхгүй байна.</div>
      {% endfor %}
    </div>

  </div>

  <div class="sb">

    <div class="sb-card">
      <div class="sb-hd">📂 Ангилалаар хайх</div>
      <div class="sb-body">
        <div class="cat-links">
          <a href="/public/?tab=house" class="cl"><span class="cl-ic">🏠</span>Орон сууц</a>
          <a href="/public/?tab=material" class="cl"><span class="cl-ic">🧱</span>Материал</a>
          <a href="/public/?tab=worker" class="cl"><span class="cl-ic">👷</span>Ажилтан</a>
          <a href="/public/?tab=repair" class="cl"><span class="cl-ic">🔧</span>Засвар</a>
          <a href="/public/?tab=design" class="cl"><span class="cl-ic">📐</span>Зураг</a>
          <a href="/public/?tab=ads" class="cl"><span class="cl-ic">📢</span>Бүх зар</a>
        </div>
      </div>
    </div>

    <div class="sb-card">
      <div class="sb-hd">⚡ Хурдан хандах</div>
      <div class="sb-body">
        <div class="ql-list">
          <a href="/register/" class="ql">📢 Зар оруулах</a>
          <a href="/register/" class="ql">🏢 Компани бүртгэх</a>
          <a href="/public/?tab=worker" class="ql">👷 Ажилтан хайх</a>
          <a href="/public/?tab=contact" class="ql">📞 Холбоо барих</a>
          {% if is_admin_like %}<a href="/admin/" class="ql">⚙️ Удирдлага</a>{% endif %}
        </div>
      </div>
    </div>

    <div class="sb-card">
      <div class="sb-hd">🔥 Сүүлийн мэдээ</div>
      <div class="sb-body">
        <div class="hot-list">
          {% for post in chat_stream|slice:":5" %}
          <div class="hot-item">
            <div class="hot-dot"></div>
            <div><div class="hot-t">{{ post.title|truncatechars:45 }}</div><div class="hot-m">{{ post.created_at|date:"Y-m-d" }}</div></div>
          </div>
          {% empty %}
          <div style="color:#94a3b8;font-size:12px;">Мэдээ байхгүй.</div>
          {% endfor %}
        </div>
      </div>
    </div>

    {% if user.is_authenticated %}
    <div class="sb-card">
      <div class="sb-hd">💬 Чат бичих</div>
      <div class="sb-body">
        <form method="post" style="display:flex;gap:6px;">
          {% csrf_token %}
          <input type="hidden" name="action" value="new_post">
          <input type="text" name="post_body" style="flex:1;padding:7px 10px;border:0.5px solid #e2e8f0;border-radius:6px;font-size:12px;outline:none;" placeholder="Бичих...">
          <button type="submit" style="padding:7px 12px;background:#1e3a4a;color:#fff;border:none;border-radius:6px;font-size:12px;cursor:pointer;">→</button>
        </form>
      </div>
    </div>
    {% endif %}

  </div>
</div>

<footer class="footer">
  <div>© 2026 barilgainfo.mn · Монголын барилгын нэгдсэн платформ</div>
  <div style="margin-top:6px;"><a href="/public/?tab=contact">Холбоо барих</a> · <a href="/register/">Бүртгүүлэх</a> · <a href="/admin/">Удирдлага</a></div>
</footer>

</body>
</html>"""

with open("apps/registry/templates/registry/public_home.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK —", len(html), "тэмдэгт")