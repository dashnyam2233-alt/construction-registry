path = r"apps\registry\templates\registry\budget_calculator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Дээврийн хуучин select-г орлуулах
old = '''    <div class="field">
      <label>Дээврийн төрөл</label>
      <select name="roof_type" id="sel_roof">
        <option value="Налуу дээвэр (метал)">Налуу — металл черепица</option>
        <option value="Налуу дээвэр (профнастил)">Налуу — профнастил</option>
        <option value="Хавтгай дээвэр">Хавтгай — олон давхар</option>
        <option value="Налуу дээвэр (битум)">Налуу — битум черепица</option>
      </select>
    </div>'''

new = '''    <!-- ДЭЭВРИЙН СИСТЕМ -->
    <div class="field">
      <label>Дээврийн үндсэн хийцлэл</label>
      <select name="roof_structure" id="sel_roof_structure" onchange="updateRoofOptions()">
        <optgroup label="📐 Налуу дээвэр (Гурвалжин)">
          <option value="pitched_wood">🪵 Шувуу нуруу — модон каркас</option>
          <option value="pitched_metal_frame">🔩 Шувуу нуруу — металл каркас</option>
          <option value="pitched_truss">🏗 Ферм дам нуруутай налуу дээвэр</option>
        </optgroup>
        <optgroup label="📋 Хавтгай дээвэр">
          <option value="flat_concrete">🏢 Хавтгай — монолит бетон цутгалт</option>
          <option value="flat_panel">🏢 Хавтгай — угсармал хавтан (ПК)</option>
          <option value="flat_sandwich">🏭 Хавтгай — сэндвич хавтан</option>
        </optgroup>
      </select>
    </div>

    <!-- Налуу дээврийн материал -->
    <div id="pitched_options" style="display:block;">
      <div class="field">
        <label>Дээврийн хучилтын материал</label>
        <select name="roof_cover" id="sel_roof_cover">
          <optgroup label="🔩 Металл">
            <option value="Металл черепица">Металл черепица — элбэг хэрэглэгддэг</option>
            <option value="Профнастил">Профнастил — хямд, агуулах</option>
            <option value="Декра дээвэр">Декра дээвэр — чанартай</option>
            <option value="Сэндвич хавтан налуу">Сэндвич хавтан — дулаан</option>
          </optgroup>
          <optgroup label="🧱 Уламжлалт">
            <option value="Битумен черепица">Битумен черепица — чимэглэлтэй</option>
            <option value="Керамик черепица">Керамик черепица — удаан эдэлгээ</option>
            <option value="Ваар">Ваар дээвэр — уламжлалт</option>
          </optgroup>
        </select>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Дулаалга (крокс хооронд)</label>
          <select name="roof_insulation">
            <option value="Шилэн хөвөн 150мм" selected>Шилэн хөвөн 150мм — стандарт</option>
            <option value="Базальт хөвөн 150мм">Базальт хөвөн 150мм — дулаан</option>
            <option value="Хөөсөнцөр 100мм">Хөөсөнцөр 100мм — хямд</option>
            <option value="XPS 100мм">XPS 100мм — усанд тэсвэртэй</option>
            <option value="Байхгүй">Дулаалгагүй</option>
          </select>
        </div>
        <div class="field">
          <label>Уур, ус тусгаарлагч</label>
          <select name="roof_membrane">
            <option value="Мембран + уур тусгаарлагч" selected>Мембран + уур тусгаарлагч</option>
            <option value="Технониколь мембран">Технониколь мембран</option>
            <option value="Рубероид 2 үе">Рубероид 2 үе — хямд</option>
            <option value="Байхгүй">Байхгүй</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Налуугийн өнцөг</label>
          <select name="roof_angle">
            <option value="15-20">15-20° — бага налуу</option>
            <option value="25-35" selected>25-35° — стандарт</option>
            <option value="40-45">40-45° — огцом</option>
            <option value="mansard">Мансард хийцтэй</option>
          </select>
        </div>
        <div class="field">
          <label>Агааржуулалт</label>
          <select name="roof_ventilation">
            <option value="байна" selected>Агааржуулалтын завсартай</option>
            <option value="байхгүй">Агааржуулалтгүй</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Хавтгай дээврийн материал -->
    <div id="flat_options" style="display:none;">
      <div class="field">
        <label>Ус тусгаарлалтын материал</label>
        <select name="flat_roof_waterproof">
          <optgroup label="🔥 Хайлуулдаг материал">
            <option value="Технониколь 2 үе" selected>Технониколь 2 үе — стандарт</option>
            <option value="Технониколь Техноэласт">Техноэласт — өндөр чанар</option>
            <option value="Хар цаасан 2 үе">Хар цаасан (рубероид) 2 үе — хямд</option>
          </optgroup>
          <optgroup label="🌊 Мембран">
            <option value="ТПО мембран">ТПО мембран — урт эдэлгээ</option>
            <option value="ПВХ мембран">ПВХ мембран</option>
            <option value="ЭПДМ мембран">ЭПДМ мембран — резин</option>
          </optgroup>
          <optgroup label="🔧 Бусад">
            <option value="Полиуретан цацалт">Полиуретан цацалт — завсаргүй</option>
            <option value="Битум эмульс">Битум эмульс</option>
          </optgroup>
        </select>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Дулаалга (хавтгай дээвэр)</label>
          <select name="flat_roof_insulation">
            <option value="XPS 150мм" selected>XPS 150мм — стандарт</option>
            <option value="Шилэн хөвөн 200мм">Шилэн хөвөн 200мм</option>
            <option value="Базальт хөвөн 200мм">Базальт хөвөн 200мм</option>
            <option value="Хөөсөнцөр 150мм">Хөөсөнцөр 150мм — хямд</option>
            <option value="EPS хавтан 200мм">EPS хавтан 200мм</option>
          </select>
        </div>
        <div class="field">
          <label>Уур тусгаарлагч (доод давхарга)</label>
          <select name="flat_roof_vapor">
            <option value="Рубероид 1 үе" selected>Рубероид 1 үе</option>
            <option value="Технониколь уур тусгаарлагч">Технониколь уур тусгаарлагч</option>
            <option value="Полиэтилен хальс">Полиэтилен хальс</option>
          </select>
        </div>
      </div>

      <div class="field">
        <label>Хавтгай дээврийн нэмэлт шийдэл</label>
        <select name="flat_roof_extra">
          <option value="энгийн" selected>Энгийн хавтгай дээвэр</option>
          <option value="ногоон">Ногоон дээвэр (газар тариалан)</option>
          <option value="зогсоол">Машины зогсоол дээвэр</option>
          <option value="террас">Террас, амралтын талбай</option>
        </select>
      </div>
    </div>

    <!-- Нийтлэг -->
    <div class="field" id="sel_roof" style="display:none;">
      <input type="hidden" name="roof_type" id="roof_type_hidden" value="Налуу дээвэр (метал)">
    </div>'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK - дээврийн сонголт нэмэгдлээ")
else:
    print("NOT FOUND")
    # Харьцуулах
    idx = content.find('sel_roof')
    if idx >= 0:
        print(repr(content[idx-100:idx+200]))

# JavaScript-д updateRoofOptions функц нэмэх
old_js = "// ============================================================\n// WIZARD NAVIGATION"
new_js = """// ============================================================
// ДЭЭВРИЙН СОНГОЛТ
// ============================================================
function updateRoofOptions() {
  const structure = document.getElementById('sel_roof_structure').value;
  const isFlat = structure.startsWith('flat_');
  document.getElementById('pitched_options').style.display = isFlat ? 'none' : 'block';
  document.getElementById('flat_options').style.display = isFlat ? 'block' : 'none';

  // roof_type_hidden update
  const cover = document.getElementById('sel_roof_cover');
  let roofType = 'Налуу дээвэр (метал)';
  if(isFlat) {
    roofType = 'Хавтгай дээвэр';
  } else if(cover) {
    roofType = cover.value;
  }
  document.getElementById('roof_type_hidden').value = roofType;
}

// roof_cover өөрчлөхөд hidden update
document.addEventListener('DOMContentLoaded', function() {
  const cover = document.getElementById('sel_roof_cover');
  if(cover) {
    cover.addEventListener('change', function() {
      document.getElementById('roof_type_hidden').value = this.value;
    });
  }
  // Автомат init
  updateRoofOptions();
});

// ============================================================
// WIZARD NAVIGATION"""

if old_js in content:
    content = content.replace(old_js, new_js, 1)
    print("OK - JS нэмэгдлээ")
else:
    print("JS NOT FOUND")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("DONE")