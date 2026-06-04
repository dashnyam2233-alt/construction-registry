# Ad detail view нэмэх
view_code = '''

def ad_detail(request, pk):
    from apps.public.models import Ad
    ad = Ad.objects.filter(pk=pk, status="active").first()
    if not ad:
        from django.http import Http404
        raise Http404
    ad.views += 1
    ad.save(update_fields=["views"])
    related = Ad.objects.filter(category=ad.category, status="active").exclude(pk=pk)[:4]
    return render(request, "registry/ad_detail.html", {
        "ad": ad,
        "related": related,
        "display_name": get_display_name(request.user),
    })
'''

content = open("apps/registry/views.py", "r", encoding="utf-8").read()
if "def ad_detail" not in content:
    with open("apps/registry/views.py", "a", encoding="utf-8") as f:
        f.write(view_code)
    print("OK — ad_detail view нэмэгдлээ")
else:
    print("Аль хэдийн байна")

# URL нэмэх
urls = open("apps/registry/urls.py", "r", encoding="utf-8").read()
if "ad_detail" not in urls:
    urls = urls.replace(
        "from .views import (",
        "from .views import (\n    ad_detail,"
    )
    urls = urls.replace(
        '    path("ads/create/", ad_create, name="ad_create"),',
        '    path("ads/create/", ad_create, name="ad_create"),\n    path("ads/<int:pk>/", ad_detail, name="ad_detail"),'
    )
    open("apps/registry/urls.py", "w", encoding="utf-8").write(urls)
    print("OK — URL нэмэгдлээ")

