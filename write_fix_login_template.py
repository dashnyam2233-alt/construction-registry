content = open("templates/registration/login.html", "r", encoding="utf-8").read()

old = '<form method="post"'
new = '<form method="post"'

# Hidden next field нэмэх
if 'name="next"' not in content:
    content = content.replace(
        '{% csrf_token %}',
        '{% csrf_token %}\n    {% if next %}<input type="hidden" name="next" value="{{ next }}">{% endif %}',
        1
    )
    open("templates/registration/login.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("Аль хэдийн байна")