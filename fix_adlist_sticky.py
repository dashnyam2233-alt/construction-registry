content = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").read()

old = '.nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;gap:12px;}'
new = '.nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;gap:12px;position:sticky;top:0;z-index:1000;}'

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")