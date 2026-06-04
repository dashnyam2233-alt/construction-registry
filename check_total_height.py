content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()
idx = content.find("total_height")
while idx >= 0:
    print(repr(content[max(0,idx-50):idx+150]))
    print("---")
    idx = content.find("total_height", idx+1)