content = open("apps/registry/templates/registry/public_home.html", "r", encoding="utf-8").read()

old = '<a href="/tender/" class="nl">📋 Тендер</a>'
new = '<a href="/tender/" class="nl">📋 Тендер</a>\n    <a href="/budget/" class="nl">🤖 AI Төсөв</a>'

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/public_home.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")