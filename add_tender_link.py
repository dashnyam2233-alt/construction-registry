content = open("apps/registry/templates/registry/public_home.html", "r", encoding="utf-8").read()

# Навигацийн сүүлийн цэсийг хайж тендер нэмэх
old = '<a href="/public/?tab=contact"'
new = '<a href="/tender/" class="nl">📋 Тендер</a>\n    <a href="/public/?tab=contact"'

if "/tender/" not in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/public_home.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("Байна")

# Шалгах
c = open("apps/registry/templates/registry/public_home.html", "r", encoding="utf-8").read()
print("tender байна уу:", "/tender/" in c)