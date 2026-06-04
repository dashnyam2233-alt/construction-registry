content = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").read()

old = '''    {% if category == 'material' %}
    <div class="sb-card">
      <div class="sb-hd">🧱 Материалын ангилал</div>
      <div class="sb-body">
        <a href="/ads/?cat=material" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=material&subcat=foundation" class="subcat-link {% if subcat == 'foundation' %}on{% endif %}">🏗 Барилгын үндсэн хийц</a>
        <a href="/ads/?cat=material&subcat=interior" class="subcat-link {% if subcat == 'interior' %}on{% endif %}">🎨 Засал чимэглэл</a>
        <a href="/ads/?cat=material&subcat=outdoor" class="subcat-link {% if subcat == 'outdoor' %}on{% endif %}">🌿 Гадна тохижилт</a>
        <a href="/ads/?cat=material&subcat=plumbing" class="subcat-link {% if subcat == 'plumbing' %}on{% endif %}">🚿 Сан, халаалт</a>
        <a href="/ads/?cat=material&subcat=electrical" class="subcat-link {% if subcat == 'electrical' %}on{% endif %}">⚡ Цахилгаан, холбоо</a>
        <a href="/ads/?cat=material&subcat=machinery" class="subcat-link {% if subcat == 'machinery' %}on{% endif %}">🔩 Машин, тоног</a>
        <a href="/ads/?cat=material&subcat=furniture" class="subcat-link {% if subcat == 'furniture' %}on{% endif %}">🪑 Тавилга</a>
        <a href="/ads/?cat=material&subcat=software" class="subcat-link {% if subcat == 'software' %}on{% endif %}">💻 Программ, ном</a>
        <a href="/ads/?cat=material&subcat=safety" class="subcat-link {% if subcat == 'safety' %}on{% endif %}">🦺 ХАБЭА</a>
      </div>
    </div>'''

