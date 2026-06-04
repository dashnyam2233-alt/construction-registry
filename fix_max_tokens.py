content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = 'max_tokens=2000,'
new = 'max_tokens=4000,'

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")
    # Байгааг харах
    import re
    matches = re.findall(r'max_tokens=\d+', content)
    print("Олдсон:", matches)