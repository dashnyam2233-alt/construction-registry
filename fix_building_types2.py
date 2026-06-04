import re

content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

old = 'value="Олон айлын орон сууц (3-9 давхар)">🏢 Олон айлын орон сууц (3-9 давхар)</option>\n            <option value="Өндөр давхар орон сууц (10+ давхар)">🏙 Өндөр давхар орон сууц (10+ давхар)</option>'
new = 'value="Олон айлын орон сууц">🏢 Олон айлын орон сууц</option>'

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    # Regex ашиглах
    pattern = r'value="Олон айлын орон сууц[^"]*">[^<]*</option>\s*<option value="Өндөр давхар[^"]*">[^<]*</option>'
    match = re.search(pattern, content)
    if match:
        content = content[:match.start()] + 'value="Олон айлын орон сууц">🏢 Олон айлын орон сууц</option>' + content[match.end():]
        open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
        print("OK — regex")
    else:
        idx = content.find("Олон айлын")
        print(repr(content[idx:idx+200]))