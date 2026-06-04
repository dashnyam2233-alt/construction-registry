content = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").read()

# Django template-д == оронд == хэрэглэх
import re
content = re.sub(r'subcat=="(\w+)"', r'subcat == "\1"', content)
content = re.sub(r'category=="(\w+)"', r'category == "\1"', content)
content = re.sub(r'item=="(\w+)"', r'item == "\1"', content)

open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(content)
print("OK")