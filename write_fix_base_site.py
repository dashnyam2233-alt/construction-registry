content = open("templates/admin/base_site.html", "r", encoding="utf-8").read()

# Давхар extends устгах
bad = """{% extends "admin/base.html" %}
{% load static %}
{% extends "admin/base.html" %}
{% load static %}
{% load admin_sidebar %}"""

good = """{% extends "admin/base.html" %}
{% load static %}
{% load admin_sidebar %}"""

content = content.replace(bad, good, 1)
open("templates/admin/base_site.html", "w", encoding="utf-8").write(content)
print("OK")
print(content[:120])