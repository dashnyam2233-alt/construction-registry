html = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI Төсөв Тооцоолох — БНБ</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f1f5f9;}
    a{text-decoration:none;color:inherit;}
    .nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;position:sticky;top:0;z-index:1000;}
    .logo-t{color:#fff;font-size:13px;font-weight:700;}
    .nav-r{margin-left:auto;display:flex;gap:8px;}
    .nb{padding:5px 12px;border-radius:6px;font-size:12px;font-weight:500;border:1px solid #2d4f63;color:#cbd5e1;background:transparent;}
    .hero{background:linear-gradient(135deg,#1e3a4a,#2f6477);padding:24px 20px;text-align:center;}
    .hero-t{color:#fff;font-size:20px;font-weight:700;margin-bottom:6px;}
    .hero-s{color:#94a3b8;font-size:13px;}
    .wrap{max-width:680px;margin:24px auto;padding:0 20px;}

    /* Progress */
    .progress{display:flex;align-items:center;margin-bottom:20px;}
    .step-dot{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0;border:2px solid #e2e8f0;background:#fff;color:#94a3b8;cursor:pointer;transition:all 0.2s;}
    .step-dot.active{background:#f59e0b;border-color:#f59e0b;color:#1e3a4a;}
    .step-dot.done{background:#22c55e;border-color:#22c55e;color:#fff;}
    .step-line{flex:1;height:2px;background:#e2e8f0;}
    .step-line.done{background:#22c55e;}

    /* Card */
    .card{background:#fff;border:0.5px solid #e2e8f0;border-radius:12px;padding:24px;}
    .step-title{font-size:16px;font-weight:700;color:#1e293b;margin-bottom:4px;}
    .step-desc{font-size:12px;color:#64748b;margin-bottom:20px;}
    
    /* Fields */
    .field{margin-bottom:14px;}
    .field label{display:block;font-size:12px;font-weight:600;color:#4a5568;margin-bottom:5px;}
    .field select,.field input{width:100%;padding:9px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:13px;color:#1e293b;outline:none;background:#fff;}
    .field select:focus,.field input:focus{border-color:#f59e0b;}
    .field-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
    .field-row3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;}
    .field-hint{font-size:11px;color:#94a3b8;margin-top:3px;}

    /* Buttons */
    .btn-row{display:flex;gap:10px;margin-top:20px;}
    .btn-next{flex:1;padding:11px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;}
    .btn-next:hover{background:#e08c00;}
    .btn-prev{padding:11px 20px;background:#f1f5f9;color:#64748b;border:none;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;}
    .btn-prev:hover{background:#e2e8f0;}
    .btn-calc{flex:1;padding:11px;background:#22c55e;color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;}
    .btn-calc:hover{background:#16a34a;}

    /* Result */
    .loading{display:none;text-align:center;padding:50px 20px;}
    .loading.show{display:block;}
    .spinner{width:48px;height:48px;border:4px solid #e2e8f0;border-top-color:#f59e0b;border-radius:50%;animation:spin 1s linear infinite;margin:0 auto 16px;}
    @keyframes spin{to{transform:rotate(360deg);}}
    .result-wrap{display:flex;flex-direction:column;gap:14px;}
    .info-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;}
    .info-box{background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:8px;padding:12px;text-align:center;}
    .info-box .val{font-size:17px;font-weight:700;color:#f59e0b;}
    .info-box .lbl{font-size:11px;color:#64748b;margin-top:3px;}
    table{width:100%;border-collapse:collapse;font-size:12px;}
    th{background:#f8fafc;padding:8px 10px;text-align:left;font-weight:600;color:#4a5568;border-bottom:1px solid #e2e8f0;}
    th.r{text-align:right;}
    td{padding:7px 10px;border-bottom:0.5px solid #f1f5f9;color:#1e293b;}
    td.r{text-align:right;font-weight:500;}
    tr:hover td{background:#fffbeb;}
    .total-row td{font-weight:700;background:#fef3c7;border-top:2px solid #f59e0b;}
    .grand-box{background:linear-gradient(135deg,#1e3a4a,#2f6477);border-radius:10px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;}
    .grand-box .lbl{color:#94a3b8;font-size:13px;}
    .grand-box .val{color:#f59e0b;font-size:22px;font-weight:700;}
    .notes-box{background:#f0fdf4;border:0.5px solid #86efac;border-radius:8px;padding:12px;font-size:12px;color:#166534;line-height:1.6;}
    .err-box{background:#fff5f5;border:0.5px solid #fed7d7;color:#c53030;border-radius:8px;padding:12px;font-size:13px;}
    .download-btn{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;background:#22c55e;color:#fff;border:none;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;}
    .recalc-btn{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;}
    @media(max-width:600px){.field-row,.field-row3{grid-template-columns:1fr;}.info-grid{grid-template-columns:1fr 1fr;}}
  </style>
</head>
<body>
<nav class="nav">
  <a href="/public/" class="logo-t">БНБ — Барилгын нэгдсэн бааз</a>
  <div class="nav-r">
    <a href="/public/" class="nb">Нүүр</a>
    <a href="/tender/" class="nb">Тендер</a>
  </div>
</nav>

<div class="hero">
  <div class="hero-t">🏗 AI Төсөв Тооцоолох</div>
  <div class="hero-s">Барилгын мэдээллийг алхам алхмаар оруулахад бодитой төсөв гарна</div>
</div>

<div class="wrap">

  {% if not result %}
  <!-- Progress bar -->
  <div class="progress" id="progress">
    <div class="step-dot active" id="dot1" onclick="goTo(1)">1</div>
    <div class="step-line" id="line1"></div>
    <div class="step-dot" id="dot2" onclick="goTo(2)">2</div>
    <div class="step-line" id="line2"></div>
    <div class="step-dot" id="dot3" onclick="goTo(3)">3</div>
    <div class="step-line" id="line3"></div>
    <div class="step-dot" id="dot4" onclick="goTo(4)">4</div>
    <div class="step-line" id="line4"></div>
    <div class="step-dot" id="dot5" onclick="goTo(5)">5</div>
  </div>

  <form method="post" id="main-form">
    {% csrf_token %}

    <!-- АЛХАМ 1: Ерөнхий мэдээлэл -->
    <div class="card" id="step1">
      <div class="step-title">1️⃣ Ерөнхий мэдээлэл</div>
      <div class="step-desc">Барилгын үндсэн төрөл, байршлыг сонгоно уу</div>

      <div class="field">
        <label>Барилгын зориулалт</label>
        <select name="building_type">
          <option value="">— Сонгоно уу —</option>
          <option value="Орон сууц (нэг өрөө)">🏠 Орон сууц — 1 өрөө</option>
          <option value="Орон сууц (хоёр өрөө)">🏠 Орон сууц — 2 өрөө</option>
          <option value="Орон сууц (гурван өрөө)">🏠 Орон сууц — 3 өрөө</option>
          <option value="Амины орон сууц">🏡 Амины орон сууц</option>
          <option value="Оффис">🏢 Оффис</option>
          <option value="Дэлгүүр, үйлчилгээний байр">🏪 Дэлгүүр, үйлчилгээний байр</option>
          <option value="Агуулах">🏭 Агуулах</option>
          <option value="Үйлдвэр">🏭 Үйлдвэр</option>
          <option value="Сургууль, цэцэрлэг">🏫 Сургууль, цэцэрлэг</option>
        </select>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Давхарын тоо</label>
          <select name="floors">
            <option value="1">1 давхар</option>
            <option value="2">2 давхар</option>
            <option value="3">3 давхар</option>
            <option value="4">4 давхар</option>
            <option value="5">5 давхар</option>
            <option value="6-10">6-10 давхар</option>
            <option value="10+">10-аас дээш</option>
          </select>
        </div>
        <div class="field">
          <label>Чанарын түвшин</label>
          <select name="quality">
            <option value="эконом">💰 Эконом</option>
            <option value="дунд" selected>⭐ Дунд</option>
            <option value="премиум">💎 Премиум</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Байршил</label>
          <select name="location">
            <option value="Улаанбаатар">🏙 Улаанбаатар</option>
            <option value="Дархан">Дархан</option>
            <option value="Эрдэнэт">Эрдэнэт</option>
            <option value="Орон нутаг (аймгийн төв)">Орон нутаг (аймгийн төв)</option>
            <option value="Орон нутаг (сум)">Орон нутаг (сум)</option>
          </select>
        </div>
        <div class="field">
          <label>Барилгын жил</label>
          <select name="build_year">
            <option value="2025">2025</option>
            <option value="2026" selected>2026</option>
            <option value="2027">2027</option>
          </select>
        </div>
      </div>

      <div class="btn-row">
        <button type="button" class="btn-next" onclick="next(1)">Дараах →</button>
      </div>
    </div>

    <!-- АЛХАМ 2: Хэмжээс, харьцаа -->
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
          <label>Дотор хуваалтын урт (м)</label>
          <input type="number" name="inner_wall_length" placeholder="20" min="0">
          <div class="field-hint">Нийт дотор ханын урт</div>
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
    </div>

    <!-- АЛХАМ 3: Суурь -->
    <div class="card" id="step3" style="display:none;">
      <div class="step-title">3️⃣ Суурь</div>
      <div class="step-desc">Суурийн төрөл, хэмжээсийг сонгоно уу</div>

      <div class="field-row">
        <div class="field">
          <label>Суурийн төрөл</label>
          <select name="foundation_type">
            <option value="Туузан суурь">Туузан суурь — элбэг хэрэглэгддэг</option>
            <option value="Хавтан суурь">Хавтан суурь — бүх талбайд</option>
            <option value="Шонон суурь">Шонон суурь — нойтон хөрс</option>
            <option value="Монолит суурь">Монолит суурь — хүчтэй</option>
          </select>
        </div>
        <div class="field">
          <label>Суурийн гүн (м)</label>
          <select name="foundation_depth">
            <option value="1.5">1.5 м</option>
            <option value="2.0">2.0 м — стандарт УБ</option>
            <option value="2.5" selected>2.5 м — хөлдөлтийн гүн</option>
            <option value="3.0">3.0 м</option>
            <option value="3.5+">3.5м+</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Суурийн өргөн (см)</label>
          <select name="foundation_width">
            <option value="40">40 см</option>
            <option value="50" selected>50 см — стандарт</option>
            <option value="60">60 см</option>
            <option value="80">80 см</option>
            <option value="100+">100см+</option>
          </select>
        </div>
        <div class="field">
          <label>Бетоны марк</label>
          <select name="concrete_grade">
            <option value="М200">М200 — хөнгөн барилга</option>
            <option value="М250" selected>М250 — стандарт</option>
            <option value="М300">М300 — хүнд барилга</option>
            <option value="М350">М350 — өндөр давхар</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Хөрсний төрөл</label>
          <select name="soil_type">
            <option value="Элсэрхэг">Элсэрхэг — хатуу</option>
            <option value="Шавранцар" selected>Шавранцар — нийтлэг</option>
            <option value="Чулуурхаг">Чулуурхаг — маш хатуу</option>
            <option value="Нойтон, намаглаг">Нойтон, намаглаг</option>
          </select>
        </div>
        <div class="field">
          <label>Газрын усны түвшин</label>
          <select name="water_table">
            <option value="Гүн (3м+)">Гүн (3м+) — хэвийн</option>
            <option value="Дунд (1.5-3м)">Дунд (1.5-3м)</option>
            <option value="Өндөр (1.5м-)">Өндөр (1.5м-) — анхаарах</option>
          </select>
        </div>
      </div>

      <div class="btn-row">
        <button type="button" class="btn-prev" onclick="prev(3)">← Өмнөх</button>
        <button type="button" class="btn-next" onclick="next(3)">Дараах →</button>
      </div>
    </div>

    <!-- АЛХАМ 4: Хана, дээвэр -->
    <div class="card" id="step4" style="display:none;">
      <div class="step-title">4️⃣ Хана, дээвэр</div>
      <div class="step-desc">Ханын материал, дээврийн төрлийг сонгоно уу</div>

      <div class="field-row">
        <div class="field">
          <label>Гадна ханын материал</label>
          <select name="wall_material">
            <option value="Мак блок">Мак блок — хөнгөн, дулаан</option>
            <option value="Тоосго">Тоосго — уламжлалт</option>
            <option value="Бетон хавтан">Бетон хавтан — хурдан</option>
            <option value="Металл хийц">Металл хийц — агуулах</option>
            <option value="Мод каркас">Мод каркас — амины байшин</option>
          </select>
        </div>
        <div class="field">
          <label>Ханын зузаан</label>
          <select name="wall_thickness">
            <option value="20 см">20 см</option>
            <option value="25 см" selected>25 см — стандарт</option>
            <option value="30 см">30 см</option>
            <option value="40 см">40 см — хүйтэн газар</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Дулаалга</label>
          <select name="insulation">
            <option value="Байхгүй">Байхгүй</option>
            <option value="Минвата 5см">Минвата 5 см</option>
            <option value="Минвата 10см" selected>Минвата 10 см — стандарт</option>
            <option value="Пенопласт 5см">Пенопласт 5 см</option>
            <option value="Пенопласт 10см">Пенопласт 10 см</option>
          </select>
        </div>
        <div class="field">
          <label>Дотор хуваалт</label>
          <select name="inner_wall_material">
            <option value="Гипрок">Гипрок — хөнгөн</option>
            <option value="Тоосго">Тоосго — бат бөх</option>
            <option value="Мак блок">Мак блок</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Дээврийн төрөл</label>
          <select name="roof_type">
            <option value="Хавтгай дээвэр">Хавтгай дээвэр — олон давхар</option>
            <option value="Налуу дээвэр (метал)">Налуу дээвэр (металл)</option>
            <option value="Налуу дээвэр (битум)">Налуу дээвэр (битум)</option>
            <option value="Профнастил">Профнастил — хямд</option>
          </select>
        </div>
        <div class="field">
          <label>Гадна засал</label>
          <select name="facade">
            <option value="Штукатур">Штукатур — хямд</option>
            <option value="Фасадын будаг">Фасадын будаг</option>
            <option value="Клинкер тоосго">Клинкер тоосго</option>
            <option value="Вентилируемый фасад">Вентилируемый фасад</option>
          </select>
        </div>
      </div>

      <div class="btn-row">
        <button type="button" class="btn-prev" onclick="prev(4)">← Өмнөх</button>
        <button type="button" class="btn-next" onclick="next(4)">Дараах →</button>
      </div>
    </div>

    <!-- АЛХАМ 5: Дотор засал + Инженер -->
    <div class="card" id="step5" style="display:none;">
      <div class="step-title">5️⃣ Дотор засал, инженерийн шугам</div>
      <div class="step-desc">Дотор засал болон инженерийн системийг сонгоно уу</div>

      <div class="field-row">
        <div class="field">
          <label>Шалны материал</label>
          <select name="floor_material">
            <option value="Цутгамал шал">Цутгамал шал — хямд</option>
            <option value="Ламинат">Ламинат — дунд</option>
            <option value="Паркет">Паркет — премиум</option>
            <option value="Плита">Плита — ванн, гал тогоо</option>
            <option value="Хосолсон">Хосолсон</option>
          </select>
        </div>
        <div class="field">
          <label>Ханын засал</label>
          <select name="wall_finish">
            <option value="Будаг">Будаг — хямд</option>
            <option value="Обой">Обой</option>
            <option value="Плита (ванн)">Плита (ванн, гал тогоо)</option>
            <option value="Хосолсон" selected>Хосолсон</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Халаалтын систем</label>
          <select name="heating">
            <option value="Төвийн халаалт">Төвийн халаалт (УБТЗ)</option>
            <option value="Бие даасан зуух">Бие даасан зуух</option>
            <option value="Газ халаалт">Газ халаалт</option>
            <option value="Цахилгаан халаалт">Цахилгаан халаалт</option>
            <option value="Шалан халаалт">Шалан халаалт</option>
          </select>
        </div>
        <div class="field">
          <label>Усан хангамж</label>
          <select name="water">
            <option value="Төвийн шугамд холбогдох">Төвийн шугамд холбогдох</option>
            <option value="Өөрийн худаг">Өөрийн худаг</option>
            <option value="Бие даасан систем">Бие даасан систем</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label>Цахилгааны систем</label>
          <select name="electrical">
            <option value="Стандарт 220В">Стандарт 220В</option>
            <option value="Гурван фаз 380В">Гурван фаз 380В</option>
          </select>
        </div>
        <div class="field">
          <label>Нэмэлт</label>
          <select name="extras">
            <option value="Байхгүй">Байхгүй</option>
            <option value="Гараж">Гараж</option>
            <option value="Подвал">Подвал</option>
            <option value="Гараж + Подвал">Гараж + Подвал</option>
          </select>
        </div>
      </div>

      <div class="btn-row">
        <button type="button" class="btn-prev" onclick="prev(5)">← Өмнөх</button>
        <button type="submit" class="btn-calc">🤖 Төсөв тооцоолох</button>
      </div>
    </div>

  </form>

  <div class="loading" id="loading">
    <div class="spinner"></div>
    <div style="font-size:15px;font-weight:600;color:#1e293b;margin-bottom:6px;">AI тооцоолж байна...</div>
    <div style="font-size:12px;color:#94a3b8;">15-20 секунд болно</div>
  </div>

  {% else %}

  {% if result and not result.error %}
  <div class="result-wrap">
    <div class="info-grid">
      <div class="info-box">
        <div class="val">{{ result.summary.duration_months }} сар</div>
        <div class="lbl">⏱ Барилгын хугацаа</div>
      </div>
      <div class="info-box">
        <div class="val">{{ result.summary.price_per_m2|floatformat:0 }}₮</div>
        <div class="lbl">📐 1 м² үнэ</div>
      </div>
      <div class="info-box">
        <div class="val">{{ result.building_info.quality }}</div>
        <div class="lbl">⭐ Чанарын түвшин</div>
      </div>
    </div>

    <div class="card">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;">
        <div style="font-size:14px;font-weight:700;">🧱 Материалын зардал</div>
        <button onclick="downloadExcel()" class="download-btn">📥 Excel татах</button>
      </div>
      <table>
        <tr><th>Материал</th><th>Нэгж</th><th class="r">Тоо</th><th class="r">Нэгж үнэ</th><th class="r">Нийт</th></tr>
        {% for item in result.materials %}
        <tr><td>{{ item.name }}</td><td>{{ item.unit }}</td><td class="r">{{ item.qty }}</td><td class="r">{{ item.unit_price|floatformat:0 }}₮</td><td class="r">{{ item.total|floatformat:0 }}₮</td></tr>
        {% endfor %}
        <tr class="total-row"><td colspan="4">Материалын нийт</td><td class="r">{{ result.summary.materials_total|floatformat:0 }}₮</td></tr>
      </table>
    </div>

    <div class="card">
      <div style="font-size:14px;font-weight:700;margin-bottom:12px;">👷 Ажилчдын зардал</div>
      <table>
        <tr><th>Ажил</th><th>Нэгж</th><th class="r">Тоо</th><th class="r">Нэгж үнэ</th><th class="r">Нийт</th></tr>
        {% for item in result.labor %}
        <tr><td>{{ item.name }}</td><td>{{ item.unit }}</td><td class="r">{{ item.qty }}</td><td class="r">{{ item.unit_price|floatformat:0 }}₮</td><td class="r">{{ item.total|floatformat:0 }}₮</td></tr>
        {% endfor %}
        <tr class="total-row"><td colspan="4">Ажилчдын нийт</td><td class="r">{{ result.summary.labor_total|floatformat:0 }}₮</td></tr>
      </table>
    </div>

    <div class="card">
      <div style="font-size:14px;font-weight:700;margin-bottom:12px;">🚛 Тээврийн зардал</div>
      <table>
        <tr><th>Тээвэр</th><th>Нэгж</th><th class="r">Тоо</th><th class="r">Нэгж үнэ</th><th class="r">Нийт</th></tr>
        {% for item in result.transport %}
        <tr><td>{{ item.name }}</td><td>{{ item.unit }}</td><td class="r">{{ item.qty }}</td><td class="r">{{ item.unit_price|floatformat:0 }}₮</td><td class="r">{{ item.total|floatformat:0 }}₮</td></tr>
        {% endfor %}
        <tr class="total-row"><td colspan="4">Тээврийн нийт</td><td class="r">{{ result.summary.transport_total|floatformat:0 }}₮</td></tr>
      </table>
    </div>

    <div class="card">
      <div style="font-size:14px;font-weight:700;margin-bottom:12px;">📦 Бусад зардал</div>
      <table>
        <tr><th>Зардал</th><th>Нэгж</th><th class="r">Тоо</th><th class="r">Нэгж үнэ</th><th class="r">Нийт</th></tr>
        {% for item in result.other %}
        <tr><td>{{ item.name }}</td><td>{{ item.unit }}</td><td class="r">{{ item.qty }}</td><td class="r">{{ item.unit_price|floatformat:0 }}₮</td><td class="r">{{ item.total|floatformat:0 }}₮</td></tr>
        {% endfor %}
        <tr class="total-row"><td colspan="4">Бусад нийт</td><td class="r">{{ result.summary.other_total|floatformat:0 }}₮</td></tr>
      </table>
    </div>

    <div class="grand-box">
      <div>
        <div class="lbl">{{ result.building_info.type }} · {{ result.building_info.location }}</div>
        <div style="color:#fff;font-size:13px;margin-top:4px;">НИЙТ ТӨСӨВ</div>
      </div>
      <div class="val">{{ result.summary.grand_total|floatformat:0 }}₮</div>
    </div>

    {% if result.notes %}
    <div class="notes-box">💡 <strong>Анхаарах:</strong><br>{{ result.notes }}</div>
    {% endif %}

    <div style="display:flex;gap:10px;">
      <button onclick="downloadExcel()" class="download-btn">📥 Excel татах</button>
      <a href="/budget/" class="recalc-btn">🔄 Дахин тооцоолох</a>
    </div>
  </div>

  {% else %}
  <div class="card"><div class="err-box">{{ result.error }}</div></div>
  <a href="/budget/" class="recalc-btn" style="display:inline-block;margin-top:12px;">🔄 Дахин оролдох</a>
  {% endif %}

  {% endif %}

</div>

<script>
let currentStep = 1;
const totalSteps = 5;

function next(step) {
  document.getElementById("step" + step).style.display = "none";
  document.getElementById("dot" + step).classList.remove("active");
  document.getElementById("dot" + step).classList.add("done");
  if (step < totalSteps) document.getElementById("line" + step).classList.add("done");
  currentStep = step + 1;
  document.getElementById("step" + currentStep).style.display = "block";
  document.getElementById("dot" + currentStep).classList.add("active");
  window.scrollTo({top: 0, behavior: "smooth"});
}

function prev(step) {
  document.getElementById("step" + step).style.display = "none";
  document.getElementById("dot" + step).classList.remove("active");
  currentStep = step - 1;
  document.getElementById("step" + currentStep).style.display = "block";
  document.getElementById("dot" + currentStep).classList.remove("done");
  document.getElementById("dot" + currentStep).classList.add("active");
  if (step <= totalSteps) document.getElementById("line" + (step-1)).classList.remove("done");
  window.scrollTo({top: 0, behavior: "smooth"});
}

function goTo(step) {
  if (step >= currentStep) return;
  document.getElementById("step" + currentStep).style.display = "none";
  document.getElementById("dot" + currentStep).classList.remove("active");
  currentStep = step;
  document.getElementById("step" + currentStep).style.display = "block";
  document.getElementById("dot" + currentStep).classList.add("active");
  window.scrollTo({top: 0, behavior: "smooth"});
}

document.getElementById("main-form") && document.getElementById("main-form").addEventListener("submit", function() {
  document.getElementById("step5").style.display = "none";
  document.getElementById("progress").style.display = "none";
  document.getElementById("loading").classList.add("show");
});

{% if result %}
function downloadExcel() {
  const data = {{ result_json|safe }};
  const form = document.createElement("form");
  form.method = "POST";
  form.action = "/budget/excel/";
  const csrf = document.createElement("input");
  csrf.type = "hidden";
  csrf.name = "csrfmiddlewaretoken";
  csrf.value = "{{ csrf_token }}";
  form.appendChild(csrf);
  const inp = document.createElement("input");
  inp.type = "hidden";
  inp.name = "data";
  inp.value = JSON.stringify(data);
  form.appendChild(inp);
  document.body.appendChild(form);
  form.submit();
}
{% endif %}
</script>
</body>
</html>"""

with open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK — wizard template бэлэн")