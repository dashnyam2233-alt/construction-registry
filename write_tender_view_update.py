content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''def tender_list(request):
    from apps.public.models import Tender
    q = request.GET.get("q", "")
    cat = request.GET.get("cat", "")
    tenders = Tender.objects.order_by("-created_at")
    if q:
        tenders = tenders.filter(title__icontains=q) | tenders.filter(organization__icontains=q)
    if cat == "construction":
        tenders = tenders.filter(is_construction=True)
    return render(request, "registry/tender_list.html", {
        "tenders": tenders[:100],
        "q": q,
        "cat": cat,
        "total": Tender.objects.count(),
        "display_name": get_display_name(request.user),
    })'''

new = '''def tender_list(request):
    from apps.public.models import Tender
    from django.db.models import Count
    q = request.GET.get("q", "")
    cat = request.GET.get("cat", "")
    tenders = Tender.objects.order_by("-created_at")
    if q:
        tenders = tenders.filter(title__icontains=q) | tenders.filter(organization__icontains=q)
    if cat:
        tenders = tenders.filter(category=cat)
    counts = {r["category"]: r["n"] for r in
              Tender.objects.values("category").annotate(n=Count("id"))}
    return render(request, "registry/tender_list.html", {
        "tenders": tenders[:100],
        "q": q,
        "cat": cat,
        "total": Tender.objects.count(),
        "counts": counts,
        "display_name": get_display_name(request.user),
    })'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")