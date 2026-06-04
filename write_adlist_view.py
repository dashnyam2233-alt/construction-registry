content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''def ad_list(request):
    from apps.public.models import Ad
    category = request.GET.get("cat", "")
    subcat = request.GET.get("subcat", "")
    q = request.GET.get("q", "")
    ads = Ad.objects.filter(status="active").order_by("-created_at")
    if category:
        ads = ads.filter(category=category)
    if subcat:
        ads = ads.filter(material_subcategory=subcat)
    if q:
        ads = ads.filter(title__icontains=q)
    SUBCAT_LABELS = {
        "foundation": "Барилгын үндсэн хийц",
        "interior": "Засал чимэглэл",
        "outdoor": "Гадна тохижилт",
        "plumbing": "Сан, халаалт",
        "electrical": "Цахилгаан, холбоо",
        "machinery": "Машин, тоног",
        "furniture": "Тавилга",
        "software": "Программ, ном",
        "safety": "ХАБЭА",
    }
    return render(request, "registry/ad_list.html", {
        "ads": ads[:100],
        "category": category,
        "subcat": subcat,
        "subcat_label": SUBCAT_LABELS.get(subcat, ""),
        "q": q,
        "display_name": get_display_name(request.user),
    })'''

new = '''def ad_list(request):
    import json, os
    from apps.public.models import Ad
    category = request.GET.get("cat", "")
    subcat = request.GET.get("subcat", "")
    item = request.GET.get("item", "")
    q = request.GET.get("q", "")
    ads = Ad.objects.filter(status="active").order_by("-created_at")
    if category:
        ads = ads.filter(category=category)
    if subcat:
        ads = ads.filter(material_subcategory=subcat)
    if item:
        ads = ads.filter(material_item=item)
    if q:
        ads = ads.filter(title__icontains=q) | Ad.objects.filter(organization__icontains=q, status="active")

    SUBCAT_LABELS = {
        "foundation": "Барилгын үндсэн хийц",
        "interior": "Засал чимэглэл",
        "outdoor": "Гадна тохижилт",
        "plumbing": "Сан, халаалт",
        "electrical": "Цахилгаан, холбоо",
        "machinery": "Машин, тоног",
        "furniture": "Тавилга",
        "software": "Программ, ном",
        "safety": "ХАБЭА",
    }

    item_choices = []
    item_label = ""
    try:
        json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "material_items.json")
        all_items = json.load(open(json_path, encoding="utf-8"))
        if subcat and subcat in all_items:
            item_choices = list(all_items[subcat].items())
            if item:
                item_label = all_items[subcat].get(item, "")
    except:
        pass

    return render(request, "registry/ad_list.html", {
        "ads": ads[:100],
        "category": category,
        "subcat": subcat,
        "item": item,
        "subcat_label": SUBCAT_LABELS.get(subcat, ""),
        "item_label": item_label,
        "item_choices": item_choices,
        "q": q,
        "display_name": get_display_name(request.user),
    })'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")