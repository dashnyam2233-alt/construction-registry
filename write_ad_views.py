# Ad create view
view_code = '''

def ad_create(request):
    from apps.public.models import Ad
    from django.utils import timezone
    import datetime

    if not request.user.is_authenticated:
        return redirect("/login/?next=/ads/create/")

    errors = {}
    if request.method == "POST":
        title = (request.POST.get("title") or "").strip()
        category = (request.POST.get("category") or "other").strip()
        description = (request.POST.get("description") or "").strip()
        price_str = (request.POST.get("price") or "").strip()
        price_type = (request.POST.get("price_type") or "negotiable").strip()
        city = (request.POST.get("city") or "UB").strip()
        district = (request.POST.get("district") or "").strip()
        contact_name = (request.POST.get("contact_name") or "").strip()
        contact_phone = (request.POST.get("contact_phone") or "").strip()
        contact_email = (request.POST.get("contact_email") or "").strip()

        if not title:
            errors["title"] = "Гарчиг заавал оруулна уу."
        if not contact_phone:
            errors["contact_phone"] = "Утасны дугаар заавал оруулна уу."

        if not errors:
            price = None
            if price_str:
                try:
                    price = float(price_str.replace(",", "").replace(" ", ""))
                except ValueError:
                    pass

            ad = Ad.objects.create(
                author=request.user,
                category=category,
                title=title,
                description=description,
                price=price,
                price_type=price_type,
                city=city,
                district=district,
                contact_name=contact_name,
                contact_phone=contact_phone,
                contact_email=contact_email,
                status="active",
                expires_at=timezone.now() + datetime.timedelta(days=30),
            )
            if request.FILES.get("image1"):
                ad.image1 = request.FILES["image1"]
            if request.FILES.get("image2"):
                ad.image2 = request.FILES["image2"]
            if request.FILES.get("image3"):
                ad.image3 = request.FILES["image3"]
            ad.save()
            return redirect("/ads/")

    return render(request, "registry/ad_create.html", {
        "errors": errors,
        "post_data": request.POST,
        "display_name": get_display_name(request.user),
    })


def ad_list(request):
    from apps.public.models import Ad
    category = request.GET.get("cat", "")
    q = request.GET.get("q", "")
    ads = Ad.objects.filter(status="active").order_by("-created_at")
    if category:
        ads = ads.filter(category=category)
    if q:
        ads = ads.filter(title__icontains=q)
    return render(request, "registry/ad_list.html", {
        "ads": ads[:50],
        "category": category,
        "q": q,
        "display_name": get_display_name(request.user),
    })
'''

content = open("apps/registry/views.py", "r", encoding="utf-8").read()
if "def ad_create" not in content:
    with open("apps/registry/views.py", "a", encoding="utf-8") as f:
        f.write(view_code)
    print("OK — view нэмэгдлээ")
else:
    print("Аль хэдийн байна")