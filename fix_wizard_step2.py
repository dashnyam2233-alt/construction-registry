import re

content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

old = '''    <!-- АЛХАМ 2: Хэмжээс, харьцаа -->
    <div class="card" id="step2" style="display:none;">
      <div class="step-title">2️⃣ Хэмжээс, харьцаа</div>
      <div class="step-desc">Барилгын гадна хэмжээ, өндрийг оруулна уу</div>

      <div class="field-row3">
        <div class="field">
          <label>Урт (м)</label>
          <input type="number" name="length" placeholder="10" min="3" max="200">
          <div class="field-hint">Гадна хэмжээ</div>
        </div>
        <div class="field">
          <label>Өргөн (м)</label>
          <input type="number" name="width" placeholder="8" min="3" max="200">
          <div class="field-hint">Гадна хэмжээ</div>
        </div>
        <div class="field">
          <label>Нийт өндөр (м)</label>
          <input type="number" name="total_height" placeholder="6" min="2" max="100">
          <div class="field-hint">Газраас дээвэр хүртэл</div>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Тааз өндөр (м)</label>
          <select name="ceiling_height">
            <option value="2.5">2.5 м — стандарт</option>
            <option value="2.7">2.7 м</option>
            <option value="3.0">3.0 м</option>
            <option value="3.5">3.5 м — өндөр</option>
            <option value="4.0+">4.0м+ — үйлдвэр</option>
          </select>
        </div>
        <div class="field">
          <label>Өрөөний тоо</label>
          <select name="inner_wall_length">
            <option value="1">1 өрөө</option>
            <option value="2">2 өрөө</option>
            <option value="3">3 өрөө</option>
            <option value="4">4 өрөө</option>
            <option value="5">5 өрөө</option>
            <option value="6+">6 ба түүнээс дээш</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Цонхны тоо</label>
          <select name="windows">
            <option value="2-4">2-4 ш</option>
            <option value="5-8">5-8 ш</option>
            <option value="9-12">9-12 ш</option>
            <option value="13-20">13-20 ш</option>
            <option value="20+">20-аас дээш</option>
          </select>
        </div>
        <div class="field">
          <label>Хаалганы тоо</label>
          <select name="doors">
            <option value="1-2">1-2 ш</option>
            <option value="3-5">3-5 ш</option>
            <option value="6-10">6-10 ш</option>
            <option value="10+">10-аас дээш</option>
          </select>
        </div>
      </div>

      <div class="btn-row">
        <button type="button" class="btn-prev" onclick="prev(2)">← Өмнөх</button>
        <button type="button" class="btn-next" onclick="next(2)">Дараах →</button>
      </div>
    </div>'''

new = '''    <!-- АЛХАМ 2: Хэмжээс, харьцаа -->
    <div class="card" id="step2" style="display:none;">
      <div class="step-title">2️⃣ Хэмжээс, харьцаа</div>
      <div class="step-desc">Барилгын гадна хэмжээ, өндрийг оруулна уу</div>

      <div class="field-row3">
        <div class="field">
          <label>Урт (м)</label>
          <input type="number" name="length" placeholder="42" min="3" max="500">
          <div class="field-hint">Гадна хэмжээ</div>
        </div>
        <div class="field">
          <label>Өргөн (м)</label>
          <input type="number" name="width" placeholder="27" min="3" max="500">
          <div class="field-hint">Гадна хэмжээ</div>
        </div>
        <div class="field">
          <label>Нийт өндөр (м)</label>
          <input type="number" name="total_height" placeholder="30" min="2" max="300">
          <div class="field-hint">Газраас дээвэр хүртэл</div>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Тааз өндөр (м)</label>
          <select name="ceiling_height">
            <option value="2.5">2.5 м — стандарт</option>
            <option value="2.7">2.7 м</option>
            <option value="3.0">3.0 м</option>
            <option value="3.5">3.5 м — өндөр</option>
            <option value="4.0+">4.0м+ — үйлдвэр</option>
          </select>
        </div>
        <div class="field">
          <label>Нэг давхарт хэдэн айл/өрөө?</label>
          <select name="units_per_floor">
            <option value="1">1 айл/өрөө</option>
            <option value="2">2 айл</option>
            <option value="3">3 айл</option>
            <option value="4" selected>4 айл — нийтлэг</option>
            <option value="6">6 айл</option>
            <option value="8">8 айл</option>
            <option value="10+">10-аас дээш</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Айл бүр хэдэн өрөөтэй?</label>
          <select name="inner_wall_length">
            <option value="1 өрөөтэй айл">1 өрөөтэй айл</option>
            <option value="2 өрөөтэй айл">2 өрөөтэй айл</option>
            <option value="3 өрөөтэй айл" selected>3 өрөөтэй айл — нийтлэг</option>
            <option value="4 өрөөтэй айл">4 өрөөтэй айл</option>
            <option value="Холимог (1-4 өрөө)">Холимог (1-4 өрөө)</option>
          </select>
        </div>
        <div class="field">
          <label>1-р давхарт хэдэн айл?</label>
          <select name="ground_floor_units">
            <option value="Дээрх давхартай адил">Дээрх давхартай адил</option>
            <option value="Хагас (дэлгүүр, холбох заал)">Хагас — дэлгүүр, холбох заал</option>
            <option value="Бүгд нийтийн зориулалт">Бүгд нийтийн зориулалт</option>
            <option value="Гараж">Гараж</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Нэг айлд хэдэн цонх?</label>
          <select name="windows">
            <option value="2-3">2-3 ш — 1 өрөө</option>
            <option value="4-5">4-5 ш — 2 өрөө</option>
            <option value="5-6" selected>5-6 ш — 3 өрөө</option>
            <option value="7-8">7-8 ш — 4 өрөө</option>
            <option value="10+">10+ ш</option>
          </select>
        </div>
        <div class="field">
          <label>Нэг айлд хэдэн хаалга?</label>
          <select name="doors">
            <option value="2-3">2-3 ш — 1 өрөө</option>
            <option value="4-5" selected>4-5 ш — 3 өрөө</option>
            <option value="6-7">6-7 ш — 4 өрөө</option>
            <option value="8+">8+ ш</option>
          </select>
        </div>
      </div>

      <div class="btn-row">
        <button type="button" class="btn-prev" onclick="prev(2)">← Өмнөх</button>
        <button type="button" class="btn-next" onclick="next(2)">Дараах →</button>
      </div>
    </div>'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
    print("OK — 2-р алхам шинэчлэгдлээ")
else:
    print("NOT FOUND — regex ашиглана")
    pattern = r'<!-- АЛХАМ 2.*?</div>\s*\n\s*<!-- АЛХАМ 3'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        replacement = new + '\n\n    <!-- АЛХАМ 3'
        content = content[:match.start()] + replacement + content[match.end():]
        open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
        print("OK — regex-ээр засагдлаа")
    else:
        print("FAILED")