# View нэмэх
view_code = '''

def news_list(request):
    from apps.public.models import PublicPost
    q = request.GET.get("q", "")
    posts = PublicPost.objects.filter(is_published=True).select_related("author").order_by("-created_at")
    if q:
        posts = posts.filter(title__icontains=q)
    return render(request, "registry/news_list.html", {
        "posts": posts[:50],
        "q": q,
        "display_name": get_display_name(request.user),
    })

def news_detail(request, pk):
    from apps.public.models import PublicPost
    post = PublicPost.objects.filter(pk=pk, is_published=True).select_related("author").first()
    if not post:
        from django.http import Http404
        raise Http404
    related = PublicPost.objects.filter(is_published=True).exclude(pk=pk).order_by("-created_at")[:4]
    return render(request, "registry/news_detail.html", {
        "post": post,
        "related": related,
        "display_name": get_display_name(request.user),
    })
'''

content = open("apps/registry/views.py", "r", encoding="utf-8").read()
if "def news_list" not in content:
    with open("apps/registry/views.py", "a", encoding="utf-8") as f:
        f.write(view_code)
    print("OK — news views нэмэгдлээ")

# URL нэмэх
urls = open("apps/registry/urls.py", "r", encoding="utf-8").read()
if "news_list" not in urls:
    urls = urls.replace(
        "from .views import (",
        "from .views import (\n    news_list,\n    news_detail,"
    )
    urls = urls.replace(
        '    path("ads/<int:pk>/", ad_detail, name="ad_detail"),',
        '    path("ads/<int:pk>/", ad_detail, name="ad_detail"),\n    path("news/", news_list, name="news_list"),\n    path("news/<int:pk>/", news_detail, name="news_detail"),'
    )
    open("apps/registry/urls.py", "w", encoding="utf-8").write(urls)
    print("OK — URLs нэмэгдлээ")

# Templates
import os

