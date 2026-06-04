content = open("apps/registry/templates/registry/ad_list.html", "r", encoding="utf-8").read()

house_sidebar = """    {% elif category == "house" %}
    <div class="sb-card">
      <div class="sb-hd">🏠 Орон сууцны ангилал</div>
      <div class="sb-body">
        <a href="/ads/?cat=house" class="subcat-link {% if not subcat %}on{% endif %}">📋 Бүгд</a>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == "rooms" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🛏 Өрөөний тоо</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=house&subcat=rooms" class="item-link {% if subcat == "rooms" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=house&subcat=rooms&item=r1" class="item-link {% if item == "r1" %}on{% endif %}">1 өрөө</a>
            <a href="/ads/?cat=house&subcat=rooms&item=r2" class="item-link {% if item == "r2" %}on{% endif %}">2 өрөө</a>
            <a href="/ads/?cat=house&subcat=rooms&item=r3" class="item-link {% if item == "r3" %}on{% endif %}">3 өрөө</a>
            <a href="/ads/?cat=house&subcat=rooms&item=r3plus" class="item-link {% if item == "r3plus" %}on{% endif %}">3-аас дээш өрөө</a>
            <a href="/ads/?cat=house&subcat=rooms&item=duplex" class="item-link {% if item == "duplex" %}on{% endif %}">Дуплекс</a>
            <a href="/ads/?cat=house&subcat=rooms&item=studio" class="item-link {% if item == "studio" %}on{% endif %}">Студи</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == "ub" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🏙 Улаанбаатар</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=house&subcat=ub" class="item-link {% if subcat == "ub" and not item %}on{% endif %}">— Бүгд дүүрэг</a>
            <a href="/ads/?cat=house&subcat=ub&item=bgd" class="item-link {% if item == "bgd" %}on{% endif %}">Баянгол дүүрэг</a>
            <a href="/ads/?cat=house&subcat=ub&item=bzd" class="item-link {% if item == "bzd" %}on{% endif %}">Баянзүрх дүүрэг</a>
            <a href="/ads/?cat=house&subcat=ub&item=sbd" class="item-link {% if item == "sbd" %}on{% endif %}">Сүхбаатар дүүрэг</a>
            <a href="/ads/?cat=house&subcat=ub&item=hud" class="item-link {% if item == "hud" %}on{% endif %}">Хан-Уул дүүрэг</a>
            <a href="/ads/?cat=house&subcat=ub&item=chd" class="item-link {% if item == "chd" %}on{% endif %}">Чингэлтэй дүүрэг</a>
            <a href="/ads/?cat=house&subcat=ub&item=shd" class="item-link {% if item == "shd" %}on{% endif %}">Сонгинохайрхан дүүрэг</a>
            <a href="/ads/?cat=house&subcat=ub&item=nld" class="item-link {% if item == "nld" %}on{% endif %}">Налайх дүүрэг</a>
            <a href="/ads/?cat=house&subcat=ub&item=bnd" class="item-link {% if item == "bnd" %}on{% endif %}">Багануур дүүрэг</a>
            <a href="/ads/?cat=house&subcat=ub&item=bhd" class="item-link {% if item == "bhd" %}on{% endif %}">Багахангай дүүрэг</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == "province" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🗺 Орон нутаг</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=house&subcat=province" class="item-link {% if subcat == "province" and not item %}on{% endif %}">— Бүгд аймаг</a>
            <a href="/ads/?cat=house&subcat=province&item=arkhangai" class="item-link {% if item == "arkhangai" %}on{% endif %}">Архангай</a>
            <a href="/ads/?cat=house&subcat=province&item=bayan_olgii" class="item-link {% if item == "bayan_olgii" %}on{% endif %}">Баян-Өлгий</a>
            <a href="/ads/?cat=house&subcat=province&item=bayankhongor" class="item-link {% if item == "bayankhongor" %}on{% endif %}">Баянхонгор</a>
            <a href="/ads/?cat=house&subcat=province&item=bulgan" class="item-link {% if item == "bulgan" %}on{% endif %}">Булган</a>
            <a href="/ads/?cat=house&subcat=province&item=gobi_altai" class="item-link {% if item == "gobi_altai" %}on{% endif %}">Говь-Алтай</a>
            <a href="/ads/?cat=house&subcat=province&item=govisumber" class="item-link {% if item == "govisumber" %}on{% endif %}">Говьсүмбэр</a>
            <a href="/ads/?cat=house&subcat=province&item=darkhan" class="item-link {% if item == "darkhan" %}on{% endif %}">Дархан-Уул</a>
            <a href="/ads/?cat=house&subcat=province&item=dornod" class="item-link {% if item == "dornod" %}on{% endif %}">Дорнод</a>
            <a href="/ads/?cat=house&subcat=province&item=dornogobi" class="item-link {% if item == "dornogobi" %}on{% endif %}">Дорноговь</a>
            <a href="/ads/?cat=house&subcat=province&item=dundgobi" class="item-link {% if item == "dundgobi" %}on{% endif %}">Дундговь</a>
            <a href="/ads/?cat=house&subcat=province&item=zavkhan" class="item-link {% if item == "zavkhan" %}on{% endif %}">Завхан</a>
            <a href="/ads/?cat=house&subcat=province&item=orkhon" class="item-link {% if item == "orkhon" %}on{% endif %}">Орхон</a>
            <a href="/ads/?cat=house&subcat=province&item=uvurkhangai" class="item-link {% if item == "uvurkhangai" %}on{% endif %}">Өвөрхангай</a>
            <a href="/ads/?cat=house&subcat=province&item=umnugobi" class="item-link {% if item == "umnugobi" %}on{% endif %}">Өмнөговь</a>
            <a href="/ads/?cat=house&subcat=province&item=sukhbaatar" class="item-link {% if item == "sukhbaatar" %}on{% endif %}">Сүхбаатар</a>
            <a href="/ads/?cat=house&subcat=province&item=selenge" class="item-link {% if item == "selenge" %}on{% endif %}">Сэлэнгэ</a>
            <a href="/ads/?cat=house&subcat=province&item=tuv" class="item-link {% if item == "tuv" %}on{% endif %}">Төв</a>
            <a href="/ads/?cat=house&subcat=province&item=uvs" class="item-link {% if item == "uvs" %}on{% endif %}">Увс</a>
            <a href="/ads/?cat=house&subcat=province&item=khovd" class="item-link {% if item == "khovd" %}on{% endif %}">Ховд</a>
            <a href="/ads/?cat=house&subcat=province&item=khuvsgul" class="item-link {% if item == "khuvsgul" %}on{% endif %}">Хөвсгөл</a>
            <a href="/ads/?cat=house&subcat=province&item=khentii" class="item-link {% if item == "khentii" %}on{% endif %}">Хэнтий</a>
          </div>
        </div>

        <div class="acc-item">
          <div class="acc-hd {% if subcat == "type" %}on{% endif %}" onclick="toggleAcc(this)">
            <span>🏷 Зарын төрөл</span><span class="acc-arr">▶</span>
          </div>
          <div class="acc-body">
            <a href="/ads/?cat=house&subcat=type" class="item-link {% if subcat == "type" and not item %}on{% endif %}">— Бүгд</a>
            <a href="/ads/?cat=house&subcat=type&item=sale" class="item-link {% if item == "sale" %}on{% endif %}">Зарна</a>
            <a href="/ads/?cat=house&subcat=type&item=rent" class="item-link {% if item == "rent" %}on{% endif %}">Түрээслэнэ</a>
            <a href="/ads/?cat=house&subcat=type&item=buy" class="item-link {% if item == "buy" %}on{% endif %}">Худалдаж авна</a>
            <a href="/ads/?cat=house&subcat=type&item=rent_partial" class="item-link {% if item == "rent_partial" %}on{% endif %}">Хэсэгчлэн түрээслэнэ</a>
          </div>
        </div>

      </div>
    </div>"""

# {% else %} хэсгийн өмнө нэмэх
old = '    {% else %}\n    <div class="sb-card">\n      <div class="sb-hd">📂 Ангилалууд</div>'
new = house_sidebar + '\n    {% else %}\n    <div class="sb-card">\n      <div class="sb-hd">📂 Ангилалууд</div>'

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8").write(content)
    print("OK — орон сууцны sidebar нэмэгдлээ")
else:
    print("NOT FOUND")