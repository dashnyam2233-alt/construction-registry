import urllib.request, re

req = urllib.request.Request(
    "https://barilga.mn/nc/22",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
)
try:
    r = urllib.request.urlopen(req, timeout=10)
    content = r.read().decode("utf-8", errors="ignore")
    print("HTML урт:", len(content))
    
    # Үнэ хайх
    for kw in ["төгрөг", "₮", "цемент", "тоосго", "арматур", "элс", "price", "rate"]:
        idx = content.lower().find(kw.lower())
        if idx >= 0:
            print(f"\n'{kw}' олдлоо {idx}-д:")
            print(content[max(0,idx-200):idx+300])
            print("---")
except Exception as e:
    print("Алдаа:", e)