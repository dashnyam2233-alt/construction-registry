content = open("apps/registry/views.py", "r", encoding="utf-8").read()

bad = """    from apps.core.models import Company, Worker, Brigade
    from apps.accounts.models import GovernmentOrganization if hasattr(__import__('apps.core.models', fromlist=['GovernmentOrganization']), 'GovernmentOrganization') else None
    companies_count = Company.objects.count()"""

good = """    companies_count = Company.objects.count()"""

if bad in content:
    content = content.replace(bad, good, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK — засагдлаа")
else:
    print("NOT FOUND — өөр хайж байна")
    idx = content.find("GovernmentOrganization")
    if idx >= 0:
        print(repr(content[idx-5:idx+100]))