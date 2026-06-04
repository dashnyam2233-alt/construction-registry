path = r"apps\public\admin.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('MaterialNormAdmin')
if idx >= 0:
    print(repr(content[idx-20:idx+300]))
else:
    print("MaterialNormAdmin БАЙХГҮЙ")
    # admin.register хайх
    idx2 = content.rfind('@admin.register')
    print(repr(content[idx2:idx2+200]))