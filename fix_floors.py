content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

old = '''          <select name="floors">
            <option value="1">1 давхар</option>
            <option value="2">2 давхар</option>
            <option value="3">3 давхар</option>
            <option value="4">4 давхар</option>
            <option value="5">5 давхар</option>
            <option value="6-10">6-10 давхар</option>
            <option value="10+">10-аас дээш</option>
          </select>'''

new = '''          <input type="number" name="floors" placeholder="Жишээ: 3" min="1" max="50" value="1">'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")