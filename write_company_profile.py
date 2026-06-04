html = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ company.name }} — БНБ</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f1f5f9;}
    a{text-decoration:none;color:inherit;}
    .nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;gap:12px;}
    .logo-box{width:32px;height:32px;background:#f59e0b;border-radius:7px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
    .logo-box svg{width:18px;height:18px;fill:none;stroke:#fff;stroke-width:2;}
    .logo-t{color:#fff;font-size:13px;font-weight:700;margin-left:8px;}
    .nav-r{margin-left:auto;display:flex;gap:6px;align-items:center;}
    .nb{padding:5px 12px;border-radius:6px;font-size:12px;font-weight:500;border:none;cursor:pointer;}
    .nb-o{background:transparent;color:#cbd5e1;border:1px solid #2d4f63;}
    .nb-y{background:#f59e0b;color:#1e3a4a;}
    .breadcrumb{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:10px 20px;font-size:12px;color:#64748b;}
    .breadcrumb a{color:#2f6477;}

    .hero{background:#1e3a4a;padding:28px 20px;}
    .hero-inner{max-width:1000px;margin:0 auto;display:flex;align-items:center;gap:20px;}
    .hero-logo{width:72px;height:72px;background:#f59e0b;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:32px;flex-shrink:0;}
    .hero-info{flex:1;}
    .hero-name{font-size:22px;font-weight:700;color:#fff;margin-bottom:6px;}
    .hero-type{display:inline-block;background:#f59e0b;color:#1e3a4a;font-size:11px;font-weight:600;padding:2px 10px;border-radius:20px;margin-bottom:8px;}
    .hero-meta{display:flex;gap:16px;flex-wrap:wrap;}
    .hero-meta span{font-size:12px;color:#94a3b8;display:flex;align-items:center;gap:4px;}
    .hero-actions{display:flex;gap:8px;flex-shrink:0;}
    .btn-contact{padding:9px 18px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;}
    .btn-share{padding:9px 14px;background:transparent;color:#cbd5e1;border:1px solid #2d4f63;border-radius:8px;font-size:13px;cursor:pointer;}

    .stats-bar{background:#2d4f63;padding:12px 20px;}
    .stats-inner{max-width:1000px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:0;}
    .stat{text-align:center;padding:8px;border-right:0.5px solid rgba(255,255,255,0.1);}
    .stat:last-child{border-right:none;}
    .stat-n{font-size:20px;font-weight:700;color:#f59e0b;}
    .stat-l{font-size:11px;color:#94a3b8;margin-top:2px;}

    .wrap{max-width:1000px;margin:20px auto;padding:0 20px;display:grid;grid-template-columns:1fr 280px;gap:16px;}

    .card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;margin-bottom:14px;overflow:hidden;}
    .card-hd{padding:14px 16px;border-bottom:0.5px solid #e2e8f0;font-size:14px;font-weight:600;color:#1e293b;}
    .card-body{padding:16px;}

    .desc{font-size:13px;color:#374151;line-height:1.7;}

    .info-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
    .info-item{display:flex;flex-direction:column;gap:3px;}
    .info-label{font-size:11px;color:#94a3b8;font-weight:500;}
    .info-val{font-size:13px;color:#1e293b;font-weight:500;}

    .worker-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;}
    .worker-card{background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:8px;padding:12px;text-align:center;}
    .worker-av{width:40px;height:40px;background:#dbeafe;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px;margin:0 auto 8px;}
    .worker-name{font-size:12px;font-weight:600;color:#1e293b;}
    .worker-role{font-size:11px;color:#64748b;margin-top:2px;}
    .locked-msg{background:#fefce8;border:0.5px solid #fef08a;border-radius:8px;padding:14px;text-align:center;font-size:13px;color:#854d0e;}
    .locked-msg a{color:#2f6477;font-weight:600;}

    .brigade-list{display:flex;flex-direction:column;gap:8px;}
    .brigade-item{background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:8px;padding:12px;display:flex;align-items:center;gap:10px;}
    .brigade-ic{font-size:20px;}
    .brigade-n{font-size:13px;font-weight:600;color:#1e293b;}
    .brigade-t{font-size:11px;color:#64748b;margin-top:2px;}

    .sb-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;margin-bottom:14px;overflow:hidden;}
    .sb-hd{padding:12px 14px;border-bottom:0.5px solid #e2e8f0;font-size:13px;font-weight:600;}
    .sb-body{padding:14px;}
    .contact-item{display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:0.5px solid #f1f5f9;}
    .contact-item:last-child{border-bottom:none;}
    .contact-ic{font-size:16px;flex-shrink:0;margin-top:1px;}
    .contact-label{font-size:11px;color:#94a3b8;}
    .contact-val{font-size:13px;color:#1e293b;font-weight:500;margin-top:1px;}
    .contact-val a{color:#2f6477;}
    .badge{display:inline-block;background:#f0fdf4;color:#166534;font-size:11px;padding:3px 10px;border-radius:20px;}
    .map-placeholder{background:#f1f5f9;border-radius:8px;height:120px;display:flex;align-items:center;justify-content:center;font-size:13px;color:#94a3b8;margin-top:10px;}

    .share-btns{display:flex;gap:8px;}
    .share-btn{flex:1;padding:8px;border:0.5px solid #e2e8f0;border-radius:7px;font-size:12px;color:#374151;text-align:center;cursor:pointer;background:#f8fafc;}
    .share-btn:hover{background:#f1f5f9;}

    .footer{background:#1e3a4a;padding:16px 20px;text-align:center;color:#64748b;font-size:11px;margin-top:0;}
    .footer a{color:#94a3b8;}
    @media(max-width:768px){.wrap{grid-template-columns:1fr;}.hero-inner{flex-direction:column;align-items:flex-start;}.stats-inner{grid-template-columns:1fr 1fr;}.worker-grid{grid-template-columns:1fr 1fr;}}
  </style>
</head>
<body>

<nav class="nav">
  <a href="/public/" style="display:flex;align-items:center;gap:8px;">
    <div class="logo-box"><svg viewBox="0 0 24 24"><path d="M3 21h18M3 7l9-4 9 4M4 7v14M20 7v14M9 21v-6h6v6"/></svg></div>
    <span class="logo-t">БНБ — Барилгын нэгдсэн бааз</span>
  </a>
  <div class="nav-r">
    {% if user.is_authenticated %}
      <span style="color:#cbd5e1;font-size:12px;">{{ display_name }}</span>
      <form method="post" action="/logout/" style="display:inline;">{% csrf_token %}<button type="submit" class="nb nb-o">Гарах</button></form>
    {% else %}
      <a href="/login/" class="nb nb-o">Нэвтрэх</a>
      <a href="/register/" class="nb nb-y">Бүртгүүлэх</a>
    {% endif %}
  </div>
</nav>

<div class="breadcrumb">
  <a href="/public/">Нүүр</a> › <a href="/public/?tab=companies">Компаниуд</a> › {{ company.name }}
</div>

<div class="hero">
  <div class="hero-inner">
    <div class="hero-logo">
      {% if company.display_logo_url %}
        <img src="{{ company.display_logo_url }}" alt="{{ company.name }}" style="width:100%;height:100%;object-fit:cover;border-radius:14px;">
      {% else %}🏢{% endif %}
    </div>
    <div class="hero-info">
      <div class="hero-name">{{ company.name }}</div>
      <span class="hero-type">{{ company.get_activity_type_display|default:"Барилга" }}</span>
      <div class="hero-meta">
        {% if company.get_city_display %}<span>📍 {{ company.get_city_display }}</span>{% endif %}
        {% if company.phone %}<span>📞 {{ company.phone }}</span>{% endif %}
        {% if company.established_year %}<span>📅 {{ company.established_year }} оноос</span>{% endif %}
        {% if company.employee_count %}<span>👥 {{ company.employee_count }} ажилтан</span>{% endif %}
      </div>
    </div>
    <div class="hero-actions">
      {% if company.phone %}
      <a href="tel:{{ company.phone }}" class="btn-contact">📞 Холбогдох</a>
      {% else %}
      <button class="btn-contact">📞 Холбогдох</button>
      {% endif %}
      <button class="btn-share" onclick="navigator.share ? navigator.share({title:'{{ company.name }}',url:window.location.href}) : navigator.clipboard.writeText(window.location.href)">🔗 Хуваалцах</button>
    </div>
  </div>
</div>

<div class="stats-bar">
  <div class="stats-inner">
    <div class="stat"><div class="stat-n">{{ workers_total }}</div><div class="stat-l">Ажиллагсад</div></div>
    <div class="stat"><div class="stat-n">{{ brigades_total }}</div><div class="stat-l">Бригадууд</div></div>
    <div class="stat"><div class="stat-n">{{ company.employee_count|default:"—" }}</div><div class="stat-l">Нийт ажилчид</div></div>
    <div class="stat"><div class="stat-n">{{ company.established_year|default:"—" }}</div><div class="stat-l">Үүссэн он</div></div>
  </div>
</div>

<div class="wrap">
  <div>

    {% if company.description %}
    <div class="card">
      <div class="card-hd">📋 Компанийн тухай</div>
      <div class="card-body"><div class="desc">{{ company.description }}</div></div>
    </div>
    {% endif %}

    <div class="card">
      <div class="card-hd">ℹ️ Үндсэн мэдээлэл</div>
      <div class="card-body">
        <div class="info-grid">
          {% if company.register_no %}
          <div class="info-item"><span class="info-label">Регистрийн дугаар</span><span class="info-val">{{ company.register_no }}</span></div>
          {% endif %}
          {% if company.activity_direction %}
          <div class="info-item"><span class="info-label">Үйл ажиллагааны чиглэл</span><span class="info-val">{{ company.get_activity_direction_display|default:company.activity_direction }}</span></div>
          {% endif %}
          {% if company.get_city_display %}
          <div class="info-item"><span class="info-label">Хот/Аймаг</span><span class="info-val">{{ company.get_city_display }}</span></div>
          {% endif %}
          {% if company.address %}
          <div class="info-item"><span class="info-label">Хаяг</span><span class="info-val">{{ company.address }}</span></div>
          {% endif %}
          {% if company.established_year %}
          <div class="info-item"><span class="info-label">Үүссэн он</span><span class="info-val">{{ company.established_year }}</span></div>
          {% endif %}
          {% if company.employee_count %}
          <div class="info-item"><span class="info-label">Ажилчдын тоо</span><span class="info-val">{{ company.employee_count }}</span></div>
          {% endif %}
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-hd">👷 Ажиллагсад <span style="background:#f1f5f9;color:#64748b;font-size:11px;padding:2px 8px;border-radius:20px;margin-left:6px;">{{ workers_total }}</span></div>
      <div class="card-body">
        {% if workers %}
          <div class="worker-grid">
            {% for w in workers %}
            <div class="worker-card">
              <div class="worker-av">👤</div>
              <div class="worker-name">{{ w.first_name }} {{ w.last_name }}</div>
              <div class="worker-role">{{ w.get_responsible_role_display|default:w.get_profession_display|default:"—" }}</div>
            </div>
            {% endfor %}
          </div>
          {% if not is_auth and workers_total > 3 %}
          <div class="locked-msg" style="margin-top:12px;">
            🔒 Нийт {{ workers_total }} ажилтны мэдээлэл харахын тулд <a href="/login/">нэвтрэх</a> шаардлагатай.
          </div>
          {% endif %}
        {% else %}
          <div class="locked-msg">
            {% if is_auth %}
              Ажиллагсдын мэдээлэл оруулаагүй байна.
            {% else %}
              🔒 Ажиллагсдын мэдээлэл харахын тулд <a href="/login/">нэвтрэх</a> шаардлагатай.
            {% endif %}
          </div>
        {% endif %}
      </div>
    </div>

    {% if brigades %}
    <div class="card">
      <div class="card-hd">🏗️ Бригадууд <span style="background:#f1f5f9;color:#64748b;font-size:11px;padding:2px 8px;border-radius:20px;margin-left:6px;">{{ brigades_total }}</span></div>
      <div class="card-body">
        <div class="brigade-list">
          {% for b in brigades %}
          <div class="brigade-item">
            <span class="brigade-ic">🏗️</span>
            <div><div class="brigade-n">{{ b.name }}</div><div class="brigade-t">{{ b.get_activity_directions_display|default:"—" }}</div></div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>
    {% endif %}

  </div>

  <div>

    <div class="sb-card">
      <div class="sb-hd">📞 Холбоо барих</div>
      <div class="sb-body">
        {% if company.phone %}
        <div class="contact-item">
          <span class="contact-ic">📞</span>
          <div><div class="contact-label">Утас</div><div class="contact-val"><a href="tel:{{ company.phone }}">{{ company.phone }}</a></div></div>
        </div>
        {% endif %}
        {% if company.email %}
        <div class="contact-item">
          <span class="contact-ic">✉️</span>
          <div><div class="contact-label">И-мэйл</div><div class="contact-val"><a href="mailto:{{ company.email }}">{{ company.email }}</a></div></div>
        </div>
        {% endif %}
        {% if company.website %}
        <div class="contact-item">
          <span class="contact-ic">🌐</span>
          <div><div class="contact-label">Вэб сайт</div><div class="contact-val"><a href="{{ company.website }}" target="_blank">{{ company.website }}</a></div></div>
        </div>
        {% endif %}
        {% if company.facebook_url %}
        <div class="contact-item">
          <span class="contact-ic">📘</span>
          <div><div class="contact-label">Facebook</div><div class="contact-val"><a href="{{ company.facebook_url }}" target="_blank">Холбоос</a></div></div>
        </div>
        {% endif %}
        {% if company.address %}
        <div class="contact-item">
          <span class="contact-ic">📍</span>
          <div><div class="contact-label">Хаяг</div><div class="contact-val">{{ company.address }}</div></div>
        </div>
        {% endif %}
        {% if not company.phone and not company.email %}
        <div style="color:#94a3b8;font-size:12px;">Холбоо барих мэдээлэл оруулаагүй байна.</div>
        {% endif %}
        <div class="map-placeholder">🗺️ Байршил тодорхойгүй</div>
      </div>
    </div>

    <div class="sb-card">
      <div class="sb-hd">🏷️ Ангилал & Статус</div>
      <div class="sb-body">
        <div style="display:flex;flex-wrap:wrap;gap:6px;">
          <span class="badge">{{ company.get_activity_type_display|default:"Барилга" }}</span>
          {% if company.get_city_display %}<span class="badge">📍 {{ company.get_city_display }}</span>{% endif %}
          <span style="background:#f0fdf4;color:#166534;font-size:11px;padding:3px 10px;border-radius:20px;display:inline-block;">✅ Идэвхтэй</span>
        </div>
      </div>
    </div>

    {% if is_owner %}
    <div class="sb-card">
      <div class="sb-hd">⚙️ Удирдлага</div>
      <div class="sb-body">
        <div style="display:flex;flex-direction:column;gap:6px;">
          <a href="/admin/core/company/" style="display:flex;align-items:center;gap:8px;padding:8px 10px;background:#f8fafc;border-radius:7px;font-size:12px;color:#374151;">✏️ Мэдээлэл засах</a>
          <a href="/admin/core/worker/add/" style="display:flex;align-items:center;gap:8px;padding:8px 10px;background:#f8fafc;border-radius:7px;font-size:12px;color:#374151;">👷 Ажилтан нэмэх</a>
        </div>
      </div>
    </div>
    {% endif %}

    <div class="sb-card">
      <div class="sb-hd">🔗 Хуваалцах</div>
      <div class="sb-body">
        <div class="share-btns">
          <div class="share-btn" onclick="navigator.clipboard.writeText(window.location.href);alert('Хуулагдлаа!')">📋 Хуулах</div>
          <a href="https://www.facebook.com/sharer/sharer.php?u={{ request.build_absolute_uri }}" target="_blank" class="share-btn">📘 FB</a>
        </div>
      </div>
    </div>

  </div>
</div>

<footer class="footer">
  <div>© 2026 barilgainfo.mn · Монголын барилгын нэгдсэн платформ</div>
  <div style="margin-top:6px;"><a href="/public/">← Нүүр хуудас</a></div>
</footer>

</body>
</html>"""

with open("apps/registry/templates/registry/company_profile.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK —", len(html), "тэмдэгт")