import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()
from apps.public.models import Ad
print("Нийт зар:", Ad.objects.count())
print("Идэвхтэй:", Ad.objects.filter(status="active").count())
for ad in Ad.objects.all()[:5]:
    print(f"  - {ad.title} | cat={ad.category} | status={ad.status}")