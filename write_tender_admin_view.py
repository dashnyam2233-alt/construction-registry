import os

# Admin-д нэмэх
admin_code = """
from .models import Tender

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "price", "deadline", "is_construction", "created_at")
    list_filter = ("is_construction",)
    search_fields = ("title", "organization", "tender_code")
    ordering = ("-created_at",)
"""

content = open("apps/public/admin.py", "r", encoding="utf-8").read()
if "class TenderAdmin" not in content:
    with open("apps/public/admin.py", "a", encoding="utf-8") as f:
        f.write(admin_code)
    print("OK — TenderAdmin нэмэгдлээ")

# View нэмэх
view_code = '''

def tender_list(request):
    from apps.public.models import Tender
    q = request.GET.get("q", "")
    cat = request.GET.get("cat", "")
    tenders = Tender.objects.order_by("-created_at")
    if q:
        tenders = tenders.filter(title__icontains=q) | tenders.filter(organization__icontains=q)
    if cat == "construction":
        tenders = tenders.filter(is_construction=True)
    return render(request, "registry/tender_list.html", {
        "tenders": tenders[:100],
        "q": q,
        "cat": cat,
        "total": Tender.objects.count(),
        "display_name": get_display_name(request.user),
    })
'''

content = open("apps/registry/views.py", "r", encoding="utf-8").read()
if "def tender_list" not in content:
    with open("apps/registry/views.py", "a", encoding="utf-8") as f:
        f.write(view_code)
    print("OK — tender_list view нэмэгдлээ")

