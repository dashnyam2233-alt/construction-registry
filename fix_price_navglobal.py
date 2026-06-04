content = open("templates/admin/base_site.html", "r", encoding="utf-8").read()

old = '''{% block nav-global %}
<style>
.price-menu{padding:8px 16px;border-bottom:1px solid #e2e8f0;}
.price-menu a{display:block;padding:6px 8px;color:#1e293b;font-size:13px;text-decoration:none;border-radius:4px;}
.price-menu a:hover{background:#fef3c7;color:#854d0e;}
.price-menu-title{font-size:11px;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:0.05em;padding:8px 8px 4px;}
</style>
{% endblock %}'''

new = '''{% block nav-global %}
<div style="background:#1e3a4a;border-top:1px solid #2d4f63;padding:3px 16px;display:flex;align-items:center;gap:6px;flex-wrap:wrap;">
  <span style="color:#94a3b8;font-size:11px;">💰 Үнэ:</span>
  <a href="/admin/public/materialprice/?category__startswith=mat_" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🧱 Материал</a>
  <a href="/admin/public/materialprice/?category__startswith=labor_" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">👷 Цалин</a>
  <a href="/admin/public/materialprice/?category__startswith=transport_" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🚛 Тээвэр</a>
  <a href="/admin/public/materialprice/?category__startswith=machine_" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🔩 Машин</a>
  <a href="/admin/public/materialprice/?category__startswith=other_" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">📦 Бусад</a>
  <a href="/admin/public/materialprice/add/" style="color:#22c55e;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">+ Нэмэх</a>
</div>
{% endblock %}'''

if old in content:
    content = content.replace(old, new, 1)
    open("templates/admin/base_site.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")