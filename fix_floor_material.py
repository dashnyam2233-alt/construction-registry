import re

content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

old = '''        <div class="field">
          <label>Шалны материал</label>
          <select name="floor_material">
            <option value="Цутгамал шал">Цутгамал шал — хямд</option>
            <option value="Ламинат">Ламинат — дунд</option>
            <option value="Паркет">Паркет — премиум</option>
            <option value="Плита">Плита — ванн, гал тогоо</option>
            <option value="Хосолсон">Хосолсон</option>
          </select>
        </div>'''

new = '''        <div class="field">
          <label>Шалны материал (үндсэн өрөө)</label>
          <select name="floor_material">
            <option value="Ламинат (үндсэн) + Плита (ванн, гал тогоо)">Ламинат + Плита — нийтлэг</option>
            <option value="Паркет (үндсэн) + Плита (ванн, гал тогоо)">Паркет + Плита — премиум</option>
            <option value="Цутгамал шал бүгд">Цутгамал шал бүгд — хямд</option>
            <option value="Плита бүгд">Плита бүгд</option>
            <option value="Винил (SPC) + Плита">Винил (SPC) + Плита</option>
            <option value="Паркет бүгд">Паркет бүгд — премиум</option>
          </select>
          <div class="field-hint">Ванн, гал тогооны шал автоматаар плита тооцогдоно</div>
        </div>'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")