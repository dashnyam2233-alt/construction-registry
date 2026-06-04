content = open("apps/registry/templates/registry/public_home.html", "r", encoding="utf-8").read()

# Хайлтын form action-г /ads/ руу өөрчлөх
import re

# form action хайх
old_patterns = [
    'action="/public/"',
    "action='/public/'",
    'action=""',
    "action=''",
]

found = False
for old in old_patterns:
    if old in content:
        content = content.replace(old, 'action="/ads/"', 1)
        print(f"OK — {old} → action='/ads/'")
        found = True
        break

if not found:
    # form tag-г шалгах
    forms = re.findall(r'<form[^>]*>', content)
    for f in forms:
        print("FORM:", f)

open("apps/registry/templates/registry/public_home.html", "w", encoding="utf-8").write(content)