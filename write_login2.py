content = open("apps/registry/templates/registration/login.html", "r", encoding="utf-8").read()
open("templates/registration/login.html", "w", encoding="utf-8").write(content)
print("OK")
print(content[:100])