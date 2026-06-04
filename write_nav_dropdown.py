path = r"templates\admin\base_site.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Бүх nav-global блокийг олж бүрэн солих
nav_start = content.find('{% block nav-global %}')
nav_end = content.find('{% endblock %}', nav_start) + len('{% endblock %}')

new_nav = '''{% block nav-global %}
<style>
.admin-top-nav {
  background: #1e3a4a;
  border-top: 1px solid #2d4f63;
  padding: 4px 16px;
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
  position: relative;
  z-index: 9999;
}
.admin-top-nav .nav-label {
  color: #94a3b8;
  font-size: 11px;
  font-weight: 700;
}
.dropdown {
  position: relative;
  display: inline-block;
}
.dropdown-btn {
  color: #f59e0b;
  font-size: 11px;
  padding: 3px 10px;
  border-radius: 4px;
  background: #2d4f63;
  text-decoration: none;
  border: none;
  cursor: pointer;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 4px;
}
.dropdown-btn:hover {
  background: #f59e0b;
  color: #1e3a4a;
}
.dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background: #1e3a4a;
  border: 1px solid #2d4f63;
  border-radius: 6px;
  min-width: 180px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  z-index: 99999;
  padding: 4px 0;
}
.dropdown:hover .dropdown-menu {
  display: block;
}
.dropdown-menu a {
  display: block;
  color: #cbd5e1;
  font-size: 12px;
  padding: 6px 14px;
  text-decoration: none;
  white-space: nowrap;
}
.dropdown-menu a:hover {
  background: #f59e0b;
  color: #1e3a4a;
}
.dropdown-menu .divider {
  border-top: 1px solid #2d4f63;
  margin: 3px 0;
}
</style>

<div class="admin-top-nav">
  <span class="nav-label">⚙️ ADMIN:</span>

  <!-- Үнэ dropdown -->
  <div class="dropdown">
    <button class="dropdown-btn">💰 Үнэ ▾</button>
    <div class="dropdown-menu">
      <a href="/admin/public/materialprice/?category__startswith=mat_">🧱 Материал</a>
      <a href="/admin/public/materialprice/?category__startswith=labor_">👷 Цалин</a>
      <a href="/admin/public/materialprice/?category__startswith=transport_">🚛 Тээвэр</a>
      <a href="/admin/public/materialprice/?category__startswith=machine_">🏗 Машин</a>
      <a href="/admin/public/materialprice/?category__startswith=other_">📦 Бусад</a>
      <div class="divider"></div>
      <a href="/admin/public/materialprice/">📋 Бүгд</a>
      <a href="/admin/public/materialprice/add/">➕ Үнэ нэмэх</a>
    </div>
  </div>

  <!-- Норм dropdown -->
  <div class="dropdown">
    <button class="dropdown-btn">📐 Норм ▾</button>
    <div class="dropdown-menu">
      <a href="/admin/public/materialnorm/?building_type=low_rise">🏡 Амины (1-2 давхар)</a>
      <a href="/admin/public/materialnorm/?building_type=mid_rise">🏢 Олон айлын (3-9 давхар)</a>
      <a href="/admin/public/materialnorm/?building_type=high_rise">🏙 Өндөр давхар (10+)</a>
      <a href="/admin/public/materialnorm/?building_type=office">🏢 Оффис</a>
      <a href="/admin/public/materialnorm/?building_type=warehouse">🏭 Агуулах</a>
      <div class="divider"></div>
      <a href="/admin/public/materialnorm/">📋 Бүгд</a>
      <a href="/admin/public/materialnorm/add/">➕ Норм нэмэх</a>
    </div>
  </div>

  <!-- Бусад товчнууд -->
  <a href="/admin/" style="color:#94a3b8;font-size:11px;padding:3px 10px;border-radius:4px;background:#2d4f63;text-decoration:none;">🏠 Нүүр</a>
  <a href="/public/" style="color:#94a3b8;font-size:11px;padding:3px 10px;border-radius:4px;background:#2d4f63;text-decoration:none;">🌐 Сайт</a>
</div>
{% endblock %}'''

if nav_start >= 0 and nav_end >= 0:
    content = content[:nav_start] + new_nav + content[nav_end:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("OK - dropdown nav хийгдлээ")
else:
    print(f"NOT FOUND: start={nav_start}, end={nav_end}")