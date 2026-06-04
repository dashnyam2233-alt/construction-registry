lines = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").readlines()

# 95-р мөрийг харах
print("90-100 мөрүүд:")
for i, l in enumerate(lines[88:102], start=89):
    print(f"{i}: {repr(l[:100])}")