path = r"apps\public\admin.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

if 'MaterialNorm' in content:
    print("MaterialNorm admin-д байна")
    # Яг хэсгийг харуулах
    idx = content.find('MaterialNorm')
    print(repr(content[idx-50:idx+200]))
else:
    print("MaterialNorm БАЙХГҮЙ")
    # import мөрийг харуулах
    idx = content.find('from .models import')
    print(repr(content[idx:idx+200]))