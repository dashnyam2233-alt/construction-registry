import re

content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

new_select = '''name="building_type">
          <option value="">— Сонгоно уу —</option>
          <optgroup label="🏠 Орон сууцны барилга">
            <option value="Амины орон сууц (1-2 давхар)">🏡 Амины орон сууц (1-2 давхар)</option>
            <option value="Олон айлын орон сууц (3-9 давхар)">🏢 Олон айлын орон сууц (3-9 давхар)</option>
            <option value="Өндөр давхар орон сууц (10+ давхар)">🏙 Өндөр давхар орон сууц (10+ давхар)</option>
          </optgroup>
          <optgroup label="🏢 Нийтийн барилга">
            <option value="Оффисын барилга">🏢 Оффисын барилга</option>
            <option value="Дэлгүүр, худалдааны төв">🏪 Дэлгүүр, худалдааны төв</option>
            <option value="Сургууль, цэцэрлэг">🏫 Сургууль, цэцэрлэг</option>
            <option value="Эмнэлэг">🏥 Эмнэлэг</option>
            <option value="Зочид буудал">🏨 Зочид буудал</option>
          </optgroup>
          <optgroup label="🏭 Үйлдвэрлэл, агуулах">
            <option value="Агуулах (хөнгөн бүтэц)">🏭 Агуулах (хөнгөн бүтэц)</option>
            <option value="Үйлдвэрийн барилга">🏭 Үйлдвэрийн барилга</option>
            <option value="Гараж, паркинг">🚗 Гараж, паркинг</option>
          </optgroup>
          <optgroup label="🔧 Тусгай барилга">
            <option value="Спортын заал">⚽ Спортын заал</option>
            <option value="Засвар, өргөтгөл">🔧 Засвар, өргөтгөл</option>
            <option value="Шашны барилга">⛪ Шашны барилга</option>
          </optgroup>
          </select>'''

pattern = r'name="building_type">.*?</select>'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + new_select + content[match.end():]
    open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")