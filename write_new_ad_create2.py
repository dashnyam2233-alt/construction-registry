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
    .nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;}
    .logo-t{color:#fff;font-size:13px;font-weight:700;}
    .nav-r{margin-left:auto;}
    .nb{padding:5px 12px;border-radius:6px;font-size:12px;font-weight:500;border:1px solid #2d4f63;color:#cbd5e1;background:transparent;}
    .wrap{max-width:700px;margin:24px auto;padding:0 20px;}
    .card{background:#fff;border:0.5px solid #e2e8f0;border-radius:12px;padding:24px;}
    .card-title{font-size:16px;font-weight:700;color:#1e293b;margin-bottom:20px;}
    .field{margin-bottom:14px;}
    .field label{display:block;font-size:12px;font-weight:600;color:#4a5568;margin-bottom:5px;}
    .field select,.field input,.field textarea{width:100%;padding:9px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:13px;color:#1e293b;outline:none;background:#fff;}
    .field select:focus,.field input:focus,.field textarea:focus{border-color:#f59e0b;}
    .field textarea{resize:vertical;min-height:100px;}
    .field-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
    .field-err{color:#e53e3e;font-size:11px;margin-top:3px;}
    .err-box{background:#fff5f5;border:0.5px solid #fed7d7;color:#c53030;border-radius:8px;padding:10px;font-size:13px;margin-bottom:14px;}
    .btn{width:100%;padding:12px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;margin-top:6px;}
    .divider{border:none;border-top:0.5px solid #e2e8f0;margin:16px 0;}
    .sec-label{font-size:11px;font-weight:600;color:#94a3b8;letter-spacing:0.05em;text-transform:uppercase;margin-bottom:10px;}
    @media(max-width:600px){.field-row{grid-template-columns:1fr;}}
  </style>
</head>
<body>
<nav class="nav">
  <a href="/public/" class="logo-t">БНБ — Барилгын нэгдсэн бааз</a>
  <div class="nav-r"><a href="/ads/" class="nb">← Зарууд</a></div>
</nav>

<div class="wrap">
  <div class="card">
    <div class="card-title">📢 Зар оруулах</div>

    {% if errors %}
    <div class="err-box">{% for k,v in errors.items %}{{ v }}<br>{% endfor %}</div>
    {% endif %}

    <form method="post" enctype="multipart/form-data">
      {% csrf_token %}
      <input type="hidden" name="material_subcategory" id="h_subcat" value="">
      <input type="hidden" name="material_item" id="h_item" value="">

      <div class="sec-label">Ангилал</div>
      <div class="field">
        <label>Зарын төрөл <span style="color:red">*</span></label>
        <select name="category" id="cat-sel" onchange="onCatChange()">
          <option value="">— Сонгоно уу —</option>
          <option value="material" {% if post_data.category == "material" %}selected{% endif %}>🧱 Материал</option>
          <option value="equipment" {% if post_data.category == "equipment" %}selected{% endif %}>🔩 Тоног төхөөрөмж</option>
          <option value="rental" {% if post_data.category == "rental" %}selected{% endif %}>🔑 Түрээс</option>
          <option value="realestate" {% if post_data.category == "realestate" %}selected{% endif %}>🏠 Үл хөдлөх хөрөнгө</option>
          <option value="service" {% if post_data.category == "service" %}selected{% endif %}>🏗 Барилгын үйлчилгээ</option>
          <option value="design" {% if post_data.category == "design" %}selected{% endif %}>📐 Зураг төсөв, дизайн</option>
          <option value="worker" {% if post_data.category == "worker" %}selected{% endif %}>👷 Ажилтан, ажлын зар</option>
          <option value="tender" {% if post_data.category == "tender" %}selected{% endif %}>📋 Тендер, төсөл</option>
          <option value="company" {% if post_data.category == "company" %}selected{% endif %}>🏢 Компаниуд</option>
          <option value="other" {% if post_data.category == "other" %}selected{% endif %}>📦 Бусад</option>
        </select>
      </div>

      <div class="field" id="subcat-field" style="display:none;">
        <label>Дэд ангилал</label>
        <select name="material_subcategory" id="subcat-sel" onchange="onSubcatChange()">
          <option value="">— Сонгоно уу —</option>
        </select>
      </div>

      <div class="field" id="item-field" style="display:none;">
        <label>Дэд төрөл</label>
        <select name="material_item" id="item-sel">
          <option value="">— Сонгоно уу —</option>
        </select>
      </div>

      <hr class="divider">
      <div class="sec-label">Үндсэн мэдээлэл</div>

      <div class="field">
        <label>Гарчиг <span style="color:red">*</span></label>
        <input type="text" name="title" placeholder="Зарын гарчиг" value="{{ post_data.title|default:'' }}">
        {% if errors.title %}<div class="field-err">{{ errors.title }}</div>{% endif %}
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
          <select name="price_unit">
            <option value="negotiable">Тохиролцоно</option>
            <option value="ton">₮ / тонн</option>
            <option value="piece">₮ / ш</option>
            <option value="m2">₮ / м²</option>
            <option value="m3">₮ / м³</option>
            <option value="kg">₮ / кг</option>
            <option value="meter">₮ / м</option>
            <option value="month">₮ / сар</option>
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
          <label>Дүүрэг/Сум</label>
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

      <hr class="divider">
      <div class="sec-label">Зураг</div>
      <div class="field-row">
        <div class="field"><label>Зураг 1</label><input type="file" name="image1" accept="image/*"></div>
        <div class="field"><label>Зураг 2</label><input type="file" name="image2" accept="image/*"></div>
      </div>

      <hr class="divider">
      <div class="sec-label">Холбоо барих</div>
      <div class="field-row">
        <div class="field">
          <label>Нэр</label>
          <input type="text" name="contact_name" placeholder="Таны нэр" value="{{ post_data.contact_name|default:'' }}">
        </div>
        <div class="field">
          <label>Утас <span style="color:red">*</span></label>
          <input type="text" name="contact_phone" placeholder="9911-2233" value="{{ post_data.contact_phone|default:'' }}">
          {% if errors.contact_phone %}<div class="field-err">{{ errors.contact_phone }}</div>{% endif %}
        </div>
      </div>
      <div class="field">
        <label>И-мэйл</label>
        <input type="email" name="contact_email" placeholder="email@example.mn" value="{{ post_data.contact_email|default:'' }}">
      </div>

      <button type="submit" class="btn">📢 Зар нийтлэх</button>
    </form>
  </div>
</div>

<script>
const SUBCATS = {
  material: [
    ["foundation", "🏗 Барилгын үндсэн хийц"],
    ["interior", "🎨 Засал чимэглэл"],
    ["outdoor", "🌿 Гадна тохижилт"],
    ["plumbing", "🚿 Сан, халаалт"],
    ["electrical", "⚡ Цахилгаан, холбоо"],
    ["furniture", "🪑 Тавилга"],
    ["software", "💻 Программ хангамж, ном"],
    ["safety", "🦺 ХАБЭА"],
  ],
  equipment: [
    ["excavator","Экскаватор"],["crane","Кран"],["concrete_mixer","Бетон зуурагч"],
    ["generator","Генератор"],["compressor","Компрессор"],["welding","Гагнуурын төхөөрөмж"],
    ["lifting","Өргөх төхөөрөмж"],["tools","Барилгын багаж"],["measuring","Хэмжилтийн багаж"],["other_eq","Бусад"],
  ],
  rental: [
    ["tech_rent","Техник түрээс"],["tool_rent","Багаж түрээс"],["scaffold_rent","Скафольд түрээс"],
    ["crane_rent","Кран түрээс"],["container_rent","Контейнер түрээс"],["office_rent","Оффис түрээс"],
    ["warehouse_rent","Агуулах түрээс"],["machine_rent","Машин механизм түрээс"],["other_rent","Бусад"],
  ],
  realestate: [
    ["apartment","Орон сууц"],["house","Амины орон сууц"],["office_re","Оффис"],
    ["commercial","Үйлчилгээний талбай"],["warehouse_re","Агуулах үйлдвэр"],["land","Газар"],
    ["under_construction","Баригдаж буй объект"],["re_rent","Түрээс"],["re_sale","Худалдах"],
  ],
  service: [
    ["interior_svc","Интерьер"],["carpenter","Мужаан"],["tiler","Плитачин"],
    ["electrician","Цахилгаанчин"],["plumber","Сантехник"],["welder","Гагнуур"],
    ["roofing","Дээвэр"],["road_svc","Зам талбай"],["demolition","Нураалт"],
    ["crane_svc","Өргөлт кран"],["consulting","Хяналт зөвлөх"],["other_svc","Бусад"],
  ],
  design: [
    ["architecture","Архитектур"],["interior_design","Интерьер дизайн"],["structure","Конструкц"],
    ["visualization","3D визуал"],["landscape","Ландшафт дизайн"],["budget","Төсөв"],
    ["render","Render"],["other_design","Бусад"],
  ],
  worker: [
    ["jobseeker_engineer","Ажил хайгч: Инженер"],["jobseeker_architect","Ажил хайгч: Архитектор"],
    ["jobseeker_welder","Ажил хайгч: Гагнуурчин"],["jobseeker_carpenter","Ажил хайгч: Мужаан"],
    ["jobseeker_brigade","Ажил хайгч: Бригад"],["jobseeker_other","Ажил хайгч: Бусад"],
    ["job_engineer","Ажлын байр: Инженер"],["job_pm","Ажлын байр: Project manager"],
    ["job_safety","Ажлын байр: Safety officer"],["job_other","Ажлын байр: Бусад"],
  ],
  tender: [
    ["tender_item","Тендер"],["contractor","Гүйцэтгэгч хайх"],["subcontractor","Туслан гүйцэтгэгч"],
    ["investment","Хөрөнгө оруулалт"],["partnership","Хамтран ажиллах"],["new_project","Шинэ төсөл"],
  ],
  company: [
    ["construction_company","Барилгын компани"],["material_supplier","Материал нийлүүлэгч"],
    ["equipment_supplier","Тоног нийлүүлэгч"],["engineering_co","Инженеринг"],
    ["architecture_co","Архитектур"],["factory","Үйлдвэр"],["other_company","Бусад"],
  ],
  other: [
    ["leftover","Үлдэгдэл материал"],["used_goods","Хэрэглэсэн бараа"],
    ["training","Сургалт"],["other_misc","Бусад"],
  ],
};

const ITEMS = {
  foundation:[["rebar","Арматур төмөр"],["metal_structure","Металь хийц"],["concrete","Бетон зуурмаг"],["insulation","Дулаан дуу тусгаарлах"],["roof_material","Дээврийн материал"],["formwork","Хэв хашмал"],["brick_block","Тоосго блок"],["wood","Модон материал"],["door_window","Цонх хаалга"],["glass","Шилэн хийц"],["cement_lime","Цемент шохой"],["sand_gravel","Элс хайрга дайрга"],["facade","Гадна фасад"]],
  interior:[["paint","Будаг эмульс"],["dry_mix","Хуурай хольц"],["wallpaper","Обой хуулга"],["parquet","Паркет ламинат"],["tile_stone","Плита чулуу"],["decoration","Гоёл чимэглэл"],["curtain","Хөшиг тюль"]],
  outdoor:[["paving","Замын хавтан"],["fence_gate","Хашаа гадна хаалга"],["landscaping","Мод зүлэгжүүлэлт"],["cleaning","Цэвэрлэгээ тоног"]],
  plumbing:[["pipe_fitting","Шугам хоолой"],["heating","Халаах хэрэгсэл"],["sanitary","Угаалтуур ванн"],["ventilation","Агааржуулалт"]],
  electrical:[["wire_cable","Утас кабель"],["lighting","Гэрэл гэрэлтүүлэг"],["switch_socket","Унтраалга залгуур"],["fire_alarm","Галын дохиолол"],["internet_tv","Интернэт ТВ"]],
};

function onCatChange() {
  const cat = document.getElementById("cat-sel").value;
  const subcatField = document.getElementById("subcat-field");
  const itemField = document.getElementById("item-field");
  const subcatSel = document.getElementById("subcat-sel");
  const itemSel = document.getElementById("item-sel");

  subcatSel.innerHTML = '<option value="">— Сонгоно уу —</option>';
  itemSel.innerHTML = '<option value="">— Сонгоно уу —</option>';
  itemField.style.display = "none";

  if (cat && SUBCATS[cat]) {
    SUBCATS[cat].forEach(([v,l]) => {
      const o = document.createElement("option");
      o.value = v; o.textContent = l;
      subcatSel.appendChild(o);
    });
    subcatField.style.display = "block";
  } else {
    subcatField.style.display = "none";
  }
}

function onSubcatChange() {
  const subcat = document.getElementById("subcat-sel").value;
  const itemField = document.getElementById("item-field");
  const itemSel = document.getElementById("item-sel");
  itemSel.innerHTML = '<option value="">— Сонгоно уу —</option>';

  if (subcat && ITEMS[subcat]) {
    ITEMS[subcat].forEach(([v,l]) => {
      const o = document.createElement("option");
      o.value = v; o.textContent = l;
      itemSel.appendChild(o);
    });
    itemField.style.display = "block";
  } else {
    itemField.style.display = "none";
  }
}

document.getElementById("subcat-sel").addEventListener("change", onSubcatChange);
</script>
</body>
</html>"""

with open("apps/registry/templates/registry/ad_create.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK")