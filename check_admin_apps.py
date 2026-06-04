import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()

from django.contrib import admin
print("Бүртгэлтэй model-ууд:")
for model, admin_class in admin.site._registry.items():
    print(f"  {model.__module__}.{model.__name__}")