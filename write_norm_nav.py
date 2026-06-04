path = r"templates\admin\base_site.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '{% block footer %}\n  {{ block.super }}\n{% endblock %}'

new = '''{% block footer %}
  {{ block.super }}
{% endblock %}

<style>
.norm-nav-bar {
  background: #1a3a4a;
  border-top: 1px solid #2d5a6a;
  padding: 6px 20px;
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 9999;
}
.norm-nav-bar a {
  color: #a0d4e8;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 4px;
  text-decoration: none;
  border: 1px solid #2d5a6a;
}
.norm-nav-bar a:hover {
  background: #f59e0b;
  color: #1e3a4a;
  border-color: #f59e0b;
}
.norm-nav-bar .nav-label {
  color: #64a0b4;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
}
</style>

<div class="norm-nav-bar">
  <span class="nav-label">📐 Норм:</span>
  <a href="/admin/public/materialnorm/?building_type=low_rise">🏡 Амины</a>
  <a href="/admin/public/materialnorm/?building_type=mid_rise">🏢 Олон айлын</a>
  <a href="/admin/public/materialnorm/?building_type=high_rise">🏙 Өндөр давхар</a>
  <a href="/admin/public/materialnorm/?building_type=office">🏢 Оффис</a>
  <a href="/admin/public/materialnorm/?building_type=warehouse">🏭 Агуулах</a>
  <a href="/admin/public/materialnorm/">📋 Бүгд</a>
  <a href="/admin/public/materialnorm/add/" style="background:#22c55e;color:#fff;border-color:#22c55e;">➕ Нэмэх</a>
</div>'''

if old in content:
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("OK")
else:
    print("NOT FOUND")
    print(repr(content[-100:]))