content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '    return {\n        "tab": tab,'

new = '''    companies_count = Company.objects.count()
    workers_count = Worker.objects.count()
    brigades_count = Brigade.objects.count()
    recent_companies = list(Company.objects.order_by("-id")[:6])

    return {
        "tab": tab,
        "companies_count": companies_count,
        "workers_count": workers_count,
        "brigades_count": brigades_count,
        "recent_companies": recent_companies,'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND — return { мөрийг хайж байна:")
    idx = content.find("return {")
    print(repr(content[idx-5:idx+50]))