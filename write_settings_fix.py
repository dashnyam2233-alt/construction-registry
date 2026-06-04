path = r"config\settings.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '    "django.contrib.staticfiles",'
new = '    "django.contrib.staticfiles",\n    "django.contrib.humanize",'

if old in content:
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("DONE - humanize нэмэгдлээ")
else:
    print("NOT FOUND")