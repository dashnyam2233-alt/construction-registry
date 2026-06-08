
import os

# OTP view код
otp_view = """
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.models import User
import json, random, string
from twilio.rest import Client

def get_twilio_client():
    return Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

@csrf_exempt
def send_otp(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)
    try:
        data = json.loads(request.body)
        phone = data.get("phone", "").strip()
        if not phone:
            return JsonResponse({"error": "Утасны дугаар оруулна уу"}, status=400)
        if not phone.startswith("+"):
            phone = "+976" + phone
        client = get_twilio_client()
        verification = client.verify.v2.services(
            os.getenv("TWILIO_VERIFY_SID")
        ).verifications.create(to=phone, channel="sms")
        return JsonResponse({"success": True, "status": verification.status})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt  
def verify_otp(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)
    try:
        data = json.loads(request.body)
        phone = data.get("phone", "").strip()
        code = data.get("code", "").strip()
        if not phone.startswith("+"):
            phone = "+976" + phone
        client = get_twilio_client()
        result = client.verify.v2.services(
            os.getenv("TWILIO_VERIFY_SID")
        ).verification_checks.create(to=phone, code=code)
        if result.status == "approved":
            user, created = User.objects.get_or_create(username=phone)
            if created:
                user.set_unusable_password()
                user.save()
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)
            return JsonResponse({"success": True, "redirect": "/public/"})
        else:
            return JsonResponse({"error": "Код буруу байна"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
"""

with open("/var/www/construction-registry/apps/registry/otp_views.py", "w") as f:
    f.write("import os\n" + otp_view)

print("OTP views created")

# urls.py-д нэмэх
with open("/var/www/construction-registry/apps/registry/urls.py", "r") as f:
    urls = f.read()

if "send_otp" not in urls:
    urls = urls.replace(
        "from .views import (",
        "from .otp_views import send_otp, verify_otp\nfrom .views import ("
    )
    urls = urls.replace(
        'path("logout/"',
        'path("auth/send-otp/", send_otp, name="send_otp"),\n    path("auth/verify-otp/", verify_otp, name="verify_otp"),\n    path("logout/"'
    )
    with open("/var/www/construction-registry/apps/registry/urls.py", "w") as f:
        f.write(urls)
    print("URLs updated")
else:
    print("URLs already updated")
