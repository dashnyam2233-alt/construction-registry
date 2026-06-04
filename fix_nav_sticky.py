content = open("apps/registry/templates/registry/public_home.html", "r", encoding="utf-8").read()

# nav-д position sticky нэмэх
old = '.nav{'
new = '.nav{position:sticky;top:0;z-index:1000;'

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/public_home.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND — nav CSS өөр байна")
    import re
    navs = re.findall(r'\.nav\b[^{]*\{[^}]*\}', content)
    for n in navs[:3]:
        print(repr(n[:100]))