content = open("templates/admin/base_site.html", "r", encoding="utf-8").read()

# Sidebar-д үнийн цэс нэмэх
old = '<a href="/tender/" class="nl">📋 Тендер</a>'

# Sidebar-д байгаа цэсийг хайх
import re
# Admin sidebar link хайх
idx = content.find("МАРКЕТИНГ")
if idx >= 0:
    print("МАРКЕТИНГ олдлоо:", idx)
    print(content[idx-200:idx+500])
else:
    print("МАРКЕТИНГ олдсонгүй")
    # Sidebar-ийн бүтцийг харах
    idx2 = content.find("sidebar")
    print("sidebar:", idx2)
    idx3 = content.find("nav-item")
    print("nav-item:", idx3)
    # Бүх цэсийг харах
    links = re.findall(r'<a[^>]*href="/admin/[^"]*"[^>]*>[^<]*</a>', content)
    for l in links[:20]:
        print(l)