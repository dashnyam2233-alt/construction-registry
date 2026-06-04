# View нэмэх
view_code = '''

def ad_delete(request, pk):
    from apps.public.models import Ad
    if not request.user.is_authenticated:
        return redirect("/login/")
    ad = Ad.objects.filter(pk=pk, author=request.user).first()
    if not ad:
        from django.http import Http404
        raise Http404
    if request.method == "POST":
        ad.delete()
        return redirect("/profile/")
    return render(request, "registry/ad_delete_confirm.html", {"ad": ad})
'''

content = open("apps/registry/views.py", "r", encoding="utf-8").read()
if "def ad_delete" not in content:
    with open("apps/registry/views.py", "a", encoding="utf-8") as f:
        f.write(view_code)
    print("OK — view нэмэгдлээ")

# URL нэмэх
urls = open("apps/registry/urls.py", "r", encoding="utf-8").read()
if "ad_delete" not in urls:
    urls = urls.replace(
        "from .views import (",
        "from .views import (\n    ad_delete,"
    )
    urls = urls.replace(
        '    path("news/<int:pk>/", news_detail, name="news_detail"),',
        '    path("news/<int:pk>/", news_detail, name="news_detail"),\n    path("ads/<int:pk>/delete/", ad_delete, name="ad_delete"),'
    )
    open("apps/registry/urls.py", "w", encoding="utf-8").write(urls)
    print("OK — URL нэмэгдлээ")

# Template
template = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <title>Зар устгах — БНБ</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f1f5f9;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px;}
    .card{width:min(440px,94vw);background:#fff;border:0.5px solid #e2e8f0;border-radius:12px;padding:28px;text-align:center;}
    .ic{font-size:48px;margin-bottom:14px;}
    h2{font-size:18px;font-weight:700;color:#1e293b;margin-bottom:8px;}
    .ad-name{background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:8px;padding:12px;margin:14px 0;font-size:14px;font-weight:600;color:#1e293b;}
    p{font-size:13px;color:#64748b;margin-bottom:20px;}
    .btns{display:flex;gap:10px;justify-content:center;}
    .btn-cancel{padding:10px 20px;background:#f1f5f9;color:#374151;border:none;border-radius:8px;font-size:14px;cursor:pointer;text-decoration:none;}
    .btn-delete{padding:10px 20px;background:#e53e3e;color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;}
  </style>
</head>
<body>
  <div class="card">
    <div class="ic">🗑️</div>
    <h2>Зар устгах уу?</h2>
    <div class="ad-name">{{ ad.title }}</div>
    <p>Устгасны дараа сэргээх боломжгүй.</p>
    <div class="btns">
      <a href="/profile/" class="btn-cancel">Болих</a>
      <form method="post" style="display:inline;">
        {% csrf_token %}
        <button type="submit" class="btn-delete">Устгах</button>
      </form>
    </div>
  </div>
</body>
</html>"""

with open("apps/registry/templates/registry/ad_delete_confirm.html", "w", encoding="utf-8") as f:
    f.write(template)
print("OK — template бэлэн")