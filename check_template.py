import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()
from django.template.loader import get_template
try:
    t = get_template("registry/ad_list.html")
    print("OK")
except Exception as e:
    print("ERROR:", e)