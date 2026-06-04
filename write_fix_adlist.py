content = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").read()

old = '    <div class="ad-card">'
new = '    <a href="/ads/{{ ad.pk }}/" class="ad-card" style="display:block;">'

old2 = '    </div>\n    {% endfor %}'
new2 = '    </a>\n    {% endfor %}'

content = content.replace(old, new, 1)
content = content.replace('    </div>\n    {% endfor %}', '    </a>\n    {% endfor %}', 1)

open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(content)
print("OK")