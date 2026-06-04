import urllib.request

req = urllib.request.Request(
    "https://barilga.mn",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
)
try:
    r = urllib.request.urlopen(req, timeout=10)
    content = r.read().decode("utf-8", errors="ignore")
    print("Статус: OK")
    print("HTML урт:", len(content))
    # Үнэтэй холбоотой хэсэг хайх
    for kw in ["үнэ", "price", "материал", "тоосго", "цемент"]:
        idx = content.lower().find(kw)
        if idx >= 0:
            print(f"\n'{kw}' олдлоо:")
            print(content[max(0,idx-100):idx+200])
            break
except Exception as e:
    print("Алдаа:", e)