# Template
template = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ ad.title }} — БНБ</title>
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
    .breadcrumb{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:10px 20px;font-size:12px;color:#64748b;}
    .breadcrumb a{color:#2f6477;}
    .wrap{max-width:960px;margin:20px auto;padding:0 20px;display:grid;grid-template-columns:1fr 300px;gap:16px;}
    .card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;margin-bottom:14px;overflow:hidden;}
    .card-hd{padding:14px 16px;border-bottom:0.5px solid #e2e8f0;font-size:14px;font-weight:600;}
    .card-body{padding:16px;}
    .img-main{width:100%;height:280px;background:#f8fafc;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:64px;margin-bottom:14px;overflow:hidden;border:0.5px solid #e2e8f0;}
    .img-main img{width:100%;height:100%;object-fit:cover;}
    .img-thumbs{display:flex;gap:8px;margin-bottom:14px;}
    .img-thumb{width:72px;height:72px;border-radius:7px;background:#f8fafc;border:0.5px solid #e2e8f0;display:flex;align-items:center;justify-content:center;font-size:24px;overflow:hidden;cursor:pointer;}
    .img-thumb img{width:100%;height:100%;object-fit:cover;}
    .ad-cat{display:inline-block;background:#fef3c7;color:#854f0b;font-size:11px;padding:2px 10px;border-radius:20px;margin-bottom:8px;}
    .ad-title{font-size:20px;font-weight:700;color:#1e293b;margin-bottom:10px;line-height:1.35;}
    .ad-price{font-size:24px;font-weight:700;color:#f59e0b;margin-bottom:12px;}
    .ad-meta{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:16px;}
    .ad-meta span{font-size:12px;color:#64748b;display:flex;align-items:center;gap:4px;}
    .ad-desc{font-size:13px;color:#374151;line-height:1.7;}
    .sb-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;margin-bottom:14px;overflow:hidden;}
    .sb-hd{padding:12px 14px;border-bottom:0.5px solid #e2e8f0;font-size:13px;font-weight:600;}
    .sb-body{padding:14px;}
    .contact-btn{width:100%;padding:11px;border:none;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;margin-bottom:8px;display:flex;align-items:center;justify-content:center;gap:8px;}
    .btn-call{background:#f59e0b;color:#1e3a4a;}
    .btn-msg{background:#1e3a4a;color:#fff;}
    .contact-info{display:flex;flex-direction:column;gap:8px;margin-top:10px;}
    .ci{display:flex;align-items:center;gap:8px;font-size:13px;color:#374151;}
    .ci-ic{font-size:16px;}
    .related-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
    .rel-card{background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:8px;padding:10px;}
    .rel-card:hover{border-color:#f59e0b;}
    .rel-img{height:60px;background:#fff;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:24px;margin-bottom:8px;border:0.5px solid #e2e8f0;}
    .rel-t{font-size:12px;font-weight:600;color:#1e293b;line-height:1.3;margin-bottom:4px;}
    .rel-p{font-size:12px;font-weight:700;color:#f59e0b;}
    .safety-box{background:#f0fdf4;border:0.5px solid #bbf7d0;border-radius:8px;padding:12px;font-size:12px;color:#166534;line-height:1.6;}
    .footer{background:#1e3a4a;padding:16px 20px;text-align:center;color:#64748b;font-size:11px;}
    .footer a{color:#94a3b8;}
    @media(max-width:768px){.wrap{grid-template-columns:1fr;}}
  </style>
</head>
<body>

<nav class="nav">
  <a href="/public/" style="display:flex;align-items:center;gap:8px;">
    <div class="logo-box"><svg viewBox="0 0 24 24"><path d="M3 21h18M3 7l9-4 9 4M4 7v14M20 7v14M9 21v-6h6v6"/></svg></div>
    <span class="logo-t">БНБ — Барилгын нэгдсэн бааз</span>
  </a>
  <div class="nav-r">
    <a href="/ads/" class="nb nb-o">← Зарууд</a>
    <a href="/ads/create/" class="nb nb-y">+ Зар оруулах</a>
  </div>
</nav>

<div class="breadcrumb">
  <a href="/public/">Нүүр</a> › <a href="/ads/">Зарууд</a> › {{ ad.title|truncatechars:40 }}
</div>

<div class="wrap">
  <div>
    <div class="card">
      <div class="card-body">
        <div class="img-main">
          {% if ad.image1 %}<img src="{{ ad.image1.url }}" alt="{{ ad.title }}">
          {% elif ad.category == 'house' %}🏠
          {% elif ad.category == 'material' %}🧱
          {% elif ad.category == 'worker' %}👷
          {% elif ad.category == 'repair' %}🔧
          {% elif ad.category == 'design' %}📐
          {% else %}📢{% endif %}
        </div>
        {% if ad.image2 or ad.image3 %}
        <div class="img-thumbs">
          {% if ad.image1 %}<div class="img-thumb"><img src="{{ ad.image1.url }}"></div>{% endif %}
          {% if ad.image2 %}<div class="img-thumb"><img src="{{ ad.image2.url }}"></div>{% endif %}
          {% if ad.image3 %}<div class="img-thumb"><img src="{{ ad.image3.url }}"></div>{% endif %}
        </div>
        {% endif %}
        <span class="ad-cat">{{ ad.get_category_display }}</span>
        <div class="ad-title">{{ ad.title }}</div>
        <div class="ad-price">{{ ad.get_price_display_full }}</div>
        <div class="ad-meta">
          <span>📍 {{ ad.city }}{% if ad.district %}, {{ ad.district }}{% endif %}</span>
          <span>📅 {{ ad.created_at|date:"Y-m-d" }}</span>
          <span>👁 {{ ad.views }} үзсэн</span>
          <span>👤 {{ ad.author.username }}</span>
        </div>
        {% if ad.description %}
        <div class="ad-desc">{{ ad.description|linebreaks }}</div>
        {% endif %}
      </div>
    </div>

    {% if related %}
    <div class="card">
      <div class="card-hd">🔍 Төстэй зарууд</div>
      <div class="card-body">
        <div class="related-grid">
          {% for r in related %}
          <a href="/ads/{{ r.pk }}/" class="rel-card">
            <div class="rel-img">
              {% if r.category == 'house' %}🏠
              {% elif r.category == 'material' %}🧱
              {% elif r.category == 'worker' %}👷
              {% else %}📢{% endif %}
            </div>
            <div class="rel-t">{{ r.title|truncatechars:40 }}</div>
            <div class="rel-p">{{ r.get_price_display_full }}</div>
          </a>
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
        {% if ad.contact_phone %}
        <a href="tel:{{ ad.contact_phone }}" class="contact-btn btn-call">📞 {{ ad.contact_phone }}</a>
        {% endif %}
        {% if ad.contact_email %}
        <a href="mailto:{{ ad.contact_email }}" class="contact-btn btn-msg">✉️ И-мэйл илгээх</a>
        {% endif %}
        <div class="contact-info">
          {% if ad.contact_name %}<div class="ci"><span class="ci-ic">👤</span>{{ ad.contact_name }}</div>{% endif %}
          {% if ad.city %}<div class="ci"><span class="ci-ic">📍</span>{{ ad.city }}</div>{% endif %}
        </div>
      </div>
    </div>

    <div class="sb-card">
      <div class="sb-hd">🛡️ Аюулгүй байдал</div>
      <div class="sb-body">
        <div class="safety-box">
          ✅ Биечлэн уулзаж гэрээ байгуулна уу<br>
          ✅ Урьдчилгаа төлбөр шилжүүлэхгүй байна<br>
          ⚠️ Сэжигтэй зарыг мэдэгдэнэ үү
        </div>
      </div>
    </div>

    <div class="sb-card">
      <div class="sb-hd">🔗 Хуваалцах</div>
      <div class="sb-body">
        <div style="display:flex;gap:8px;">
          <div onclick="navigator.clipboard.writeText(window.location.href);alert('Хуулагдлаа!')" style="flex:1;padding:8px;border:0.5px solid #e2e8f0;border-radius:7px;font-size:12px;text-align:center;cursor:pointer;background:#f8fafc;">📋 Хуулах</div>
          <a href="https://www.facebook.com/sharer/sharer.php?u={{ request.build_absolute_uri }}" target="_blank" style="flex:1;padding:8px;border:0.5px solid #e2e8f0;border-radius:7px;font-size:12px;text-align:center;cursor:pointer;background:#f8fafc;">📘 FB</a>
        </div>
      </div>
    </div>
  </div>
</div>

<footer class="footer">
  <div>© 2026 barilgainfo.mn</div>
  <div style="margin-top:4px;"><a href="/ads/">← Зарууд руу буцах</a></div>
</footer>
</body>
</html>"""

with open("apps/registry/templates/registry/ad_detail.html", "w", encoding="utf-8") as f:
    f.write(template)
print("OK — ad_detail template бэлэн")