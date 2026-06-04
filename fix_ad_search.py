content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = 'ads = ads.filter(title__icontains=q) | Ad.objects.filter(organization__icontains=q, status="active")'
new = 'ads = ads.filter(title__icontains=q)'

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")