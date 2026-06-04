content = open("apps/registry/views.py", "r", encoding="utf-8").read()
idx = content.find("def budget_calculator")
print(content[idx+2800:idx+4200])