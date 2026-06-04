content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''        ad = Ad.objects.create(
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
            )'''

new = '''        material_subcategory = (request.POST.get("material_subcategory") or "").strip()
        material_item = (request.POST.get("material_item") or "").strip()
        price_unit = (request.POST.get("price_unit") or "negotiable").strip()

        ad = Ad.objects.create(
                author=request.user,
                category=category,
                material_subcategory=material_subcategory,
                material_item=material_item,
                price_unit=price_unit,
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
            )'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")