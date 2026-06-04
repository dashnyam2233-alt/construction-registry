content = open("apps/registry/views.py", "r", encoding="utf-8").read()
idx = content.find("one_floor_area")
print(repr(content[idx:idx+400]))