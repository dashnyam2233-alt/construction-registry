content = open("apps/registry/templates/registry/public_home.html", "r", encoding="utf-8").read()
idx = content.find("<nav")
print(content[idx+1200:idx+2000])