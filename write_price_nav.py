content = open("templates/admin/base_site.html", "r", encoding="utf-8").read()

# Admin nav-д үнийн холбоос нэмэх
old = '{% block footer %}'
new = '''<style>
.price-nav{background:#fff3cd;border-top:2px solid #f59e0b;padding:10px 20px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;}
.price-nav-t{font-size:12px;font-weight:700;color:#854d0e;}
.price-nav a{font-size:12px;color:#1e3a4a;padding:4px 10px;background:#f59e0b;border-radius:6px;font-weight:600;text-decoration:none;}
.price-nav a:hover{background:#e08c00;}
</style>
{% if request.user.is_authenticated %}
<div class="price-nav">
  <span class="price-nav-t">💰 Үнийн мэдээлэл:</span>
  <a href="/admin/public/materialprice/?category=mat_cement">🧱 Материал</a>
  <a href="/admin/public/materialprice/?category=labor_general">👷 Цалин</a>
  <a href="/admin/public/materialprice/?category=transport_material">🚛 Тээвэр</a>
  <a href="/admin/public/materialprice/?category=machine_crane">🔩 Машин</a>
  <a href="/admin/public/materialprice/?category=other_design">📦 Бусад</a>
  <a href="/admin/public/materialprice/">📋 Бүгд үнэ</a>
</div>
{% endif %}

{% block footer %}'''

if old in content:
    content = content.replace(old, new, 1)
    open("templates/admin/base_site.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")