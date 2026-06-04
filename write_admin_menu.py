content = open("templates/admin/base_site.html", "r", encoding="utf-8").read()

# Зүүн sidebar-д үнийн цэс нэмэх — nav дотор
old = '{% block extrastyle %}'
new = '''{% block nav-global %}
<style>
.price-menu{padding:8px 16px;border-bottom:1px solid #e2e8f0;}
.price-menu a{display:block;padding:6px 8px;color:#1e293b;font-size:13px;text-decoration:none;border-radius:4px;}
.price-menu a:hover{background:#fef3c7;color:#854d0e;}
.price-menu-title{font-size:11px;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:0.05em;padding:8px 8px 4px;}
</style>
{% endblock %}

{% block extrastyle %}'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK 1")
else:
    print("NOT FOUND 1")

# App list-д нэмэх — index.html засах
index = open("templates/admin/index.html", "r", encoding="utf-8").read()
print("\nindex.html агуулга:")
print(index[:500])

open("templates/admin/base_site.html", "w", encoding="utf-8").write(content)