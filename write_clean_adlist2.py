content = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").read()

# Буруу select хэсгийг зөв болгох
old = '''<select class="search-sel" name="cat" onchange="this.form.submit()">
      <option value="">📂 Бүх ангилал</option>
      <option value="material"'''

new = '''<select class="search-sel" name="cat" onchange="this.form.submit()">
      <option value="">📂 Бүх ангилал</option>
      <option value="material" {% if category == "material" %}selected{% endif %}>🧱 Материал</option>
      <option value="equipment" {% if category == "equipment" %}selected{% endif %}>🔩 Тоног төхөөрөмж</option>
      <option value="rental" {% if category == "rental" %}selected{% endif %}>🔑 Түрээс</option>
      <option value="realestate" {% if category == "realestate" %}selected{% endif %}>🏠 Үл хөдлөх хөрөнгө</option>
      <option value="service" {% if category == "service" %}selected{% endif %}>🏗 Барилгын үйлчилгээ</option>
      <option value="design" {% if category == "design" %}selected{% endif %}>📐 Зураг төсөв, дизайн</option>
      <option value="worker" {% if category == "worker" %}selected{% endif %}>👷 Ажилтан, ажлын зар</option>
      <option value="tender" {% if category == "tender" %}selected{% endif %}>📋 Тендер, төсөл</option>
      <option value="company" {% if category == "company" %}selected{% endif %}>🏢 Компаниуд</option>
      <option value="other" {% if category == "other" %}selected{% endif %}>📦 Бусад</option>
    </select>'''

# Буруу select-г олоод устгах
import re
pattern = r'<select class="search-sel" name="cat" onchange="this\.form\.submit\(\)">.*?(?=</form>|<div class="cats">|{% if category)'
match = re.search(pattern, content, re.DOTALL)
if match:
    print("Олдлоо, засаж байна...")
    content = content[:match.start()] + new + '\n  ' + content[match.end():]
    open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND — шууд idx-ээр засна")
    idx = content.find('<select class="search-sel" name="cat"')
    end_idx = content.find('{% if category == "material" %}', idx)
    if end_idx > 0:
        content = content[:idx] + new + '\n  ' + content[end_idx:]
        open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(content)
        print("OK — idx-ээр засагдлаа")