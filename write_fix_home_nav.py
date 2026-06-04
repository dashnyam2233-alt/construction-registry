content = open("apps/registry/templates/registry/public_home.html", "r", encoding="utf-8").read()

old = '\n    <a href="/ads/create/" class="nb nb-y">+ Зар оруулах</a>'
new = ''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/public_home.html", "w", encoding="utf-8").write(content)
    print("OK — устгагдлаа")
else:
    old2 = '<a href="/ads/create/" class="nb nb-y">+ Зар оруулах</a>'
    if old2 in content:
        content = content.replace(old2, '', 1)
        open("apps/registry/templates/registry/public_home.html", "w", encoding="utf-8").write(content)
        print("OK — устгагдлаа")
    else:
        print("NOT FOUND")