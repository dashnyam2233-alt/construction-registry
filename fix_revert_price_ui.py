# 1. Index.html-аас үнийн блок устгах
content = open("templates/admin/index.html", "r", encoding="utf-8").read()

import re
content = re.sub(r'\s*<!-- Үнийн мэдээлэл -->.*?</div>\s*', '\n  ', content, flags=re.DOTALL, count=1)
open("templates/admin/index.html", "w", encoding="utf-8").write(content)
print("OK — index.html цэвэрлэгдлээ")

# 2. _sidebar_registry.html-аас үнийн блок устгах
content2 = open("templates/admin/_sidebar_registry.html", "r", encoding="utf-8").read()
content2 = re.sub(r'<!-- Үнийн мэдээлэл -->.*?</div>\s*\n\n', '', content2, flags=re.DOTALL, count=1)
open("templates/admin/_sidebar_registry.html", "w", encoding="utf-8").write(content2)
print("OK — sidebar цэвэрлэгдлээ")