# URL нэмэх
urls = open("apps/registry/urls.py", "r", encoding="utf-8").read()
if "tender_list" not in urls:
    urls = urls.replace(
        "from .views import (",
        "from .views import (\n    tender_list,"
    )
    urls = urls.replace(
        '    path("news/<int:pk>/", news_detail, name="news_detail"),',
        '    path("news/<int:pk>/", news_detail, name="news_detail"),\n    path("tender/", tender_list, name="tender_list"),'
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
  <title>Тендерүүд — БНБ</title>
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
    .hero{background:#1e3a4a;padding:24px 20px;}
    .hero-t{color:#fff;font-size:18px;font-weight:700;margin-bottom:6px;}
    .hero-s{color:#94a3b8;font-size:13px;margin-bottom:14px;}
    .search-box{max-width:600px;background:#fff;border-radius:10px;padding:5px;display:flex;gap:6px;}
    .search-inp{flex:1;padding:8px 14px;border:none;outline:none;font-size:13px;border-radius:7px;}
    .search-btn{padding:8px 16px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:7px;font-size:13px;font-weight:700;cursor:pointer;}
    .cats{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:0 20px;display:flex;gap:0;}
    .cat{padding:10px 16px;font-size:13px;color:#64748b;border-bottom:2px solid transparent;cursor:pointer;white-space:nowrap;}
    .cat:hover{color:#1e3a4a;}
    .cat.on{color:#1e3a4a;border-bottom-color:#f59e0b;font-weight:600;}
    .wrap{max-width:1000px;margin:16px auto;padding:0 20px;}
    .top-bar{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
    .top-t{font-size:14px;font-weight:600;color:#1e293b;}
    .tender-list{display:flex;flex-direction:column;gap:10px;}
    .tender-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;padding:16px;display:flex;gap:16px;align-items:flex-start;}
    .tender-card:hover{border-color:#f59e0b;}
    .tender-date{background:#1e3a4a;color:#fff;border-radius:8px;padding:8px;text-align:center;min-width:52px;flex-shrink:0;}
    .date-m{font-size:10px;color:#94a3b8;}
    .date-d{font-size:20px;font-weight:700;line-height:1;}
    .date-t{font-size:10px;color:#f59e0b;margin-top:2px;}
    .tender-body{flex:1;}
    .tender-tag{display:inline-block;background:#f0fdf4;color:#166534;font-size:10px;padding:1px 7px;border-radius:20px;margin-bottom:5px;}
    .tender-tag.blue{background:#eff6ff;color:#1d4ed8;}
    .tender-title{font-size:14px;font-weight:600;color:#1e293b;margin-bottom:5px;line-height:1.4;}
    .tender-org{font-size:12px;color:#64748b;margin-bottom:6px;}
    .tender-meta{display:flex;gap:12px;flex-wrap:wrap;}
    .tender-meta span{font-size:11px;color:#94a3b8;display:flex;align-items:center;gap:3px;}
    .tender-price{font-size:14px;font-weight:700;color:#f59e0b;margin-left:auto;white-space:nowrap;}
    .badge-c{background:#fef3c7;color:#854d0e;font-size:10px;padding:2px 7px;border-radius:20px;}
    .empty{text-align:center;padding:40px;color:#94a3b8;background:#fff;border-radius:10px;border:0.5px dashed #e2e8f0;}
    .footer{background:#1e3a4a;padding:16px 20px;text-align:center;color:#64748b;font-size:11px;margin-top:20px;}
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
    <a href="/ads/" class="nb nb-o">Зарууд</a>
    {% if user.is_authenticated %}
    <form method="post" action="/logout/" style="display:inline;">{% csrf_token %}<button type="submit" class="nb nb-o">Гарах</button></form>
    {% else %}
    <a href="/login/" class="nb nb-y">Нэвтрэх</a>
    {% endif %}
  </div>
</nav>

<div class="hero">
  <div class="hero-t">📋 Тендерүүд</div>
  <div class="hero-s">Нийт {{ total }} тендер бүртгэлтэй · tender.gov.mn-аас татсан</div>
  <form method="get" action="/tender/" class="search-box">
    <input class="search-inp" name="q" placeholder="Тендер хайх... (нэр, байгууллага)" value="{{ q }}">
    <button type="submit" class="search-btn">🔍 Хайх</button>
  </form>
</div>

<div class="cats">
  <a href="/tender/" class="cat {% if not cat %}on{% endif %}">📋 Бүгд ({{ total }})</a>
  <a href="/tender/?cat=construction" class="cat {% if cat == 'construction' %}on{% endif %}">🏗 Барилга</a>
</div>

<div class="wrap">
  <div class="top-bar">
    <div class="top-t">{{ tenders|length }} тендер харагдаж байна</div>
    <a href="https://tender.gov.mn" target="_blank" style="font-size:12px;color:#2f6477;">tender.gov.mn →</a>
  </div>

  {% if tenders %}
  <div class="tender-list">
    {% for t in tenders %}
    <a href="{{ t.url }}" target="_blank" class="tender-card">
      <div class="tender-date">
        <div class="date-m">{{ t.deadline|slice:":7" }}</div>
        <div class="date-d">{{ t.deadline|slice:"8:10" }}</div>
        <div class="date-t">Хугацаа</div>
      </div>
      <div class="tender-body">
        {% if t.is_construction %}
        <span class="tender-tag">🏗 Барилга</span>
        {% else %}
        <span class="tender-tag blue">📋 Тендер</span>
        {% endif %}
        <div class="tender-title">{{ t.title }}</div>
        <div class="tender-org">🏛 {{ t.organization }}</div>
        <div class="tender-meta">
          {% if t.method %}<span>📜 {{ t.method|truncatechars:40 }}</span>{% endif %}
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
  </div>
  {% endif %}
</div>

<footer class="footer">
  <div>© 2026 barilgainfo.mn · Тендерийн мэдээлэл tender.gov.mn-аас татагдсан</div>
</footer>
</body>
</html>"""

os.makedirs("apps/registry/templates/registry", exist_ok=True)
with open("apps/registry/templates/registry/tender_list.html", "w", encoding="utf-8") as f:
    f.write(template)
print("OK — template бэлэн")