import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()
from apps.public.models import Ad

# house → realestate
updated = Ad.objects.filter(category="house").update(category="realestate")
print(f"house → realestate: {updated}")

# repair → service
updated2 = Ad.objects.filter(category="repair").update(category="service")
print(f"repair → service: {updated2}")

# Шалгах
for ad in Ad.objects.all():
    print(f"  {ad.title} | {ad.category}")