new = '''    {% if category == 'material' %}
    <div class="sb-card">
      <div class="sb-hd">🧱 Материалын ангилал</div>
      <div class="sb-body">
        <a href="/ads/?cat=material" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд материал</a>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == 'foundation' %}on{% endif %}" onclick="toggleAcc(this)">
            🏗 Барилгын үндсэн хийц <span class="acc-arr">▶</span>
          </div>
          <div class="acc-body {% if subcat == 'foundation' %}show{% endif %}">
            <a href="/ads/?cat=material&subcat=foundation" class="item-link {% if subcat == 'foundation' and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=foundation&item=rebar" class="item-link {% if item == 'rebar' %}on{% endif %}">Арматур төмөр</a>
            <a href="/ads/?cat=material&subcat=foundation&item=metal_structure" class="item-link {% if item == 'metal_structure' %}on{% endif %}">Металь хийц</a>
            <a href="/ads/?cat=material&subcat=foundation&item=concrete" class="item-link {% if item == 'concrete' %}on{% endif %}">Бетон зуурмаг</a>
            <a href="/ads/?cat=material&subcat=foundation&item=insulation" class="item-link {% if item == 'insulation' %}on{% endif %}">Дулаан дуу тусгаарлах</a>
            <a href="/ads/?cat=material&subcat=foundation&item=roof_material" class="item-link {% if item == 'roof_material' %}on{% endif %}">Дээврийн материал</a>
            <a href="/ads/?cat=material&subcat=foundation&item=formwork" class="item-link {% if item == 'formwork' %}on{% endif %}">Хэв хашмал</a>
            <a href="/ads/?cat=material&subcat=foundation&item=brick_block" class="item-link {% if item == 'brick_block' %}on{% endif %}">Тоосго блок</a>
            <a href="/ads/?cat=material&subcat=foundation&item=wood" class="item-link {% if item == 'wood' %}on{% endif %}">Модон материал</a>
            <a href="/ads/?cat=material&subcat=foundation&item=door_window" class="item-link {% if item == 'door_window' %}on{% endif %}">Цонх хаалга</a>
            <a href="/ads/?cat=material&subcat=foundation&item=glass" class="item-link {% if item == 'glass' %}on{% endif %}">Шилэн хийц</a>
            <a href="/ads/?cat=material&subcat=foundation&item=cement_lime" class="item-link {% if item == 'cement_lime' %}on{% endif %}">Цемент шохой</a>
            <a href="/ads/?cat=material&subcat=foundation&item=sand_gravel" class="item-link {% if item == 'sand_gravel' %}on{% endif %}">Элс хайрга дайрга</a>
            <a href="/ads/?cat=material&subcat=foundation&item=facade" class="item-link {% if item == 'facade' %}on{% endif %}">Гадна фасад</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == 'interior' %}on{% endif %}" onclick="toggleAcc(this)">
            🎨 Засал чимэглэл <span class="acc-arr">▶</span>
          </div>
          <div class="acc-body {% if subcat == 'interior' %}show{% endif %}">
            <a href="/ads/?cat=material&subcat=interior" class="item-link {% if subcat == 'interior' and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=interior&item=paint" class="item-link {% if item == 'paint' %}on{% endif %}">Будаг эмульс</a>
            <a href="/ads/?cat=material&subcat=interior&item=dry_mix" class="item-link {% if item == 'dry_mix' %}on{% endif %}">Хуурай хольц</a>
            <a href="/ads/?cat=material&subcat=interior&item=wallpaper" class="item-link {% if item == 'wallpaper' %}on{% endif %}">Обой хуулга</a>
            <a href="/ads/?cat=material&subcat=interior&item=parquet" class="item-link {% if item == 'parquet' %}on{% endif %}">Паркет ламинат</a>
            <a href="/ads/?cat=material&subcat=interior&item=floor_accessories" class="item-link {% if item == 'floor_accessories' %}on{% endif %}">Шал дагалдах</a>
            <a href="/ads/?cat=material&subcat=interior&item=tile_stone" class="item-link {% if item == 'tile_stone' %}on{% endif %}">Плита чулуу</a>
            <a href="/ads/?cat=material&subcat=interior&item=decoration" class="item-link {% if item == 'decoration' %}on{% endif %}">Гоёл чимэглэл</a>
            <a href="/ads/?cat=material&subcat=interior&item=curtain" class="item-link {% if item == 'curtain' %}on{% endif %}">Хөшиг тюль</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == 'outdoor' %}on{% endif %}" onclick="toggleAcc(this)">
            🌿 Гадна тохижилт <span class="acc-arr">▶</span>
          </div>
          <div class="acc-body {% if subcat == 'outdoor' %}show{% endif %}">
            <a href="/ads/?cat=material&subcat=outdoor" class="item-link {% if subcat == 'outdoor' and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=paving" class="item-link {% if item == 'paving' %}on{% endif %}">Замын хавтан болон бродюр</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=fence_gate" class="item-link {% if item == 'fence_gate' %}on{% endif %}">Хашаа гадна хаалга</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=playground" class="item-link {% if item == 'playground' %}on{% endif %}">Хүүхдийн тоглоом талбай</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=landscaping" class="item-link {% if item == 'landscaping' %}on{% endif %}">Мод зүлэгжүүлэлт</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=cleaning" class="item-link {% if item == 'cleaning' %}on{% endif %}">Цэвэрлэгээ тоног төхөөрөмж</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == 'plumbing' %}on{% endif %}" onclick="toggleAcc(this)">
            🚿 Сан, халаалт, агааржуулалт <span class="acc-arr">▶</span>
          </div>
          <div class="acc-body {% if subcat == 'plumbing' %}show{% endif %}">
            <a href="/ads/?cat=material&subcat=plumbing" class="item-link {% if subcat == 'plumbing' and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=pipe_fitting" class="item-link {% if item == 'pipe_fitting' %}on{% endif %}">Шугам хоолой холбох хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=heating" class="item-link {% if item == 'heating' %}on{% endif %}">Халаах хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=sanitary" class="item-link {% if item == 'sanitary' %}on{% endif %}">Угаалтуур суултуур ванн</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=ventilation" class="item-link {% if item == 'ventilation' %}on{% endif %}">Агааржуулалт хөргөлт</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == 'electrical' %}on{% endif %}" onclick="toggleAcc(this)">
            ⚡ Цахилгаан, холбоо, дохиолол <span class="acc-arr">▶</span>
          </div>
          <div class="acc-body {% if subcat == 'electrical' %}show{% endif %}">
            <a href="/ads/?cat=material&subcat=electrical" class="item-link {% if subcat == 'electrical' and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=electrical&item=wire_cable" class="item-link {% if item == 'wire_cable' %}on{% endif %}">Цахилгааны утас кабель</a>
            <a href="/ads/?cat=material&subcat=electrical&item=electrical_fitting" class="item-link {% if item == 'electrical_fitting' %}on{% endif %}">Цахилгаан холбох хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=electrical&item=lighting" class="item-link {% if item == 'lighting' %}on{% endif %}">Гэрэл гэрэлтүүлэг</a>
            <a href="/ads/?cat=material&subcat=electrical&item=generator_meter" class="item-link {% if item == 'generator_meter' %}on{% endif %}">Цахилгааны үүсгүүр тоолуур</a>
            <a href="/ads/?cat=material&subcat=electrical&item=switch_socket" class="item-link {% if item == 'switch_socket' %}on{% endif %}">Унтраалга залгуур</a>
            <a href="/ads/?cat=material&subcat=electrical&item=signal" class="item-link {% if item == 'signal' %}on{% endif %}">Холбоо дохиолол</a>
            <a href="/ads/?cat=material&subcat=electrical&item=fire_alarm" class="item-link {% if item == 'fire_alarm' %}on{% endif %}">Галын дохиолол</a>
            <a href="/ads/?cat=material&subcat=electrical&item=domophone" class="item-link {% if item == 'domophone' %}on{% endif %}">Домофон ухаалаг цоож</a>
            <a href="/ads/?cat=material&subcat=electrical&item=internet_tv" class="item-link {% if item == 'internet_tv' %}on{% endif %}">Интернэт ТВ</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == 'machinery' %}on{% endif %}" onclick="toggleAcc(this)">
            🔩 Машин механизм тоног төхөөрөмж <span class="acc-arr">▶</span>
          </div>
          <div class="acc-body {% if subcat == 'machinery' %}show{% endif %}">
            <a href="/ads/?cat=material&subcat=machinery" class="item-link {% if subcat == 'machinery' and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=machinery&item=machine" class="item-link {% if item == 'machine' %}on{% endif %}">Машин механизм</a>
            <a href="/ads/?cat=material&subcat=machinery&item=construction_equipment" class="item-link {% if item == 'construction_equipment' %}on{% endif %}">Барилгын тоног төхөөрөмж</a>
            <a href="/ads/?cat=material&subcat=machinery&item=tools" class="item-link {% if item == 'tools' %}on{% endif %}">Барилгын багаж хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=machinery&item=elevator" class="item-link {% if item == 'elevator' %}on{% endif %}">Лифт угсардаг шат</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == 'furniture' %}on{% endif %}" onclick="toggleAcc(this)">
            🪑 Тавилга <span class="acc-arr">▶</span>
          </div>
          <div class="acc-body {% if subcat == 'furniture' %}show{% endif %}">
            <a href="/ads/?cat=material&subcat=furniture" class="item-link {% if subcat == 'furniture' and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=furniture&item=office" class="item-link {% if item == 'office' %}on{% endif %}">Албан тасалгаа</a>
            <a href="/ads/?cat=material&subcat=furniture&item=household" class="item-link {% if item == 'household' %}on{% endif %}">Гэр ахуй</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == 'software' %}on{% endif %}" onclick="toggleAcc(this)">
            💻 Программ хангамж ном гарын авлага <span class="acc-arr">▶</span>
          </div>
          <div class="acc-body {% if subcat == 'software' %}show{% endif %}">
            <a href="/ads/?cat=material&subcat=software" class="item-link {% if subcat == 'software' and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=software&item=software_item" class="item-link {% if item == 'software_item' %}on{% endif %}">Программ хангамж</a>
            <a href="/ads/?cat=material&subcat=software&item=book" class="item-link {% if item == 'book' %}on{% endif %}">Ном сэтгүүл</a>
            <a href="/ads/?cat=material&subcat=software&item=manual" class="item-link {% if item == 'manual' %}on{% endif %}">Гарын авлага</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == 'safety' %}on{% endif %}" onclick="toggleAcc(this)">
            🦺 ХАБЭА <span class="acc-arr">▶</span>
          </div>
          <div class="acc-body {% if subcat == 'safety' %}show{% endif %}">
            <a href="/ads/?cat=material&subcat=safety" class="item-link {% if subcat == 'safety' and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=safety&item=safety_equipment" class="item-link {% if item == 'safety_equipment' %}on{% endif %}">ХАБЭА хэрэгсэл</a>
          </div>
        </div>

      </div>
    </div>'''

