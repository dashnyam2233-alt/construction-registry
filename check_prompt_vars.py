content = open("apps/registry/views.py", "r", encoding="utf-8").read()
idx = content.find("Нэг давхрын талбай")
print(repr(content[idx:idx+500]))