content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''        profile = UserCompanyProfile.objects.filter(user=user).select_related("company").first()
        company = profile.company if profile else None
        return render(request, "registry/profile.html", {"company": company})'''

new = '''        profile = UserCompanyProfile.objects.filter(user=user).select_related("company").first()
        company = profile.company if profile else None
        from apps.public.models import Ad
        my_ads = list(Ad.objects.filter(author=user).order_by("-created_at")[:10])
        return render(request, "registry/profile.html", {"company": company, "my_ads": my_ads})'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")