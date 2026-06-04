content = open("apps/registry/static/registry/admin/admin_menu.js", "r", encoding="utf-8").read()

old = "        { url: '/admin/messaging/messagelog/',"
new = """        { url: '/admin/public/ad/',        label: '\\ud83d\\udce2 \\u0411\\u04af\\u0445 \\u0437\\u0430\\u0440\\u0443\\u0443\\u0434' },
        { url: '/admin/public/sliderad/',   label: '\\ud83d\\udd04 \\u0423\\u0440\\u0441\\u0434\\u0430\\u0433 \\u0437\\u0430\\u0440\\u0443\\u0443\\u0434' },
        { url: '/admin/messaging/messagelog/',"""

content = content.replace(old, new, 1)
open("apps/registry/static/registry/admin/admin_menu.js", "w", encoding="utf-8").write(content)
print("OK")