news_list_html = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Мэдээ — БНБ</title>
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
    .hero-t{color:#fff;font-size:18px;font-weight:700;margin-bottom:12px;}
    .search-box{max-width:500px;background:#fff;border-radius:10px;padding:5px;display:flex;gap:6px;}
    .search-inp{flex:1;padding:8px 14px;border:none;outline:none;font-size:13px;border-radius:7px;}
    .search-btn{padding:8px 16px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:7px;font-size:13px;font-weight:700;cursor:pointer;}
    .wrap{max-width:960px;margin:20px auto;padding:0 20px;display:grid;grid-template-columns:1fr 260px;gap:16px;}
    .news-list{display:flex;flex-direction:column;gap:12px;}
    .news-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;padding:16px;display:flex;gap:14px;}
    .news-card:hover{border-color:#2f6477;}
    .news-img{width:80px;height:80px;border-radius:8px;background:#dbeafe;display:flex;align-items:center;justify-content:center;font-size:32px;flex-shrink:0;}
    .news-tag{display:inline-block;background:#eff6ff;color:#1d4ed8;font-size:10px;padding:1px 7px;border-radius:20px;margin-bottom:4px;}
    .news-t{font-size:14px;font-weight:600;color:#1e293b;line-height:1.4;margin-bottom:6px;}
    .news-body{font-size:12px;color:#64748b;line-height:1.5;margin-bottom:6px;}
    .news-m{font-size:11px;color:#94a3b8;display:flex;gap:10px;}
    .sb-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:9px;margin-bottom:12px;overflow:hidden;}
    .sb-hd{padding:10px 14px;border-bottom:0.5px solid #e2e8f0;font-size:13px;font-weight:600;}
    .sb-body{padding:12px 14px;}
    .hot-item{display:flex;gap:8px;padding:6px 0;border-bottom:0.5px solid #f1f5f9;}
    .hot-item:last-child{border-bottom:none;}
    .hot-n{width:18px;height:18px;background:#1e3a4a;color:#f59e0b;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:700;flex-shrink:0;margin-top:2px;}
    .hot-t{font-size:12px;color:#374151;line-height:1.4;}
    .hot-m{font-size:10px;color:#94a3b8;margin-top:1px;}
    .empty{text-align:center;padding:32px;color:#94a3b8;font-size:13px;background:#fff;border-radius:10px;border:0.5px dashed #e2e8f0;}
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
    <a href="/public/" class="nb nb-o">Нүүр</a>
    <a href="/ads/" class="nb nb-o">Зарууд</a>
  </div>
</nav>
<div class="hero">
  <div class="hero-t">📰 Барилгын мэдээ</div>
  <form method="get" action="/news/" class="search-box">
    <input class="search-inp" name="q" placeholder="Мэдээ хайх..." value="{{ q }}">
    <button type="submit" class="search-btn">Хайх</button>
  </form>
</div>
<div class="wrap">
  <div>
    {% if posts %}
    <div class="news-list">
      {% for post in posts %}
      <a href="/news/{{ post.pk }}/" class="news-card">
        <div class="news-img">📰</div>
        <div>
          <span class="news-tag">Мэдээ</span>
          <div class="news-t">{{ post.title }}</div>
          <div class="news-body">{{ post.body|truncatechars:120 }}</div>
          <div class="news-m">
            <span>📅 {{ post.created_at|date:"Y-m-d" }}</span>
            <span>👤 {{ post.author.username|default:"" }}</span>
          </div>
        </div>
      </a>
      {% endfor %}
    </div>
    {% else %}
    <div class="empty">
      <div style="font-size:36px;margin-bottom:10px;">📭</div>
      <div>Одоогоор мэдээ байхгүй байна.</div>
    </div>
    {% endif %}
  </div>
  <div>
    <div class="sb-card">
      <div class="sb-hd">🔥 Сүүлийн мэдээ</div>
      <div class="sb-body">
        {% for post in posts|slice:":5" %}
        <a href="/news/{{ post.pk }}/" class="hot-item" style="display:flex;">
          <div class="hot-n">{{ forloop.counter }}</div>
          <div><div class="hot-t">{{ post.title|truncatechars:45 }}</div><div class="hot-m">{{ post.created_at|date:"Y-m-d" }}</div></div>
        </a>
        {% endfor %}
      </div>
    </div>
    <div class="sb-card">
      <div class="sb-hd">⚡ Хурдан хандах</div>
      <div class="sb-body" style="display:flex;flex-direction:column;gap:4px;">
        <a href="/public/" style="display:flex;align-items:center;gap:8px;padding:8px 10px;background:#f8fafc;border-radius:7px;font-size:12px;color:#374151;">🏠 Нүүр</a>
        <a href="/ads/" style="display:flex;align-items:center;gap:8px;padding:8px 10px;background:#f8fafc;border-radius:7px;font-size:12px;color:#374151;">📢 Зарууд</a>
        <a href="/public/?tab=companies" style="display:flex;align-items:center;gap:8px;padding:8px 10px;background:#f8fafc;border-radius:7px;font-size:12px;color:#374151;">🏢 Компаниуд</a>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

news_detail_html = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ post.title }} — БНБ</title>
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
    .breadcrumb{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:10px 20px;font-size:12px;color:#64748b;}
    .breadcrumb a{color:#2f6477;}
    .wrap{max-width:960px;margin:20px auto;padding:0 20px;display:grid;grid-template-columns:1fr 260px;gap:16px;}
    .card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;overflow:hidden;margin-bottom:14px;}
    .card-body{padding:20px;}
    .post-tag{display:inline-block;background:#eff6ff;color:#1d4ed8;font-size:11px;padding:2px 10px;border-radius:20px;margin-bottom:10px;}
    .post-title{font-size:22px;font-weight:700;color:#1e293b;line-height:1.35;margin-bottom:12px;}
    .post-meta{display:flex;gap:16px;margin-bottom:16px;padding-bottom:16px;border-bottom:0.5px solid #e2e8f0;}
    .post-meta span{font-size:12px;color:#64748b;}
    .post-body{font-size:14px;color:#374151;line-height:1.8;}
    .sb-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:9px;margin-bottom:12px;overflow:hidden;}
    .sb-hd{padding:10px 14px;border-bottom:0.5px solid #e2e8f0;font-size:13px;font-weight:600;}
    .sb-body{padding:12px 14px;}
    .rel-item{padding:8px 0;border-bottom:0.5px solid #f1f5f9;display:flex;gap:8px;}
    .rel-item:last-child{border-bottom:none;}
    .rel-dot{width:6px;height:6px;background:#f59e0b;border-radius:50%;margin-top:5px;flex-shrink:0;}
    .rel-t{font-size:12px;color:#374151;line-height:1.4;}
    .rel-m{font-size:10px;color:#94a3b8;margin-top:1px;}
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
    <a href="/news/" class="nb nb-o">← Мэдээнүүд</a>
  </div>
</nav>
<div class="breadcrumb">
  <a href="/public/">Нүүр</a> › <a href="/news/">Мэдээ</a> › {{ post.title|truncatechars:40 }}
</div>
<div class="wrap">
  <div>
    <div class="card">
      <div class="card-body">
        <span class="post-tag">📰 Мэдээ</span>
        <div class="post-title">{{ post.title }}</div>
        <div class="post-meta">
          <span>📅 {{ post.created_at|date:"Y-m-d H:i" }}</span>
          <span>👤 {{ post.author.username|default:"" }}</span>
        </div>
        <div class="post-body">{{ post.body|linebreaks }}</div>
      </div>
    </div>
  </div>
  <div>
    {% if related %}
    <div class="sb-card">
      <div class="sb-hd">📰 Бусад мэдээ</div>
      <div class="sb-body">
        {% for r in related %}
        <a href="/news/{{ r.pk }}/" class="rel-item" style="display:flex;">
          <div class="rel-dot"></div>
          <div><div class="rel-t">{{ r.title|truncatechars:50 }}</div><div class="rel-m">{{ r.created_at|date:"Y-m-d" }}</div></div>
        </a>
        {% endfor %}
      </div>
    </div>
    {% endif %}
    <div class="sb-card">
      <div class="sb-hd">⚡ Хурдан хандах</div>
      <div class="sb-body" style="display:flex;flex-direction:column;gap:4px;">
        <a href="/public/" style="display:flex;align-items:center;gap:8px;padding:8px 10px;background:#f8fafc;border-radius:7px;font-size:12px;color:#374151;">🏠 Нүүр</a>
        <a href="/ads/" style="display:flex;align-items:center;gap:8px;padding:8px 10px;background:#f8fafc;border-radius:7px;font-size:12px;color:#374151;">📢 Зарууд</a>
        <a href="/public/?tab=companies" style="display:flex;align-items:center;gap:8px;padding:8px 10px;background:#f8fafc;border-radius:7px;font-size:12px;color:#374151;">🏢 Компаниуд</a>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

os.makedirs("apps/registry/templates/registry", exist_ok=True)
with open("apps/registry/templates/registry/news_list.html", "w", encoding="utf-8") as f:
    f.write(news_list_html)
with open("apps/registry/templates/registry/news_detail.html", "w", encoding="utf-8") as f:
    f.write(news_detail_html)
print("OK — templates бэлэн")