import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.public.models import MaterialPrice

cats = MaterialPrice.objects.filter(is_active=True).values_list('category', 'name', 'price_min', 'price_max', 'unit').order_by('category')
for c in cats:
    print(f"{c[0]:25} | {c[1]:40} | {int(c[2]):>10,}₮ | {int(c[3]):>10,}₮ | {c[4]}")