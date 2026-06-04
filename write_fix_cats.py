content = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").read()

old = """<div class="cats">
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

new = """<div class="cats">
  <a href="/ads/" class="cat {% if not category %}on{% endif %}">🏠 Бүгд зар</a>
  <a href="/ads/?cat=material" class="cat {% if category == "material" %}on{% endif %}">🧱 Материал</a>
  <a href="/ads/?cat=equipment" class="cat {% if category == "equipment" %}on{% endif %}">🔩 Тоног төхөөрөмж</a>
  <a href="/ads/?cat=rental" class="cat {% if category == "rental" %}on{% endif %}">🔑 Түрээс</a>
  <a href="/ads/?cat=realestate" class="cat {% if category == "realestate" %}on{% endif %}">🏠 Үл хөдлөх хөрөнгө</a>
  <a href="/ads/?cat=service" class="cat {% if category == "service" %}on{% endif %}">🏗 Барилгын үйлчилгээ</a>
  <a href="/ads/?cat=design" class="cat {% if category == "design" %}on{% endif %}">📐 Зураг төсөв, дизайн</a>
  <a href="/ads/?cat=worker" class="cat {% if category == "worker" %}on{% endif %}">👷 Ажилтан, ажлын зар</a>
  <a href="/ads/?cat=tender" class="cat {% if category == "tender" %}on{% endif %}">📋 Тендер, төсөл</a>
  <a href="/ads/?cat=company" class="cat {% if category == "company" %}on{% endif %}">🏢 Компаниуд</a>
  <a href="/ads/?cat=other" class="cat {% if category == "other" %}on{% endif %}">📦 Бусад</a>
</div>"""

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")