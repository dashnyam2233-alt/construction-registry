import os, sys, django, json
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.public.models import Tender

tenders = list(Tender.objects.values(
    'title', 'organization', 'category', 'price',
    'deadline', 'url', 'tender_code', 'method',
    'is_construction', 'created_at'
))

for t in tenders:
    for k, v in t.items():
        if hasattr(v, 'isoformat'):
            t[k] = v.isoformat()

with open('tenders_export.json', 'w', encoding='utf-8') as f:
    json.dump(tenders, f, ensure_ascii=False, indent=2)

print(f"DONE - {len(tenders)} тендер экспортлогдлоо → tenders_export.json")