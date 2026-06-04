content = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").read()

# Dropdown сонголтуудыг шинэчлэх
old_select = """      <option value="material" {% if category == "material" %}selected{% endif %}>🧱 Материал</option>
      <option value="house" {% if category == "house" %}selected{% endif %}>🏠 Орон сууц</option>
      <option value="worker" {% if category == "worker" %}selected{% endif %}>👷 Ажилтан</option>
      <option value="repair" {% if category == "repair" %}selected{% endif %}>🔧 Засвар</option>
      <option value="design" {% if category == "design" %}selected{% endif %}>📐 Зураг төсөл</option>
      <option value="other" {% if category == "other" %}selected{% endif %}>📦 Бусад</option>"""

new_select = """      <option value="material" {% if category == "material" %}selected{% endif %}>🧱 Материал</option>
      <option value="equipment" {% if category == "equipment" %}selected{% endif %}>🔩 Тоног төхөөрөмж</option>
      <option value="rental" {% if category == "rental" %}selected{% endif %}>🔑 Түрээс</option>
      <option value="realestate" {% if category == "realestate" %}selected{% endif %}>🏠 Үл хөдлөх хөрөнгө</option>
      <option value="service" {% if category == "service" %}selected{% endif %}>🏗 Барилгын үйлчилгээ</option>
      <option value="design" {% if category == "design" %}selected{% endif %}>📐 Зураг төсөв, дизайн</option>
      <option value="worker" {% if category == "worker" %}selected{% endif %}>👷 Ажилтан, ажлын зар</option>
      <option value="tender" {% if category == "tender" %}selected{% endif %}>📋 Тендер, төсөл</option>
      <option value="company" {% if category == "company" %}selected{% endif %}>🏢 Компаниуд</option>
      <option value="other" {% if category == "other" %}selected{% endif %}>📦 Бусад</option>"""

# Cats tab шинэчлэх
old_cats = """<div class="cats">
  <a href="/ads/" class="cat {% if not category %}on{% endif %}">🏠 Бүгд</a>
  <a href="/ads/?cat=material" class="cat {% if category == "material" %}on{% endif %}">🧱 Материал</a>
  <a href="/ads/?cat=house" class="cat {% if category == "house" %}on{% endif %}">🏠 Орон сууц</a>
  <a href="/ads/?cat=worker" class="cat {% if category == "worker" %}on{% endif %}">👷 Ажилтан</a>
  <a href="/ads/?cat=repair" class="cat {% if category == "repair" %}on{% endif %}">🔧 Засвар</a>
  <a href="/ads/?cat=design" class="cat {% if category == "design" %}on{% endif %}">📐 Зураг төсөл</a>
  <a href="/ads/?cat=other" class="cat {% if category == "other" %}on{% endif %}">📦 Бусад</a>
</div>"""

new_cats = """<div class="cats">
  <a href="/ads/" class="cat {% if not category %}on{% endif %}">🏠 Бүгд</a>
  <a href="/ads/?cat=material" class="cat {% if category == "material" %}on{% endif %}">🧱 Материал</a>
  <a href="/ads/?cat=equipment" class="cat {% if category == "equipment" %}on{% endif %}">🔩 Тоног</a>
  <a href="/ads/?cat=rental" class="cat {% if category == "rental" %}on{% endif %}">🔑 Түрээс</a>
  <a href="/ads/?cat=realestate" class="cat {% if category == "realestate" %}on{% endif %}">🏠 Үл хөдлөх</a>
  <a href="/ads/?cat=service" class="cat {% if category == "service" %}on{% endif %}">🏗 Үйлчилгээ</a>
  <a href="/ads/?cat=design" class="cat {% if category == "design" %}on{% endif %}">📐 Зураг</a>
  <a href="/ads/?cat=worker" class="cat {% if category == "worker" %}on{% endif %}">👷 Ажилтан</a>
  <a href="/ads/?cat=tender" class="cat {% if category == "tender" %}on{% endif %}">📋 Тендер</a>
  <a href="/ads/?cat=company" class="cat {% if category == "company" %}on{% endif %}">🏢 Компани</a>
  <a href="/ads/?cat=other" class="cat {% if category == "other" %}on{% endif %}">📦 Бусад</a>
</div>"""

# Sidebar-д бусад ангиллуудыг нэмэх
old_other_sb = """    {% else %}
    <div class="sb-card">
      <div class="sb-hd">📂 Ангилалууд</div>
      <div class="sb-body">
        <a href="/ads/?cat=material" class="subcat-link">🧱 Материал</a>
        <a href="/ads/?cat=house" class="subcat-link">🏠 Орон сууц</a>
        <a href="/ads/?cat=worker" class="subcat-link">👷 Ажилтан</a>
        <a href="/ads/?cat=repair" class="subcat-link">🔧 Засвар</a>
        <a href="/ads/?cat=design" class="subcat-link">📐 Зураг төсөл</a>
        <a href="/ads/?cat=other" class="subcat-link">📦 Бусад</a>
      </div>
    </div>
    {% endif %}"""

new_other_sb = """    {% else %}
    <div class="sb-card">
      <div class="sb-hd">📂 Ангилалууд</div>
      <div class="sb-body">
        <a href="/ads/?cat=material" class="subcat-link {% if category == "material" %}on{% endif %}">🧱 Материал</a>
        <a href="/ads/?cat=equipment" class="subcat-link {% if category == "equipment" %}on{% endif %}">🔩 Тоног төхөөрөмж</a>
        <a href="/ads/?cat=rental" class="subcat-link {% if category == "rental" %}on{% endif %}">🔑 Түрээс</a>
        <a href="/ads/?cat=realestate" class="subcat-link {% if category == "realestate" %}on{% endif %}">🏠 Үл хөдлөх хөрөнгө</a>
        <a href="/ads/?cat=service" class="subcat-link {% if category == "service" %}on{% endif %}">🏗 Барилгын үйлчилгээ</a>
        <a href="/ads/?cat=design" class="subcat-link {% if category == "design" %}on{% endif %}">📐 Зураг төсөв</a>
        <a href="/ads/?cat=worker" class="subcat-link {% if category == "worker" %}on{% endif %}">👷 Ажилтан</a>
        <a href="/ads/?cat=tender" class="subcat-link {% if category == "tender" %}on{% endif %}">📋 Тендер</a>
        <a href="/ads/?cat=company" class="subcat-link {% if category == "company" %}on{% endif %}">🏢 Компаниуд</a>
        <a href="/ads/?cat=other" class="subcat-link {% if category == "other" %}on{% endif %}">📦 Бусад</a>
      </div>
    </div>
    {% endif %}"""

changed = False
if old_select in content:
    content = content.replace(old_select, new_select, 1)
    changed = True
    print("OK — dropdown шинэчлэгдлээ")
else:
    print("NOT FOUND — dropdown")

if old_cats in content:
    content = content.replace(old_cats, new_cats, 1)
    changed = True
    print("OK — cats tab шинэчлэгдлээ")
else:
    print("NOT FOUND — cats tab")

if old_other_sb in content:
    content = content.replace(old_other_sb, new_other_sb, 1)
    changed = True
    print("OK — sidebar шинэчлэгдлээ")
else:
    print("NOT FOUND — sidebar")

if changed:
    open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(content)