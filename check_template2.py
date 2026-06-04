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

try:
    response = ad_list(request)
    print("Status:", response.status_code)
    content = response.content.decode("utf-8")
    print("HTML урт:", len(content))
    # cats tab байгаа эсэх
    print("cats div байна уу:", "cats" in content)
    print("wrap div байна уу:", "wrap" in content)
    print("ads-grid байна уу:", "ads-grid" in content)
except Exception as e:
    import traceback
    traceback.print_exc()