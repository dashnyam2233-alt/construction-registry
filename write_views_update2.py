content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = """from apps.core.models import Company, Worker, Brigade
    from apps.accounts.models import GovernmentOrganization if hasattr(__import__('apps.core.models', fromlist=['GovernmentOrganization']), 'GovernmentOrganization') else None
    companies_count = Company.objects.count()
    workers_count = Worker.objects.count()
    brigades_count = Brigade.objects.count()
    recent_companies = list(Company.objects.order_by('-id')[:6])

    return {
        "tab": tab,
        "contact": contact,
        "banners": banners,
        "featured_admin_post": featured_admin_post,
        "chat_stream": chat_stream,
        "is_admin_like": is_admin_like,
        "can_post": user.is_authenticated,
        "display_name": get_display_name(user),
        "hero_banner": hero_banner,
        "slider_ads": slider_ads,
        "sub_banner": sub_banner,
    }"""

new = """    companies_count = Company.objects.count()
    workers_count = Worker.objects.count()
    brigades_count = Brigade.objects.count()
    recent_companies = list(Company.objects.order_by('-id')[:6])

    return {
        "tab": tab,
        "contact": contact,
        "banners": banners,
        "featured_admin_post": featured_admin_post,
        "chat_stream": chat_stream,
        "is_admin_like": is_admin_like,
        "can_post": user.is_authenticated,
        "display_name": get_display_name(user),
        "hero_banner": hero_banner,
        "slider_ads": slider_ads,
        "sub_banner": sub_banner,
        "companies_count": companies_count,
        "workers_count": workers_count,
        "brigades_count": brigades_count,
        "recent_companies": recent_companies,
    }"""

content = content.replace(old, new, 1)
open("apps/registry/views.py", "w", encoding="utf-8").write(content)
print("OK")
print("Check:", "companies_count" in content)