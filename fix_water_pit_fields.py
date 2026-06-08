path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\templates\registry\budget_calculator.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old = """    <div id="eng-water_pit" style="display:none;">
      <div class="field-row">
        <div><label class="field-label">Диаметр (м)</label><input type="number" id="eng-diameter" value="1.5" step="0.1" class="form-inp"></div>
        <div><label class="field-label">Гүн (м)</label><input type="number" id="eng-depth2" value="3.0" step="0.1" class="form-inp"></div>
      </div>
    </div>"""

new = """    <div id="eng-water_pit" style="display:none;">
      <div class="field-row">
        <div><label class="field-label">Тоо ширхэг</label><input type="number" id="eng-water-count" value="1" min="1" class="form-inp"></div>
        <div><label class="field-label">Диаметр (м)</label><input type="number" id="eng-diameter" value="1.5" step="0.1" class="form-inp"></div>
      </div>
      <div class="field-row">
        <div><label class="field-label">Гүн (м)</label><input type="number" id="eng-depth2" value="3.0" step="0.1" class="form-inp"></div>
        <div><label class="field-label">Бурхуулийн материал</label>
          <select id="eng-cover" class="form-inp">
            <option value="бетон">Бетон цутгамал</option>
            <option value="тоосго">Тоосго</option>
            <option value="цагираг">Бетон цагираг (КС)</option>
          </select>
        </div>
      </div>
    </div>"""

if old in content:
    content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Усны худгийн field-үүд нэмэгдлээ")
else:
    print("❌ Олдсонгүй")