content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

old = '''        <div class="field">
          <label>Нийт өндөр (м)</label>
          <input type="number" name="total_height" placeholder="30" min="2" max="300">
          <div class="field-hint">Газраас дээвэр хүртэл</div>
        </div>'''

new = '''        <div class="field">
          <label>Нийт өндөр (м)</label>
          <input type="number" name="total_height" placeholder="30" min="0" max="300" value="0">
          <div class="field-hint">Газраас дээвэр хүртэл (мэдэхгүй бол 0)</div>
        </div>'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")