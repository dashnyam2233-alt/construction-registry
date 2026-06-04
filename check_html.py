import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()

from django.test import RequestFactory
from apps.registry.views import ad_list

factory = RequestFactory()
request = factory.get("/ads/")
request.user = type("U", (), {"is_authenticated": False, "username": ""})()
response = ad_list(request)
content = response.content.decode("utf-8")

# Эхний 3000 тэмдэгтийг харах
print(content[500:3500])