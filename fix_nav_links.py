content = open("apps/registry/templates/registry/public_home.html", "r", encoding="utf-8").read()

replacements = [
    ('/public/?tab=house', '/ads/?cat=realestate'),
    ('/public/?tab=material', '/ads/?cat=material'),
    ('/public/?tab=worker', '/ads/?cat=worker'),
    ('/public/?tab=repair', '/ads/?cat=service'),
    ('/public/?tab=design', '/ads/?cat=design'),
]

for old, new in replacements:
    content = content.replace(old, new)
    print(f"OK — {old} → {new}")

open("apps/registry/templates/registry/public_home.html", "w", encoding="utf-8").write(content)
print("Хадгалагдлаа")