# CSS нэмэх
old_css = '    .item-link.on{color:#854d0e;font-weight:500;}'
new_css = '''    .item-link.on{color:#854d0e;font-weight:500;}
    .acc-item{margin-bottom:2px;}
    .acc-hd{display:flex;align-items:center;justify-content:space-between;padding:7px 8px;border-radius:6px;font-size:12px;color:#374151;cursor:pointer;font-weight:500;}
    .acc-hd:hover{background:#f8fafc;}
    .acc-hd.on{background:#fef3c7;color:#854d0e;}
    .acc-arr{font-size:10px;transition:transform 0.2s;color:#94a3b8;}
    .acc-body{display:none;flex-direction:column;padding-left:10px;margin-top:2px;}
    .acc-body.show{display:flex;}
    .acc-body .item-link{font-size:11px;color:#64748b;padding:4px 8px;border-radius:5px;}
    .acc-body .item-link:hover{background:#f1f5f9;color:#1e293b;}
    .acc-body .item-link.on{color:#854d0e;background:#fef9ec;font-weight:500;}'''

# JS нэмэх
old_js = '</script>'
new_js = '''
function toggleAcc(el) {
  const body = el.nextElementSibling;
  const arr = el.querySelector('.acc-arr');
  const isOpen = body.classList.contains('show');
  document.querySelectorAll('.acc-body').forEach(b => b.classList.remove('show'));
  document.querySelectorAll('.acc-hd').forEach(h => {
    h.classList.remove('on');
    const a = h.querySelector('.acc-arr');
    if (a) a.style.transform = '';
  });
  if (!isOpen) {
    body.classList.add('show');
    el.classList.add('on');
    if (arr) arr.style.transform = 'rotate(90deg)';
  }
}

// Одоогийн subcat-г автоматаар нээх
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.acc-hd.on').forEach(function(hd) {
    const body = hd.nextElementSibling;
    const arr = hd.querySelector('.acc-arr');
    if (body) body.classList.add('show');
    if (arr) arr.style.transform = 'rotate(90deg)';
  });
});
</script>'''

if old in content:
    content = content.replace(old, new, 1)
    content = content.replace(old_css, new_css, 1)
    content = content.replace(old_js, new_js, 1)
    open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")