content = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").read()

NEW_SIDEBARS = """    {% if category == "material" %}
    <div class="sb-card">
      <div class="sb-hd">🧱 Материалын ангилал</div>
      <div class="sb-body">
        <a href="/ads/?cat=material" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "foundation" %}on{% endif %}" onclick="toggleAcc(this)"><span>🏗 Барилгын үндсэн хийц</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=foundation" class="item-link {% if subcat == "foundation" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=foundation&item=rebar" class="item-link {% if item == "rebar" %}on{% endif %}">Арматур төмөр</a>
            <a href="/ads/?cat=material&subcat=foundation&item=metal_structure" class="item-link {% if item == "metal_structure" %}on{% endif %}">Металь хийц</a>
            <a href="/ads/?cat=material&subcat=foundation&item=concrete" class="item-link {% if item == "concrete" %}on{% endif %}">Бетон зуурмаг</a>
            <a href="/ads/?cat=material&subcat=foundation&item=insulation" class="item-link {% if item == "insulation" %}on{% endif %}">Дулаан дуу тусгаарлах</a>
            <a href="/ads/?cat=material&subcat=foundation&item=roof_material" class="item-link {% if item == "roof_material" %}on{% endif %}">Дээврийн материал</a>
            <a href="/ads/?cat=material&subcat=foundation&item=formwork" class="item-link {% if item == "formwork" %}on{% endif %}">Хэв хашмал</a>
            <a href="/ads/?cat=material&subcat=foundation&item=brick_block" class="item-link {% if item == "brick_block" %}on{% endif %}">Тоосго блок</a>
            <a href="/ads/?cat=material&subcat=foundation&item=wood" class="item-link {% if item == "wood" %}on{% endif %}">Модон материал</a>
            <a href="/ads/?cat=material&subcat=foundation&item=door_window" class="item-link {% if item == "door_window" %}on{% endif %}">Цонх хаалга</a>
            <a href="/ads/?cat=material&subcat=foundation&item=glass" class="item-link {% if item == "glass" %}on{% endif %}">Шилэн хийц</a>
            <a href="/ads/?cat=material&subcat=foundation&item=cement_lime" class="item-link {% if item == "cement_lime" %}on{% endif %}">Цемент шохой</a>
            <a href="/ads/?cat=material&subcat=foundation&item=sand_gravel" class="item-link {% if item == "sand_gravel" %}on{% endif %}">Элс хайрга дайрга</a>
            <a href="/ads/?cat=material&subcat=foundation&item=facade" class="item-link {% if item == "facade" %}on{% endif %}">Гадна фасад</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "interior" %}on{% endif %}" onclick="toggleAcc(this)"><span>🎨 Засал чимэглэл</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=interior" class="item-link {% if subcat == "interior" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=interior&item=paint" class="item-link {% if item == "paint" %}on{% endif %}">Будаг эмульс</a>
            <a href="/ads/?cat=material&subcat=interior&item=dry_mix" class="item-link {% if item == "dry_mix" %}on{% endif %}">Хуурай хольц</a>
            <a href="/ads/?cat=material&subcat=interior&item=wallpaper" class="item-link {% if item == "wallpaper" %}on{% endif %}">Обой хуулга</a>
            <a href="/ads/?cat=material&subcat=interior&item=parquet" class="item-link {% if item == "parquet" %}on{% endif %}">Паркет ламинат</a>
            <a href="/ads/?cat=material&subcat=interior&item=floor_accessories" class="item-link {% if item == "floor_accessories" %}on{% endif %}">Шал дагалдах</a>
            <a href="/ads/?cat=material&subcat=interior&item=tile_stone" class="item-link {% if item == "tile_stone" %}on{% endif %}">Плита чулуу</a>
            <a href="/ads/?cat=material&subcat=interior&item=decoration" class="item-link {% if item == "decoration" %}on{% endif %}">Гоёл чимэглэл</a>
            <a href="/ads/?cat=material&subcat=interior&item=curtain" class="item-link {% if item == "curtain" %}on{% endif %}">Хөшиг тюль</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "outdoor" %}on{% endif %}" onclick="toggleAcc(this)"><span>🌿 Гадна тохижилт</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=outdoor" class="item-link {% if subcat == "outdoor" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=paving" class="item-link {% if item == "paving" %}on{% endif %}">Замын хавтан болон бродюр</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=fence_gate" class="item-link {% if item == "fence_gate" %}on{% endif %}">Хашаа гадна хаалга</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=playground" class="item-link {% if item == "playground" %}on{% endif %}">Хүүхдийн тоглоом талбай</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=landscaping" class="item-link {% if item == "landscaping" %}on{% endif %}">Мод зүлэгжүүлэлт</a>
            <a href="/ads/?cat=material&subcat=outdoor&item=cleaning" class="item-link {% if item == "cleaning" %}on{% endif %}">Цэвэрлэгээ тоног төхөөрөмж</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "plumbing" %}on{% endif %}" onclick="toggleAcc(this)"><span>🚿 Сан, халаалт</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=plumbing" class="item-link {% if subcat == "plumbing" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=pipe_fitting" class="item-link {% if item == "pipe_fitting" %}on{% endif %}">Шугам хоолой холбох хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=heating" class="item-link {% if item == "heating" %}on{% endif %}">Халаах хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=sanitary" class="item-link {% if item == "sanitary" %}on{% endif %}">Угаалтуур суултуур ванн</a>
            <a href="/ads/?cat=material&subcat=plumbing&item=ventilation" class="item-link {% if item == "ventilation" %}on{% endif %}">Агааржуулалт хөргөлт</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "electrical" %}on{% endif %}" onclick="toggleAcc(this)"><span>⚡ Цахилгаан, холбоо</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=electrical" class="item-link {% if subcat == "electrical" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=electrical&item=wire_cable" class="item-link {% if item == "wire_cable" %}on{% endif %}">Цахилгааны утас кабель</a>
            <a href="/ads/?cat=material&subcat=electrical&item=electrical_fitting" class="item-link {% if item == "electrical_fitting" %}on{% endif %}">Цахилгаан холбох хэрэгсэл</a>
            <a href="/ads/?cat=material&subcat=electrical&item=lighting" class="item-link {% if item == "lighting" %}on{% endif %}">Гэрэл гэрэлтүүлэг</a>
            <a href="/ads/?cat=material&subcat=electrical&item=generator_meter" class="item-link {% if item == "generator_meter" %}on{% endif %}">Цахилгааны үүсгүүр тоолуур</a>
            <a href="/ads/?cat=material&subcat=electrical&item=switch_socket" class="item-link {% if item == "switch_socket" %}on{% endif %}">Унтраалга залгуур</a>
            <a href="/ads/?cat=material&subcat=electrical&item=signal" class="item-link {% if item == "signal" %}on{% endif %}">Холбоо дохиолол</a>
            <a href="/ads/?cat=material&subcat=electrical&item=fire_alarm" class="item-link {% if item == "fire_alarm" %}on{% endif %}">Галын дохиолол</a>
            <a href="/ads/?cat=material&subcat=electrical&item=domophone" class="item-link {% if item == "domophone" %}on{% endif %}">Домофон ухаалаг цоож</a>
            <a href="/ads/?cat=material&subcat=electrical&item=internet_tv" class="item-link {% if item == "internet_tv" %}on{% endif %}">Интернэт ТВ</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "furniture" %}on{% endif %}" onclick="toggleAcc(this)"><span>🪑 Тавилга</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=furniture" class="item-link {% if subcat == "furniture" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=furniture&item=office" class="item-link {% if item == "office" %}on{% endif %}">Албан тасалгаа</a>
            <a href="/ads/?cat=material&subcat=furniture&item=household" class="item-link {% if item == "household" %}on{% endif %}">Гэр ахуй</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "software" %}on{% endif %}" onclick="toggleAcc(this)"><span>💻 Программ хангамж, ном</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=software" class="item-link {% if subcat == "software" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=software&item=software_item" class="item-link {% if item == "software_item" %}on{% endif %}">Программ хангамж</a>
            <a href="/ads/?cat=material&subcat=software&item=book" class="item-link {% if item == "book" %}on{% endif %}">Ном сэтгүүл</a>
            <a href="/ads/?cat=material&subcat=software&item=manual" class="item-link {% if item == "manual" %}on{% endif %}">Гарын авлага</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "safety" %}on{% endif %}" onclick="toggleAcc(this)"><span>🦺 ХАБЭА</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=material&subcat=safety" class="item-link {% if subcat == "safety" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=material&subcat=safety&item=safety_equipment" class="item-link {% if item == "safety_equipment" %}on{% endif %}">ХАБЭА хэрэгсэл</a>
          </div>
        </div>
      </div>
    </div>

    {% elif category == "equipment" %}
    <div class="sb-card">
      <div class="sb-hd">🔩 Тоног төхөөрөмж</div>
      <div class="sb-body">
        <a href="/ads/?cat=equipment" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=equipment&subcat=excavator" class="subcat-link {% if subcat == "excavator" %}on{% endif %}">Экскаватор</a>
        <a href="/ads/?cat=equipment&subcat=crane" class="subcat-link {% if subcat == "crane" %}on{% endif %}">Кран</a>
        <a href="/ads/?cat=equipment&subcat=bucket" class="subcat-link {% if subcat == "bucket" %}on{% endif %}">Ковш</a>
        <a href="/ads/?cat=equipment&subcat=iron" class="subcat-link {% if subcat == "iron" %}on{% endif %}">Индүү</a>
        <a href="/ads/?cat=equipment&subcat=concrete_mixer" class="subcat-link {% if subcat == "concrete_mixer" %}on{% endif %}">Бетон зуурагч</a>
        <a href="/ads/?cat=equipment&subcat=generator" class="subcat-link {% if subcat == "generator" %}on{% endif %}">Генератор</a>
        <a href="/ads/?cat=equipment&subcat=compressor" class="subcat-link {% if subcat == "compressor" %}on{% endif %}">Компрессор</a>
        <a href="/ads/?cat=equipment&subcat=welding" class="subcat-link {% if subcat == "welding" %}on{% endif %}">Гагнуурын төхөөрөмж</a>
        <a href="/ads/?cat=equipment&subcat=lifting" class="subcat-link {% if subcat == "lifting" %}on{% endif %}">Өргөх төхөөрөмж</a>
        <a href="/ads/?cat=equipment&subcat=tools" class="subcat-link {% if subcat == "tools" %}on{% endif %}">Барилгын багаж</a>
        <a href="/ads/?cat=equipment&subcat=measuring" class="subcat-link {% if subcat == "measuring" %}on{% endif %}">Хэмжилтийн багаж</a>
        <a href="/ads/?cat=equipment&subcat=warehouse_eq" class="subcat-link {% if subcat == "warehouse_eq" %}on{% endif %}">Агуулахын төхөөрөмж</a>
        <a href="/ads/?cat=equipment&subcat=other_eq" class="subcat-link {% if subcat == "other_eq" %}on{% endif %}">Бусад төхөөрөмж</a>
      </div>
    </div>

    {% elif category == "rental" %}
    <div class="sb-card">
      <div class="sb-hd">🔑 Түрээс</div>
      <div class="sb-body">
        <a href="/ads/?cat=rental" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=rental&subcat=tech_rent" class="subcat-link {% if subcat == "tech_rent" %}on{% endif %}">Техник түрээс</a>
        <a href="/ads/?cat=rental&subcat=tool_rent" class="subcat-link {% if subcat == "tool_rent" %}on{% endif %}">Багаж түрээс</a>
        <a href="/ads/?cat=rental&subcat=scaffold_rent" class="subcat-link {% if subcat == "scaffold_rent" %}on{% endif %}">Скафольд түрээс</a>
        <a href="/ads/?cat=rental&subcat=formwork_rent" class="subcat-link {% if subcat == "formwork_rent" %}on{% endif %}">Хэв хашмал түрээс</a>
        <a href="/ads/?cat=rental&subcat=crane_rent" class="subcat-link {% if subcat == "crane_rent" %}on{% endif %}">Кран түрээс</a>
        <a href="/ads/?cat=rental&subcat=container_rent" class="subcat-link {% if subcat == "container_rent" %}on{% endif %}">Контейнер түрээс</a>
        <a href="/ads/?cat=rental&subcat=office_rent" class="subcat-link {% if subcat == "office_rent" %}on{% endif %}">Оффис түрээс</a>
        <a href="/ads/?cat=rental&subcat=warehouse_rent" class="subcat-link {% if subcat == "warehouse_rent" %}on{% endif %}">Агуулах түрээс</a>
        <a href="/ads/?cat=rental&subcat=machine_rent" class="subcat-link {% if subcat == "machine_rent" %}on{% endif %}">Машин механизм түрээс</a>
        <a href="/ads/?cat=rental&subcat=other_rent" class="subcat-link {% if subcat == "other_rent" %}on{% endif %}">Бусад түрээс</a>
      </div>
    </div>

    {% elif category == "realestate" %}
    <div class="sb-card">
      <div class="sb-hd">🏠 Үл хөдлөх хөрөнгө</div>
      <div class="sb-body">
        <a href="/ads/?cat=realestate" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "rooms" %}on{% endif %}" onclick="toggleAcc(this)"><span>🛏 Өрөөний тоо</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=realestate&subcat=rooms" class="item-link {% if subcat == "rooms" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=realestate&subcat=rooms&item=r1" class="item-link {% if item == "r1" %}on{% endif %}">1 өрөө</a>
            <a href="/ads/?cat=realestate&subcat=rooms&item=r2" class="item-link {% if item == "r2" %}on{% endif %}">2 өрөө</a>
            <a href="/ads/?cat=realestate&subcat=rooms&item=r3" class="item-link {% if item == "r3" %}on{% endif %}">3 өрөө</a>
            <a href="/ads/?cat=realestate&subcat=rooms&item=r3plus" class="item-link {% if item == "r3plus" %}on{% endif %}">3-аас дээш өрөө</a>
            <a href="/ads/?cat=realestate&subcat=rooms&item=duplex" class="item-link {% if item == "duplex" %}on{% endif %}">Дуплекс</a>
            <a href="/ads/?cat=realestate&subcat=rooms&item=studio" class="item-link {% if item == "studio" %}on{% endif %}">Студи</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "ub" %}on{% endif %}" onclick="toggleAcc(this)"><span>🏙 Улаанбаатар</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=realestate&subcat=ub" class="item-link {% if subcat == "ub" and not item %}on{% endif %}">— Бүгд дүүрэг</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=bgd" class="item-link {% if item == "bgd" %}on{% endif %}">Баянгол дүүрэг</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=bzd" class="item-link {% if item == "bzd" %}on{% endif %}">Баянзүрх дүүрэг</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=sbd" class="item-link {% if item == "sbd" %}on{% endif %}">Сүхбаатар дүүрэг</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=hud" class="item-link {% if item == "hud" %}on{% endif %}">Хан-Уул дүүрэг</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=chd" class="item-link {% if item == "chd" %}on{% endif %}">Чингэлтэй дүүрэг</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=shd" class="item-link {% if item == "shd" %}on{% endif %}">Сонгинохайрхан</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=nld" class="item-link {% if item == "nld" %}on{% endif %}">Налайх дүүрэг</a>
            <a href="/ads/?cat=realestate&subcat=ub&item=bnd" class="item-link {% if item == "bnd" %}on{% endif %}">Багануур дүүрэг</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "province" %}on{% endif %}" onclick="toggleAcc(this)"><span>🗺 Орон нутаг</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=realestate&subcat=province" class="item-link {% if subcat == "province" and not item %}on{% endif %}">— Бүгд аймаг</a>
            <a href="/ads/?cat=realestate&subcat=province&item=arkhangai" class="item-link {% if item == "arkhangai" %}on{% endif %}">Архангай</a>
            <a href="/ads/?cat=realestate&subcat=province&item=darkhan" class="item-link {% if item == "darkhan" %}on{% endif %}">Дархан-Уул</a>
            <a href="/ads/?cat=realestate&subcat=province&item=orkhon" class="item-link {% if item == "orkhon" %}on{% endif %}">Орхон</a>
            <a href="/ads/?cat=realestate&subcat=province&item=selenge" class="item-link {% if item == "selenge" %}on{% endif %}">Сэлэнгэ</a>
            <a href="/ads/?cat=realestate&subcat=province&item=tuv" class="item-link {% if item == "tuv" %}on{% endif %}">Төв</a>
            <a href="/ads/?cat=realestate&subcat=province&item=other_province" class="item-link {% if item == "other_province" %}on{% endif %}">Бусад аймаг</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "re_type" %}on{% endif %}" onclick="toggleAcc(this)"><span>🏷 Зарын төрөл</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=realestate&subcat=re_type&item=apartment" class="item-link {% if item == "apartment" %}on{% endif %}">Орон сууц</a>
            <a href="/ads/?cat=realestate&subcat=re_type&item=house" class="item-link {% if item == "house" %}on{% endif %}">Амины орон сууц</a>
            <a href="/ads/?cat=realestate&subcat=re_type&item=office_re" class="item-link {% if item == "office_re" %}on{% endif %}">Оффис</a>
            <a href="/ads/?cat=realestate&subcat=re_type&item=commercial" class="item-link {% if item == "commercial" %}on{% endif %}">Үйлчилгээний талбай</a>
            <a href="/ads/?cat=realestate&subcat=re_type&item=warehouse_re" class="item-link {% if item == "warehouse_re" %}on{% endif %}">Агуулах үйлдвэр</a>
            <a href="/ads/?cat=realestate&subcat=re_type&item=land" class="item-link {% if item == "land" %}on{% endif %}">Газар</a>
            <a href="/ads/?cat=realestate&subcat=re_type&item=under_construction" class="item-link {% if item == "under_construction" %}on{% endif %}">Баригдаж буй объект</a>
          </div>
        </div>
      </div>
    </div>

    {% elif category == "service" %}
    <div class="sb-card">
      <div class="sb-hd">🏗 Барилгын үйлчилгээ</div>
      <div class="sb-body">
        <a href="/ads/?cat=service" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=service&subcat=construction_co" class="subcat-link {% if subcat == "construction_co" %}on{% endif %}">Барилгын компани</a>
        <a href="/ads/?cat=service&subcat=interior_svc" class="subcat-link {% if subcat == "interior_svc" %}on{% endif %}">Интерьер</a>
        <a href="/ads/?cat=service&subcat=exterior_svc" class="subcat-link {% if subcat == "exterior_svc" %}on{% endif %}">Экстерьер</a>
        <a href="/ads/?cat=service&subcat=carpenter" class="subcat-link {% if subcat == "carpenter" %}on{% endif %}">Мужаан</a>
        <a href="/ads/?cat=service&subcat=tiler" class="subcat-link {% if subcat == "tiler" %}on{% endif %}">Плитачин</a>
        <a href="/ads/?cat=service&subcat=electrician" class="subcat-link {% if subcat == "electrician" %}on{% endif %}">Цахилгаанчин</a>
        <a href="/ads/?cat=service&subcat=plumber" class="subcat-link {% if subcat == "plumber" %}on{% endif %}">Сантехник</a>
        <a href="/ads/?cat=service&subcat=welder" class="subcat-link {% if subcat == "welder" %}on{% endif %}">Гагнуур</a>
        <a href="/ads/?cat=service&subcat=roofing" class="subcat-link {% if subcat == "roofing" %}on{% endif %}">Дээвэр</a>
        <a href="/ads/?cat=service&subcat=facade_svc" class="subcat-link {% if subcat == "facade_svc" %}on{% endif %}">Фасад</a>
        <a href="/ads/?cat=service&subcat=road_svc" class="subcat-link {% if subcat == "road_svc" %}on{% endif %}">Зам талбай</a>
        <a href="/ads/?cat=service&subcat=cleaning_svc" class="subcat-link {% if subcat == "cleaning_svc" %}on{% endif %}">Цэвэрлэгээ</a>
        <a href="/ads/?cat=service&subcat=demolition" class="subcat-link {% if subcat == "demolition" %}on{% endif %}">Нураалт</a>
        <a href="/ads/?cat=service&subcat=crane_svc" class="subcat-link {% if subcat == "crane_svc" %}on{% endif %}">Өргөлт кран үйлчилгээ</a>
        <a href="/ads/?cat=service&subcat=engineering_svc" class="subcat-link {% if subcat == "engineering_svc" %}on{% endif %}">Инженеринг</a>
        <a href="/ads/?cat=service&subcat=consulting" class="subcat-link {% if subcat == "consulting" %}on{% endif %}">Хяналт зөвлөх</a>
        <a href="/ads/?cat=service&subcat=other_svc" class="subcat-link {% if subcat == "other_svc" %}on{% endif %}">Бусад үйлчилгээ</a>
      </div>
    </div>

    {% elif category == "design" %}
    <div class="sb-card">
      <div class="sb-hd">📐 Зураг төсөв, дизайн</div>
      <div class="sb-body">
        <a href="/ads/?cat=design" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=design&subcat=architecture" class="subcat-link {% if subcat == "architecture" %}on{% endif %}">Архитектур</a>
        <a href="/ads/?cat=design&subcat=interior_design" class="subcat-link {% if subcat == "interior_design" %}on{% endif %}">Интерьер дизайн</a>
        <a href="/ads/?cat=design&subcat=structure" class="subcat-link {% if subcat == "structure" %}on{% endif %}">Конструкц</a>
        <a href="/ads/?cat=design&subcat=engineering_design" class="subcat-link {% if subcat == "engineering_design" %}on{% endif %}">Инженерийн зураг</a>
        <a href="/ads/?cat=design&subcat=visualization" class="subcat-link {% if subcat == "visualization" %}on{% endif %}">3D визуал</a>
        <a href="/ads/?cat=design&subcat=landscape" class="subcat-link {% if subcat == "landscape" %}on{% endif %}">Ландшафт дизайн</a>
        <a href="/ads/?cat=design&subcat=budget" class="subcat-link {% if subcat == "budget" %}on{% endif %}">Төсөв</a>
        <a href="/ads/?cat=design&subcat=render" class="subcat-link {% if subcat == "render" %}on{% endif %}">Render</a>
        <a href="/ads/?cat=design&subcat=other_design" class="subcat-link {% if subcat == "other_design" %}on{% endif %}">Бусад дизайн</a>
      </div>
    </div>

    {% elif category == "worker" %}
    <div class="sb-card">
      <div class="sb-hd">👷 Ажилтан, ажлын зар</div>
      <div class="sb-body">
        <a href="/ads/?cat=worker" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "jobseeker" %}on{% endif %}" onclick="toggleAcc(this)"><span>🙋 Ажил хайгч</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=worker&subcat=jobseeker_engineer" class="item-link {% if subcat == "jobseeker_engineer" %}on{% endif %}">Инженер</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_architect" class="item-link {% if subcat == "jobseeker_architect" %}on{% endif %}">Архитектор</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_operator" class="item-link {% if subcat == "jobseeker_operator" %}on{% endif %}">Оператор</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_welder" class="item-link {% if subcat == "jobseeker_welder" %}on{% endif %}">Гагнуурчин</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_carpenter" class="item-link {% if subcat == "jobseeker_carpenter" %}on{% endif %}">Мужаан</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_electrician" class="item-link {% if subcat == "jobseeker_electrician" %}on{% endif %}">Цахилгаанчин</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_plumber" class="item-link {% if subcat == "jobseeker_plumber" %}on{% endif %}">Сантехникч</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_helper" class="item-link {% if subcat == "jobseeker_helper" %}on{% endif %}">Туслах ажилтан</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_brigade" class="item-link {% if subcat == "jobseeker_brigade" %}on{% endif %}">Бригад</a>
            <a href="/ads/?cat=worker&subcat=jobseeker_other" class="item-link {% if subcat == "jobseeker_other" %}on{% endif %}">Бусад</a>
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-hd {% if subcat == "job" %}on{% endif %}" onclick="toggleAcc(this)"><span>💼 Ажлын байр</span><span class="acc-arr">▶</span></div>
          <div class="acc-body">
            <a href="/ads/?cat=worker&subcat=job_engineer" class="item-link {% if subcat == "job_engineer" %}on{% endif %}">Инженер</a>
            <a href="/ads/?cat=worker&subcat=job_field" class="item-link {% if subcat == "job_field" %}on{% endif %}">Талбайн ажилтан</a>
            <a href="/ads/?cat=worker&subcat=job_operator" class="item-link {% if subcat == "job_operator" %}on{% endif %}">Оператор</a>
            <a href="/ads/?cat=worker&subcat=job_estimator" class="item-link {% if subcat == "job_estimator" %}on{% endif %}">Төсөвчин</a>
            <a href="/ads/?cat=worker&subcat=job_pm" class="item-link {% if subcat == "job_pm" %}on{% endif %}">Project manager</a>
            <a href="/ads/?cat=worker&subcat=job_safety" class="item-link {% if subcat == "job_safety" %}on{% endif %}">Safety officer</a>
            <a href="/ads/?cat=worker&subcat=job_other" class="item-link {% if subcat == "job_other" %}on{% endif %}">Бусад</a>
          </div>
        </div>
      </div>
    </div>

    {% elif category == "tender" %}
    <div class="sb-card">
      <div class="sb-hd">📋 Тендер, төсөл</div>
      <div class="sb-body">
        <a href="/ads/?cat=tender" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=tender&subcat=tender_item" class="subcat-link {% if subcat == "tender_item" %}on{% endif %}">Тендер</a>
        <a href="/ads/?cat=tender&subcat=contractor" class="subcat-link {% if subcat == "contractor" %}on{% endif %}">Гүйцэтгэгч хайх</a>
        <a href="/ads/?cat=tender&subcat=subcontractor" class="subcat-link {% if subcat == "subcontractor" %}on{% endif %}">Туслан гүйцэтгэгч</a>
        <a href="/ads/?cat=tender&subcat=investment" class="subcat-link {% if subcat == "investment" %}on{% endif %}">Хөрөнгө оруулалт</a>
        <a href="/ads/?cat=tender&subcat=partnership" class="subcat-link {% if subcat == "partnership" %}on{% endif %}">Хамтран ажиллах</a>
        <a href="/ads/?cat=tender&subcat=new_project" class="subcat-link {% if subcat == "new_project" %}on{% endif %}">Шинэ төсөл</a>
        <a href="/ads/?cat=tender&subcat=tender_other" class="subcat-link {% if subcat == "tender_other" %}on{% endif %}">Бусад</a>
      </div>
    </div>

    {% elif category == "company" %}
    <div class="sb-card">
      <div class="sb-hd">🏢 Компаниуд</div>
      <div class="sb-body">
        <a href="/ads/?cat=company" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=company&subcat=construction_company" class="subcat-link {% if subcat == "construction_company" %}on{% endif %}">Барилгын компани</a>
        <a href="/ads/?cat=company&subcat=material_supplier" class="subcat-link {% if subcat == "material_supplier" %}on{% endif %}">Материал нийлүүлэгч</a>
        <a href="/ads/?cat=company&subcat=equipment_supplier" class="subcat-link {% if subcat == "equipment_supplier" %}on{% endif %}">Тоног нийлүүлэгч</a>
        <a href="/ads/?cat=company&subcat=engineering_co" class="subcat-link {% if subcat == "engineering_co" %}on{% endif %}">Инженеринг</a>
        <a href="/ads/?cat=company&subcat=interior_co" class="subcat-link {% if subcat == "interior_co" %}on{% endif %}">Интерьер</a>
        <a href="/ads/?cat=company&subcat=architecture_co" class="subcat-link {% if subcat == "architecture_co" %}on{% endif %}">Архитектур</a>
        <a href="/ads/?cat=company&subcat=factory" class="subcat-link {% if subcat == "factory" %}on{% endif %}">Үйлдвэр</a>
        <a href="/ads/?cat=company&subcat=rental_co" class="subcat-link {% if subcat == "rental_co" %}on{% endif %}">Түрээс үйлчилгээ</a>
        <a href="/ads/?cat=company&subcat=other_company" class="subcat-link {% if subcat == "other_company" %}on{% endif %}">Бусад компани</a>
      </div>
    </div>

    {% elif category == "other" %}
    <div class="sb-card">
      <div class="sb-hd">📦 Бусад</div>
      <div class="sb-body">
        <a href="/ads/?cat=other" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>
        <a href="/ads/?cat=other&subcat=leftover" class="subcat-link {% if subcat == "leftover" %}on{% endif %}">Үлдэгдэл материал</a>
        <a href="/ads/?cat=other&subcat=warehouse_trade" class="subcat-link {% if subcat == "warehouse_trade" %}on{% endif %}">Агуулахын худалдаа</a>
        <a href="/ads/?cat=other&subcat=used_goods" class="subcat-link {% if subcat == "used_goods" %}on{% endif %}">Хэрэглэсэн бараа</a>
        <a href="/ads/?cat=other&subcat=news" class="subcat-link {% if subcat == "news" %}on{% endif %}">Барилгын мэдээ</a>
        <a href="/ads/?cat=other&subcat=training" class="subcat-link {% if subcat == "training" %}on{% endif %}">Сургалт</a>
        <a href="/ads/?cat=other&subcat=other_misc" class="subcat-link {% if subcat == "other_misc" %}on{% endif %}">Бусад</a>
      </div>
    </div>"""

# Хуучин sidebar-г солих
import re
old_pattern = re.search(r'{% if category == "material" %}.*?{% else %}\s*<div class="sb-card">\s*<div class="sb-hd">📂 Ангилалууд</div>', content, re.DOTALL)

if old_pattern:
    new_content = content[:old_pattern.start()] + NEW_SIDEBARS + '\n    {% else %}\n    <div class="sb-card">\n      <div class="sb-hd">📂 Ангилалууд</div>' + content[old_pattern.end():]
    open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(new_content)
    print("OK — бүх sidebar шинэчлэгдлээ")
else:
    print("NOT FOUND")