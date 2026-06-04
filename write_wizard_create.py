html = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Зар оруулах — БНБ</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f1f5f9;}
    a{text-decoration:none;color:inherit;}
    .nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;gap:12px;}
    .logo-box{width:32px;height:32px;background:#f59e0b;border-radius:7px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
    .logo-box svg{width:18px;height:18px;fill:none;stroke:#fff;stroke-width:2;}
    .logo-t{color:#fff;font-size:13px;font-weight:700;margin-left:8px;}
    .nav-r{margin-left:auto;display:flex;gap:6px;}
    .nb{padding:5px 12px;border-radius:6px;font-size:12px;font-weight:500;border:none;cursor:pointer;}
    .nb-o{background:transparent;color:#cbd5e1;border:1px solid #2d4f63;}
    .breadcrumb{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:10px 20px;font-size:12px;color:#64748b;}
    .breadcrumb a{color:#2f6477;}
    .page{max-width:680px;margin:24px auto;padding:0 20px;}
    .card{background:#fff;border:0.5px solid #e2e8f0;border-radius:12px;overflow:hidden;}
    .card-hd{padding:14px 20px;border-bottom:0.5px solid #e2e8f0;display:flex;align-items:center;justify-content:space-between;}
    .card-hd-t{font-size:15px;font-weight:600;color:#1e293b;}
    .steps{display:flex;gap:6px;align-items:center;}
    .step-dot{width:8px;height:8px;border-radius:50%;background:#e2e8f0;transition:background .2s;}
    .step-dot.on{background:#1e3a4a;}
    .step-lbl{font-size:12px;color:#94a3b8;margin-left:4px;}
    .card-body{padding:20px;}
    .sec-lbl{font-size:11px;font-weight:600;color:#94a3b8;letter-spacing:0.05em;text-transform:uppercase;margin:0 0 12px;}
    .cat-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
    .cat-btn{display:flex;align-items:center;gap:10px;padding:12px;border:1.5px solid #e2e8f0;border-radius:10px;background:#fff;cursor:pointer;text-align:left;transition:all .15s;}
    .cat-btn:hover{border-color:#f59e0b;background:#fffbeb;}
    .cat-btn.on{border-color:#f59e0b;background:#fef3c7;}
    .cat-icon{width:38px;height:38px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:20px;}
    .cat-lbl{font-size:12px;font-weight:500;color:#1e293b;line-height:1.3;}
    .cat-sub{font-size:11px;color:#94a3b8;margin-top:2px;}
    .back-btn{font-size:12px;color:#64748b;border:none;background:none;cursor:pointer;padding:0;display:flex;align-items:center;gap:4px;}
    .step-title{font-size:14px;font-weight:600;color:#1e293b;}
    .field{margin-bottom:14px;}
    .field label{display:block;font-size:12px;font-weight:600;color:#4a5568;margin-bottom:5px;}
    .field input,.field select,.field textarea{width:100%;padding:9px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:13px;color:#1e293b;outline:none;background:#fff;}
    .field input:focus,.field select:focus,.field textarea:focus{border-color:#f59e0b;}
    .field textarea{resize:vertical;min-height:80px;}
    .field-row{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
    .field-hint{font-size:11px;color:#94a3b8;margin-top:3px;}
    .field-req{color:#e53e3e;}
    .pill-group{display:flex;flex-wrap:wrap;gap:6px;}
    .pill{font-size:12px;padding:5px 12px;border-radius:20px;border:1px solid #e2e8f0;cursor:pointer;background:#fff;color:#374151;transition:all .15s;}
    .pill:hover{border-color:#f59e0b;}
    .pill.on{background:#fef3c7;border-color:#f59e0b;color:#854d0e;font-weight:500;}
    .btn-main{width:100%;padding:12px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;margin-top:16px;}
    .btn-next{width:100%;padding:10px;background:#1e3a4a;color:#fff;border:none;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;margin-top:16px;}
    .agree-box{display:flex;align-items:flex-start;gap:8px;background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:8px;padding:10px;margin-top:14px;}
    .agree-box input{margin-top:2px;accent-color:#f59e0b;}
    .agree-box label{font-size:12px;color:#4a5568;line-height:1.5;}
    .err-box{background:#fff5f5;border:0.5px solid #fed7d7;color:#c53030;border-radius:8px;padding:10px;font-size:13px;margin-bottom:14px;}
    .tip-card{background:#f0f9ff;border:0.5px solid #bae6fd;border-radius:10px;padding:12px 16px;margin-top:14px;}
    .tip-card p{font-size:12px;color:#0369a1;line-height:1.6;margin:0;}
    @media(max-width:600px){.cat-grid{grid-template-columns:1fr;}.field-row{grid-template-columns:1fr;}}
  </style>
</head>
<body>

<nav class="nav">
  <a href="/public/" style="display:flex;align-items:center;gap:8px;">
    <div class="logo-box"><svg viewBox="0 0 24 24"><path d="M3 21h18M3 7l9-4 9 4M4 7v14M20 7v14M9 21v-6h6v6"/></svg></div>
    <span class="logo-t">БНБ — Барилгын нэгдсэн бааз</span>
  </a>
  <div class="nav-r">
    <a href="/ads/" class="nb nb-o">← Зарууд</a>
  </div>
</nav>

<div class="breadcrumb">
  <a href="/public/">Нүүр</a> › <a href="/ads/">Зарууд</a> › Шинэ зар
</div>

<div class="page">
  <div class="card">
    <div class="card-hd">
      <span class="card-hd-t" id="hd-title">📢 Зар оруулах</span>
      <div class="steps">
        <div class="step-dot on" id="dot1"></div>
        <div class="step-dot" id="dot2"></div>
        <div class="step-dot" id="dot3"></div>
        <span class="step-lbl" id="step-lbl">1 / 3</span>
      </div>
    </div>

    <form method="post" enctype="multipart/form-data" id="ad-form">
      {% csrf_token %}
      <input type="hidden" name="category" id="h_cat" value="">
      <input type="hidden" name="material_subcategory" id="h_subcat" value="">
      <input type="hidden" name="material_item" id="h_item" value="">

      <!-- АЛХАМ 1: Ангилал -->
      <div class="card-body" id="step1">
        <div class="sec-lbl">Ямар зар оруулах вэ?</div>
        {% if errors %}
        <div class="err-box">{% for k,v in errors.items %}{{ v }}<br>{% endfor %}</div>
        {% endif %}
        <div class="cat-grid" id="cat-grid"></div>
      </div>

      <!-- АЛХАМ 2: Ангиллын онцлог -->
      <div class="card-body" id="step2" style="display:none;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:16px;">
          <button type="button" class="back-btn" onclick="goStep(1)">← Буцах</button>
          <span class="step-title" id="step2-title"></span>
        </div>
        <div id="step2-fields"></div>
        <button type="button" class="btn-next" onclick="goStep(3)">Үргэлжлүүлэх →</button>
      </div>

      <!-- АЛХАМ 3: Үндсэн мэдээлэл -->
      <div class="card-body" id="step3" style="display:none;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:16px;">
          <button type="button" class="back-btn" onclick="goStep(2)">← Буцах</button>
          <span class="step-title">Үндсэн мэдээлэл</span>
        </div>

        <div class="field">
          <label>Гарчиг <span class="field-req">*</span></label>
          <input type="text" name="title" id="f-title" placeholder="Зарын гарчиг тодорхой бичнэ үү" value="{{ post_data.title|default:'' }}">
          <div class="field-hint" id="title-hint"></div>
        </div>

        <div class="field">
          <label>Тайлбар</label>
          <textarea name="description" placeholder="Дэлгэрэнгүй мэдээлэл...">{{ post_data.description|default:'' }}</textarea>
        </div>

        <div class="field-row">
          <div class="field">
            <label>Үнэ</label>
            <input type="text" name="price" placeholder="0" value="{{ post_data.price|default:'' }}">
          </div>
          <div class="field">
            <label>Үнийн нэгж</label>
            <select name="price_unit" id="f-price-unit">
              <option value="negotiable">Тохиролцоно</option>
              <option value="piece">₮ / ш</option>
              <option value="m2">₮ / м²</option>
              <option value="m3">₮ / м³</option>
              <option value="ton">₮ / тонн</option>
              <option value="kg">₮ / кг</option>
              <option value="meter">₮ / м</option>
              <option value="month">₮ / сар</option>
              <option value="day">₮ / өдөр</option>
            </select>
          </div>
        </div>

        <div class="field-row">
          <div class="field">
            <label>Хот/Аймаг</label>
            <select name="city">
              <option value="UB">Улаанбаатар</option>
              <option value="DA">Дархан</option>
              <option value="OR">Эрдэнэт</option>
              <option value="OTHER">Бусад аймаг</option>
            </select>
          </div>
          <div class="field">
            <label>Дүүрэг</label>
            <select name="district">
              <option value="">---</option>
              <option value="BGD">Баянгол</option>
              <option value="BZD">Баянзүрх</option>
              <option value="SBD">Сүхбаатар</option>
              <option value="HUD">Хан-Уул</option>
              <option value="CHD">Чингэлтэй</option>
              <option value="SHD">Сонгинохайрхан</option>
            </select>
          </div>
        </div>

        <div class="field-row">
          <div class="field">
            <label>Зураг 1</label>
            <input type="file" name="image1" accept="image/*">
          </div>
          <div class="field">
            <label>Зураг 2</label>
            <input type="file" name="image2" accept="image/*">
          </div>
        </div>

        <div class="field-row">
          <div class="field">
            <label>Холбоо барих нэр</label>
            <input type="text" name="contact_name" placeholder="Таны нэр" value="{{ post_data.contact_name|default:'' }}">
          </div>
          <div class="field">
            <label>Утас <span class="field-req">*</span></label>
            <input type="text" name="contact_phone" placeholder="9911-2233" value="{{ post_data.contact_phone|default:'' }}">
          </div>
        </div>

        <div class="field">
          <label>И-мэйл</label>
          <input type="email" name="contact_email" placeholder="email@example.mn" value="{{ post_data.contact_email|default:'' }}">
        </div>

        <div class="agree-box">
          <input type="checkbox" id="agree" name="agree" required>
          <label for="agree">Зарын дүрэм журамтай танилцаж зөвшөөрлөө.</label>
        </div>

        <button type="submit" class="btn-main">📢 Зар нийтлэх</button>
      </div>
    </form>
  </div>

  <div class="tip-card" id="tip-box">
    <p>💡 Зураг оруулсан зар 3 дахин их үзэгдэнэ. Үнийг заасан зар хурдан зарагддаг.</p>
  </div>
</div>

<script>
const CATS = [
  {
    code: "material", icon: "🧱", label: "Материал зарах",
    sub: "Барилгын материал, тоосго, бетон...",
    color: "#E6F1FB", tc: "#0C447C",
    titleHint: "Жишээ: А500 арматур 12мм — 5 тонн зарна",
    priceUnit: "ton",
    fields: [
      { type: "select", name: "material_subcategory", label: "Материалын төрөл", required: true,
        options: [["foundation","Барилгын үндсэн хийц"],["interior","Засал чимэглэл"],["outdoor","Гадна тохижилт"],["plumbing","Сан, халаалт"],["electrical","Цахилгаан, холбоо"],["furniture","Тавилга"],["safety","ХАБЭА"],["other","Бусад"]] },
      { type: "pills", name: "material_item", label: "Дэд төрөл",
        depends: "material_subcategory",
        options: {
          foundation: [["rebar","Арматур төмөр"],["metal_structure","Металь хийц"],["concrete","Бетон зуурмаг"],["insulation","Дулаалга"],["roof_material","Дээвэр"],["formwork","Хэв хашмал"],["brick_block","Тоосго блок"],["wood","Мод"],["door_window","Цонх хаалга"],["glass","Шил"],["cement_lime","Цемент шохой"],["sand_gravel","Элс хайрга"],["facade","Гадна фасад"]],
          interior: [["paint","Будаг эмульс"],["dry_mix","Хуурай хольц"],["wallpaper","Обой хуулга"],["parquet","Паркет ламинат"],["tile_stone","Плита чулуу"],["decoration","Гоёл чимэглэл"],["curtain","Хөшиг тюль"]],
          plumbing: [["pipe_fitting","Хоолой холбох"],["heating","Халаах хэрэгсэл"],["sanitary","Угаалтуур ванн"],["ventilation","Агааржуулалт"]],
          electrical: [["wire_cable","Утас кабель"],["lighting","Гэрэл"],["switch_socket","Унтраалга"],["fire_alarm","Галын дохиолол"],["internet_tv","Интернэт ТВ"]],
        }
      },
      { type: "text", name: "quantity", label: "Тоо хэмжээ (заавал биш)", placeholder: "Жишээ: 5 тонн, 200 ш" },
    ]
  },
  {
    code: "equipment", icon: "🔩", label: "Тоног төхөөрөмж",
    sub: "Экскаватор, кран, генератор...",
    color: "#F1EFE8", tc: "#444441",
    titleHint: "Жишээ: Komatsu PC200 экскаватор зарна 2018 он",
    priceUnit: "negotiable",
    fields: [
      { type: "select", name: "material_subcategory", label: "Тоногийн төрөл", required: true,
        options: [["excavator","Экскаватор"],["crane","Кран"],["concrete_mixer","Бетон зуурагч"],["generator","Генератор"],["compressor","Компрессор"],["welding","Гагнуурын төхөөрөмж"],["lifting","Өргөх төхөөрөмж"],["tools","Барилгын багаж"],["measuring","Хэмжилтийн багаж"],["other_eq","Бусад"]] },
      { type: "pills", name: "condition", label: "Төлөв",
        options: { "": [["new","Шинэ"],["used_good","Хэрэглэсэн — сайн"],["used_ok","Хэрэглэсэн — хэвийн"]] } },
      { type: "text", name: "model_year", label: "Марк, он (заавал биш)", placeholder: "Жишээ: Komatsu PC200, 2018 он" },
    ]
  },
  {
    code: "rental", icon: "🔑", label: "Түрээслэх",
    sub: "Техник, скафольд, контейнер...",
    color: "#EEEDFE", tc: "#3C3489",
    titleHint: "Жишээ: Скафольд иж бүрдэл түрээслэнэ",
    priceUnit: "day",
    fields: [
      { type: "select", name: "material_subcategory", label: "Түрээсийн төрөл", required: true,
        options: [["tech_rent","Техник түрээс"],["tool_rent","Багаж түрээс"],["scaffold_rent","Скафольд"],["formwork_rent","Хэв хашмал"],["crane_rent","Кран"],["container_rent","Контейнер"],["office_rent","Оффис"],["warehouse_rent","Агуулах"],["machine_rent","Машин механизм"],["other_rent","Бусад"]] },
      { type: "text", name: "rental_period", label: "Түрээсийн хамгийн бага хугацаа", placeholder: "Жишээ: 1 өдөр, 1 сар" },
    ]
  },
  {
    code: "realestate", icon: "🏠", label: "Үл хөдлөх хөрөнгө",
    sub: "Орон сууц, оффис, газар...",
    color: "#EAF3DE", tc: "#27500A",
    titleHint: "Жишээ: БЗД 23-р хороо 2 өрөө байр зарна",
    priceUnit: "negotiable",
    fields: [
      { type: "pills", name: "house_type", label: "Зарын төрөл", required: true,
        options: { "": [["sale","Зарна"],["rent","Түрээслэнэ"],["buy","Худалдаж авна"],["rent_partial","Хэсэгчлэн түрээслэнэ"]] } },
      { type: "pills", name: "material_subcategory", label: "Үл хөдлөхийн төрөл", required: true,
        options: { "": [["apartment","Орон сууц"],["house","Амины орон сууц"],["office_re","Оффис"],["commercial","Үйлчилгээний талбай"],["warehouse_re","Агуулах үйлдвэр"],["land","Газар"],["under_construction","Баригдаж буй"]] } },
      { type: "pills", name: "house_rooms", label: "Өрөөний тоо",
        options: { "": [["r1","1 өрөө"],["r2","2 өрөө"],["r3","3 өрөө"],["r3plus","3+ өрөө"],["studio","Студи"],["duplex","Дуплекс"]] } },
      { type: "text", name: "area", label: "Талбай (м²)", placeholder: "Жишээ: 65" },
    ]
  },
  {
    code: "service", icon: "🏗", label: "Барилгын үйлчилгээ",
    sub: "Мужаан, цахилгаанчин, засвар...",
    color: "#FAEEDA", tc: "#633806",
    titleHint: "Жишээ: Интерьер засал чимэглэлийн ажил хийнэ",
    priceUnit: "negotiable",
    fields: [
      { type: "select", name: "material_subcategory", label: "Үйлчилгээний төрөл", required: true,
        options: [["interior_svc","Интерьер"],["exterior_svc","Экстерьер"],["carpenter","Мужаан"],["tiler","Плитачин"],["electrician","Цахилгаанчин"],["plumber","Сантехник"],["welder","Гагнуур"],["roofing","Дээвэр"],["facade_svc","Фасад"],["road_svc","Зам талбай"],["demolition","Нураалт"],["crane_svc","Кран үйлчилгээ"],["consulting","Зөвлөх"],["other_svc","Бусад"]] },
      { type: "pills", name: "experience", label: "Туршлага",
        options: { "": [["exp1","1-3 жил"],["exp2","3-5 жил"],["exp3","5-10 жил"],["exp4","10+ жил"]] } },
      { type: "pills", name: "has_team", label: "Баг",
        options: { "": [["solo","Ганцаараа"],["team","Багтай"]] } },
    ]
  },
  {
    code: "worker", icon: "👷", label: "Ажилтан / Ажлын зар",
    sub: "Ажил хайх эсвэл ажилтан хайх...",
    color: "#FCEBEB", tc: "#791F1F",
    titleHint: "Жишээ: Туршлагатай цахилгаанчин ажил хайж байна",
    priceUnit: "month",
    fields: [
      { type: "pills", name: "worker_type", label: "Зарын төрөл", required: true,
        options: { "": [["jobseeker","Ажил хайж байна"],["employer","Ажилтан хайж байна"]] } },
      { type: "select", name: "material_subcategory", label: "Мэргэжил / Чиглэл", required: true,
        options: [["jobseeker_engineer","Инженер"],["jobseeker_architect","Архитектор"],["jobseeker_operator","Оператор"],["jobseeker_welder","Гагнуурчин"],["jobseeker_carpenter","Мужаан"],["jobseeker_electrician","Цахилгаанчин"],["jobseeker_plumber","Сантехникч"],["jobseeker_helper","Туслах ажилтан"],["jobseeker_brigade","Бригад"],["jobseeker_other","Бусад"]] },
      { type: "pills", name: "experience", label: "Туршлага",
        options: { "": [["exp0","Туршлагагүй"],["exp1","1-3 жил"],["exp2","3-5 жил"],["exp3","5+ жил"]] } },
    ]
  },
  {
    code: "design", icon: "📐", label: "Зураг төсөв, дизайн",
    sub: "Архитектур, интерьер, 3D...",
    color: "#E0E7FF", tc: "#3730A3",
    titleHint: "Жишээ: Орон сууцны интерьер дизайн хийнэ",
    priceUnit: "negotiable",
    fields: [
      { type: "select", name: "material_subcategory", label: "Үйлчилгээний төрөл", required: true,
        options: [["architecture","Архитектур"],["interior_design","Интерьер дизайн"],["structure","Конструкц"],["engineering_design","Инженерийн зураг"],["visualization","3D визуал"],["landscape","Ландшафт дизайн"],["budget","Төсөв"],["render","Render"],["other_design","Бусад"]] },
      { type: "text", name: "software", label: "Ашигладаг программ (заавал биш)", placeholder: "AutoCAD, Revit, SketchUp..." },
    ]
  },
  {
    code: "other", icon: "📦", label: "Бусад",
    sub: "Үлдэгдэл материал, сургалт...",
    color: "#F1EFE8", tc: "#444441",
    titleHint: "Зарын агуулгыг тодорхой бичнэ үү",
    priceUnit: "negotiable",
    fields: [
      { type: "select", name: "material_subcategory", label: "Дэд ангилал",
        options: [["leftover","Үлдэгдэл материал"],["used_goods","Хэрэглэсэн бараа"],["training","Сургалт"],["other_misc","Бусад"]] },
    ]
  },
];

let currentCat = null;
let currentStep = 1;
const extraData = {};

function buildCatGrid() {
  const grid = document.getElementById("cat-grid");
  CATS.forEach(cat => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "cat-btn";
    btn.innerHTML = `<div class="cat-icon" style="background:${cat.color};">${cat.icon}</div><div><div class="cat-lbl">${cat.label}</div><div class="cat-sub">${cat.sub}</div></div>`;
    btn.onclick = () => selectCat(cat);
    grid.appendChild(btn);
  });
}

function selectCat(cat) {
  currentCat = cat;
  document.getElementById("h_cat").value = cat.code;
  document.getElementById("step2-title").textContent = cat.icon + " " + cat.label;
  document.getElementById("title-hint").textContent = cat.titleHint;
  document.getElementById("f-price-unit").value = cat.priceUnit;
  buildStep2Fields(cat);
  goStep(2);
}

function buildStep2Fields(cat) {
  const container = document.getElementById("step2-fields");
  container.innerHTML = "";
  cat.fields.forEach(f => {
    const wrap = document.createElement("div");
    wrap.className = "field";
    wrap.id = "field-" + f.name;
    const lbl = document.createElement("label");
    lbl.innerHTML = f.label + (f.required ? ' <span class="field-req">*</span>' : "");
    wrap.appendChild(lbl);
    if (f.type === "select") {
      const sel = document.createElement("select");
      sel.name = f.name;
      sel.id = "sel-" + f.name;
      const blank = document.createElement("option");
      blank.value = ""; blank.textContent = "--- сонгоно уу ---";
      sel.appendChild(blank);
      f.options.forEach(([v, l]) => {
        const opt = document.createElement("option");
        opt.value = v; opt.textContent = l;
        sel.appendChild(opt);
      });
      sel.onchange = function() {
        extraData[f.name] = this.value;
        if (f.name === "material_subcategory") {
          document.getElementById("h_subcat").value = this.value;
        }
        rebuildDependentFields(cat);
      };
      wrap.appendChild(sel);
    } else if (f.type === "pills") {
      const pg = document.createElement("div");
      pg.className = "pill-group";
      pg.id = "pills-" + f.name;
      const opts = f.depends ? (f.options[extraData[f.depends]] || []) : (f.options[""] || []);
      opts.forEach(([v, l]) => {
        const pill = document.createElement("span");
        pill.className = "pill";
        pill.textContent = l;
        pill.dataset.val = v;
        pill.onclick = function() {
          pg.querySelectorAll(".pill").forEach(p => p.classList.remove("on"));
          this.classList.add("on");
          extraData[f.name] = v;
          if (f.name === "material_subcategory") document.getElementById("h_subcat").value = v;
          if (f.name === "material_item") document.getElementById("h_item").value = v;
          if (f.name === "house_rooms") document.querySelector('[name="house_rooms"]') && (document.querySelector('[name="house_rooms"]').value = v);
          rebuildDependentFields(cat);
        };
        pg.appendChild(pill);
      });
      wrap.appendChild(pg);
    } else if (f.type === "text") {
      const inp = document.createElement("input");
      inp.type = "text";
      inp.name = f.name;
      inp.placeholder = f.placeholder || "";
      wrap.appendChild(inp);
    }
    container.appendChild(wrap);
  });
}

function rebuildDependentFields(cat) {
  cat.fields.forEach(f => {
    if (f.type === "pills" && f.depends) {
      const pg = document.getElementById("pills-" + f.name);
      if (!pg) return;
      pg.innerHTML = "";
      const depVal = extraData[f.depends];
      const opts = f.options[depVal] || [];
      opts.forEach(([v, l]) => {
        const pill = document.createElement("span");
        pill.className = "pill";
        pill.textContent = l;
        pill.dataset.val = v;
        pill.onclick = function() {
          pg.querySelectorAll(".pill").forEach(p => p.classList.remove("on"));
          this.classList.add("on");
          extraData[f.name] = v;
          if (f.name === "material_item") document.getElementById("h_item").value = v;
        };
        pg.appendChild(pill);
      });
      document.getElementById("field-" + f.name).style.display = opts.length ? "block" : "none";
    }
  });
}

function goStep(n) {
  currentStep = n;
  [1,2,3].forEach(i => {
    document.getElementById("step"+i).style.display = i===n ? "block" : "none";
    document.getElementById("dot"+i).classList.toggle("on", i<=n);
  });
  document.getElementById("step-lbl").textContent = n + " / 3";
  if (n === 1) document.getElementById("hd-title").textContent = "📢 Зар оруулах";
  if (n === 2) document.getElementById("hd-title").textContent = "📋 Дэлгэрэнгүй";
  if (n === 3) document.getElementById("hd-title").textContent = "✏️ Мэдээлэл оруулах";
}

buildCatGrid();
</script>
</body>
</html>"""

with open("apps/registry/templates/registry/ad_create.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK — wizard ad_create.html бэлэн")