content = open("templates/admin/base_site.html", "r", encoding="utf-8").read()

old = """{% block footer %}
  {{ block.super }}
{% endblock %}"""

new = """{% block footer %}
  {{ block.super }}
  {% if request.user.is_authenticated %}
    <aside style="position:fixed;top:90px;right:0;width:280px;height:calc(100vh - 90px);overflow-y:auto;background:#fff;border-left:0.5px solid #e2e8f0;padding:14px;z-index:100;">
      {% registry_admin_sidebar %}
    </aside>
  {% endif %}
{% endblock %}"""

if old in content:
    content = content.replace(old, new, 1)
    open("templates/admin/base_site.html", "w", encoding="utf-8").write(content)
    print("OK — sidebar сэргээгдлээ")
else:
    print("NOT FOUND")
    print(repr(content[-300:]))