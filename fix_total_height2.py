content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

# min attribute-г устгах
old = 'input type="number" name="total_height" placeholder="30" min="0" max="300" value="0"'
new = 'input type="number" name="total_height" placeholder="30" max="300" value="0"'

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    # Урт, өргөн-д байгаа min-г ч устгах
    import re
    content = re.sub(r'(name="total_height"[^>]*)\bmin="\d+"', r'\1', content)
    content = re.sub(r'(name="length"[^>]*)\bmin="\d+"', r'\1', content)
    content = re.sub(r'(name="width"[^>]*)\bmin="\d+"', r'\1', content)
    open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
    print("OK — regex-ээр засагдлаа")