content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

# Суурийн төрөл засах
old1 = '''          <select name="foundation_type">
            <option value="Туузан суурь">Туузан суурь — элбэг хэрэглэгддэг</option>
            <option value="Хавтан суурь">Хавтан суурь — бүх талбайд</option>
            <option value="Шонон суурь">Шонон суурь — нойтон хөрс</option>
            <option value="Монолит суурь">Монолит суурь — хүчтэй</option>
          </select>'''

new1 = '''          <select name="foundation_type">
            <option value="Шугаман суурь (стандарт)">Шугаман суурь — стандарт</option>
            <option value="Хавтан суурь">Хавтан суурь — бүх талбайд</option>
            <option value="Гадсан суурь">Гадсан суурь — нойтон хөрс</option>
            <option value="Нил суурь">Нил суурь — өндөр давхар</option>
            <option value="Монолит суурь">Монолит суурь — хүчтэй</option>
          </select>'''

# Дулаалга засах
old2 = '''        <div class="field">
          <label>Дулаалга</label>
          <select name="insulation">
            <option value="Байхгүй">Байхгүй</option>
            <option value="Минвата 5см">Минвата 5 см</option>
            <option value="Минвата 10см" selected>Минвата 10 см — стандарт</option>
            <option value="Пенопласт 5см">Пенопласт 5 см</option>
            <option value="Пенопласт 10см">Пенопласт 10 см</option>
          </select>
        </div>'''

new2 = '''        <div class="field">
          <label>Ханын дулаалга</label>
          <select name="insulation">
            <option value="Байхгүй">Байхгүй</option>
            <option value="Шилэн хөвөн 5см">Шилэн хөвөн 5 см</option>
            <option value="Шилэн хөвөн 10см" selected>Шилэн хөвөн 10 см — стандарт</option>
            <option value="Хөөсөнцөр (пенопласт) 5см">Хөөсөнцөр 5 см</option>
            <option value="Хөөсөнцөр (пенопласт) 10см">Хөөсөнцөр 10 см</option>
            <option value="Базальт хөвөн 5см">Базальт хөвөн 5 см</option>
            <option value="Базальт хөвөн 10см">Базальт хөвөн 10 см</option>
            <option value="Пенополиуретан">Пенополиуретан (PPU)</option>
            <option value="Экструдированный пенополистирол">Экструдированный пенополистирол (XPS)</option>
          </select>
        </div>'''

# Гадна засал → Гадна хана засах
old3 = '''        <div class="field">
          <label>Гадна засал</label>
          <select name="facade">
            <option value="Штукатур">Штукатур — хямд</option>
            <option value="Фасадын будаг">Фасадын будаг</option>
            <option value="Клинкер тоосго">Клинкер тоосго</option>
            <option value="Вентилируемый фасад">Вентилируемый фасад</option>
          </select>
        </div>'''

new3 = '''        <div class="field">
          <label>Гадна хана өнгөлгөө</label>
          <select name="facade">
            <option value="Шавар штукатур">Шавар штукатур — хямд</option>
            <option value="Эмульс будаг">Эмульс будаг</option>
            <option value="Өнгөлгөөний тоосго">Өнгөлгөөний тоосго</option>
            <option value="Клинкер тоосго">Клинкер тоосго — премиум</option>
            <option value="Шилэн фасад">Шилэн фасад</option>
            <option value="Металл фасад (касетт)">Металл фасад (касетт)</option>
            <option value="Вентилируемый фасад">Вентилируемый фасад</option>
            <option value="Композит хавтан">Композит хавтан</option>
          </select>
        </div>'''

changed = 0
for old, new in [(old1, new1), (old2, new2), (old3, new3)]:
    if old in content:
        content = content.replace(old, new, 1)
        changed += 1
        print(f"OK — {changed}-р өөрчлөлт")
    else:
        print(f"NOT FOUND — {changed+1}-р өөрчлөлт")

open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
print("Хадгалагдлаа")