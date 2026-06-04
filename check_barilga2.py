import urllib.request

req = urllib.request.Request(
    "https://barilga.mn/fwlink/barilgarate",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
)
try:
    r = urllib.request.urlopen(req, timeout=10)
    content = r.read().decode("utf-8", errors="ignore")
    print("Статус: OK")
    print("HTML урт:", len(content))
    print("\nЭхний 3000 тэмдэгт:")
    print(content[:3000])
except Exception as e:
    print("Алдаа:", e)