content = open("apps/registry/views.py", "r", encoding="utf-8").read()
idx = content.find("def public_login")
print(content[idx:idx+500])