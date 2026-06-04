content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''    item = request.GET.get("item", "")
    q = request.GET.get("q", "")
    ads = Ad.objects.filter(status="active").order_by("-created_at")
    if category:
        ads = ads.filter(category=category)
    if subcat:
        ads = ads.filter(material_subcategory=subcat)
    if item:
        ads = ads.filter(material_item=item)'''

new = '''    item_raw = request.GET.get("item", "")
    q = request.GET.get("q", "")

    # subcat__item форматаар задлах
    item = ""
    if item_raw and "__" in item_raw:
        parts = item_raw.split("__", 1)
        if not subcat:
            subcat = parts[0]
        item = parts[1]
    elif item_raw:
        item = item_raw

    ads = Ad.objects.filter(status="active").order_by("-created_at")
    if category:
        ads = ads.filter(category=category)
    if subcat:
        ads = ads.filter(material_subcategory=subcat)
    if item:
        ads = ads.filter(material_item=item)'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")