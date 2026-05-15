import io

path = r"apps\registry\static\registry\admin\admin_menu.js"

mapping = [
    ("/admin/registry/company/",                   "/admin/core/company/"),
    ("/admin/registry/governmentorganization/",    "/admin/core/governmentorganization/"),
    ("/admin/registry/nongovernmentorganization/", "/admin/core/nongovernmentorganization/"),
    ("/admin/registry/worker/",                    "/admin/core/worker/"),
    ("/admin/registry/familymember/",              "/admin/core/familymember/"),
    ("/admin/registry/brigade/",                   "/admin/core/brigade/"),
    ("/admin/registry/brigademember/",             "/admin/core/brigademember/"),
    ("/admin/registry/messagelog/",                "/admin/messaging/messagelog/"),
    ("/admin/registry/herobanner/",                "/admin/public/herobanner/"),
    ("/admin/registry/subbanner/",                 "/admin/public/subbanner/"),
    ("/admin/registry/sliderad/",                  "/admin/public/sliderad/"),
    ("/admin/registry/banner/",                    "/admin/public/banner/"),
    ("/admin/registry/publicpost/",                "/admin/public/publicpost/"),
    ("/admin/registry/usercompanyprofile/",        "/admin/accounts/usercompanyprofile/"),
    ("/admin/registry/siteconfig/",                "/admin/messaging/siteconfig/"),
]

with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

for old, new in mapping:
    text = text.replace(old, new)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("DONE")