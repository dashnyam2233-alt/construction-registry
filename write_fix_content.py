content = open("templates/admin/base_site.html", "r", encoding="utf-8").read()

old = "    #content{ padding-top: 12px; }"
new = "    #content{ padding-top: 12px; padding-right: 0 !important; }\n    #changelist-filter{ display: block !important; }"

content = content.replace(old, new, 1)
open("templates/admin/base_site.html", "w", encoding="utf-8").write(content)
print("OK")