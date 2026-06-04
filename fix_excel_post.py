content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''    data_str = request.GET.get("data", "{}")'''
new = '''    data_str = request.POST.get("data", request.GET.get("data", "{}"))'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")