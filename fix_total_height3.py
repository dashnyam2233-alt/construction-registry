content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

old = '<input type="number" name="total_height" placeholder="30" max="300" value="0">'
new = '<input type="text" name="total_height" placeholder="30" value="0">'

if old in content:
    content = content.replace(old, new, 1)

# Урт, өргөн-ийн min attribute ч устгах
old2 = '<input type="number" name="length" placeholder="42" max="500">'
new2 = '<input type="text" name="length" placeholder="42">'
if old2 in content:
    content = content.replace(old2, new2, 1)

old3 = '<input type="number" name="width" placeholder="27" max="500">'
new3 = '<input type="text" name="width" placeholder="27">'
if old3 in content:
    content = content.replace(old3, new3, 1)

# inner_wall_length input байвал устгах
import re
content = re.sub(r'<input type="number" name="inner_wall_length"[^>]*>', 
                 '<input type="text" name="inner_wall_length" placeholder="0" value="0">', 
                 content)

open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
print("OK")