content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '    if subcat:\n        ads = ads.filter(material_subcategory=subcat)\n    if item:\n        ads = ads.filter(material_item=item)'

new = '''    if subcat:
        if category == "material":
            ads = ads.filter(material_subcategory=subcat)
        elif category == "house":
            ads = ads.filter(house_location_type=subcat)
    if item:
        if category == "material":
            ads = ads.filter(material_item=item)
        elif category == "house":
            if subcat == "rooms":
                ads = ads.filter(house_rooms=item)
            elif subcat in ("ub", "province"):
                ads = ads.filter(house_location=item)
            elif subcat == "type":
                ads = ads.filter(house_type=item)'''

HOUSE_SUBCAT_LABELS = {
    "rooms": "Өрөөний тоо",
    "ub": "Улаанбаатар",
    "province": "Орон нутаг",
    "type": "Зарын төрөл",
}

if old in content:
    content = content.replace(old, new, 1)
    # SUBCAT_LABELS-д house нэмэх
    content = content.replace(
        '"safety": "ХАБЭА",\n    }',
        '"safety": "ХАБЭА",\n        "rooms": "Өрөөний тоо",\n        "ub": "Улаанбаатар",\n        "province": "Орон нутаг",\n        "type": "Зарын төрөл",\n    }'
    )
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")