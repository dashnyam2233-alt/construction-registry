content = open("apps/registry/templates/registry/public_home.html", "r", encoding="utf-8").read()

# Навигацид тендер нэмэх
old = '<a href="/public/?tab=contact" class="nl {% if tab == \'contact\' %}on{% endif %}">Холбоо</a>'
new = '<a href="/public/?tab=contact" class="nl {% if tab == \'contact\' %}on{% endif %}">Холбоо</a>\n    <a href="/tender/" class="nl">📋 Тендер</a>'

if "Тендер" not in content:
    content = content.replace(old, new)
    open("apps/registry/templates/registry/public_home.html", "w", encoding="utf-8").write(content)
    print("OK — Тендер цэс нэмэгдлээ")
else:
    print("Аль хэдийн байна")