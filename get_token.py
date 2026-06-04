import urllib.request
import json

USERNAME = "нэвтрэх_нэр"
PASSWORD = "нууц_үг"

# Өөр өөр endpoint туршина
endpoints = [
    "http://opendata.tender.gov.mn/api/login",
    "http://opendata.tender.gov.mn/api/auth",
    "http://opendata.tender.gov.mn/api/token",
    "https://user.tender.gov.mn/api/login",
]

for url in endpoints:
    try:
        data = json.dumps({"username": USERNAME, "password": PASSWORD}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        r = urllib.request.urlopen(req, timeout=5)
        print(f"✅ {url}")
        print(r.read().decode()[:500])
    except Exception as e:
        print(f"❌ {url} — {e}")