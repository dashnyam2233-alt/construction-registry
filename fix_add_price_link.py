content = open("templates/admin/base_site.html", "r", encoding="utf-8").read()

# Nav bar-д үнийн холбоос нэмэх
old = '{% block nav-global %}{% endblock %}'
new = '''{% block nav-global %}{% endblock %}
<style>
.price-quicklink{background:#f59e0b;padding:4px 10px;border-radius:4px;color:#1e3a4a!important;font-size:12px;font-weight:700;margin-left:8px;}
.price-quicklink:hover{background:#e08c00;}
</style>'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK 1")
else:
    # Өөр хэсэгт нэмэх
    old2 = '</nav>'
    new2 = '''<div style="background:#1e3a4a;padding:4px 20px;border-top:1px solid #2d4f63;display:flex;gap:8px;flex-wrap:wrap;">
  <span style="color:#94a3b8;font-size:11px;line-height:28px;">💰 Үнэ:</span>
  <a href="/admin/public/materialprice/?category__startswith=mat_" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🧱 Материал</a>
  <a href="/admin/public/materialprice/?category__startswith=labor_" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">👷 Цалин</a>
  <a href="/admin/public/materialprice/?category__startswith=transport_" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🚛 Тээвэр</a>
  <a href="/admin/public/materialprice/?category__startswith=machine_" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🔩 Машин</a>
  <a href="/admin/public/materialprice/?category__startswith=other_" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">📦 Бусад</a>
  <a href="/admin/public/materialprice/add/" style="color:#22c55e;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">+ Нэмэх</a>
</div>
</nav>'''
    if '</nav>' in content:
        content = content.replace('</nav>', new2, 1)
        print("OK 2 — nav-д нэмэгдлээ")
    else:
        print("NOT FOUND")

open("templates/admin/base_site.html", "w", encoding="utf-8").write(content)