content = open("templates/registry/profile.html", "r", encoding="utf-8").read()

old = '              <span class="btn-sm btn-del">🗑 Устгах</span>'
new = '''              <form method="post" action="/ads/{{ ad.pk }}/delete/" style="display:inline;" onsubmit="return confirm('Устгах уу?')">
                {% csrf_token %}
                <button type="submit" class="btn-sm btn-del">🗑 Устгах</button>
              </form>'''

content = content.replace(old, new)
open("templates/registry/profile.html", "w", encoding="utf-8").write(content)
print("OK")