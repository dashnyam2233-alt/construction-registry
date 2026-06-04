import json, os

items = json.load(open("material_items.json", encoding="utf-8"))
items_js = json.dumps(items, ensure_ascii=False)

SUBCATS = [
    ("foundation", "1. Барилгын үндсэн хийц материал"),
    ("interior", "2. Засал чимэглэл"),
    ("outdoor", "3. Гадна тохижилт"),
    ("plumbing", "4. Сан, халаалт, агааржуулалт"),
    ("electrical", "5. Цахилгаан, холбоо, дохиолол"),
    ("machinery", "6. Машин механизм тоног төхөөрөмж"),
    ("furniture", "7. Тавилга"),
    ("software", "8. Программ хангамж, ном гарын авлага"),
    ("safety", "9. ХАБЭА"),
]

subcat_options = "\n".join(
    f'<option value="{code}">{label}</option>'
    for code, label in SUBCATS
)

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
    .nb-y{background:#f59e0b;color:#1e3a4a;}
    .breadcrumb{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:10px 20px;font-size:12px;color:#64748b;}
    .breadcrumb a{color:#2f6477;}
    .wrap{max-width:860px;margin:20px auto;padding:0 20px;display:grid;grid-template-columns:1fr 240px;gap:16px;}
    .form-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;overflow:hidden;}
    .form-hd{padding:14px 20px;border-bottom:0.5px solid #e2e8f0;display:flex;align-items:center;gap:10px;}
    .form-hd-icon{width:32px;height:32px;background:#fef3c7;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:16px;}
    .form-hd-t{font-size:15px;font-weight:600;color:#1e293b;}
    .form-body{padding:20px;}
    .sec-label{font-size:11px;font-weight:600;color:#94a3b8;letter-spacing:0.05em;text-transform:uppercase;margin:16px 0 10px;}
    .sec-label:first-child{margin-top:0;}
    .main-cats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:4px;}
    .main-cat{padding:10px 8px;border:1.5px solid #e2e8f0;border-radius:8px;text-align:center;cursor:pointer;background:#fff;transition:all .15s;}
    .main-cat.on{border-color:#f59e0b;background:#fef3c7;}
    .main-cat .ic{font-size:20px;display:block;margin-bottom:4px;}
    .main-cat span{font-size:11px;font-weight:500;color:#374151;display:block;}
    .material-section{display:none;}
    .material-section.show{display:block;}
    .subcat-grid{display:flex;flex-direction:column;gap:8px;margin-bottom:10px;}
    .subcat-item{border:0.5px solid #e2e8f0;border-radius:8px;overflow:hidden;}
    .subcat-hd{padding:9px 12px;cursor:pointer;display:flex;align-items:center;justify-content:space-between;font-size:13px;font-weight:500;color:#1e293b;background:#f8fafc;}
    .subcat-hd:hover{background:#f1f5f9;}
    .subcat-hd.on{background:#fef3c7;color:#854d0e;}
    .subcat-items{display:none;flex-wrap:wrap;gap:6px;padding:10px 12px;border-top:0.5px solid #e2e8f0;}
    .subcat-items.show{display:flex;}
    .item-pill{font-size:11px;padding:4px 10px;border-radius:20px;border:0.5px solid #e2e8f0;cursor:pointer;background:#fff;color:#374151;}
    .item-pill.on{background:#fef3c7;border-color:#f59e0b;color:#854d0e;}
    .field{margin-bottom:12px;}
    .field label{display:block;font-size:12px;font-weight:600;color:#4a5568;margin-bottom:4px;}
    .field input,.field select,.field textarea{width:100%;padding:8px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:13px;color:#1e293b;outline:none;background:#fff;}
    .field input::placeholder,.field textarea::placeholder{color:#b0bac9;font-size:12px;}
    .field input:focus,.field select:focus,.field textarea:focus{border-color:#f59e0b;}
    .field textarea{resize:vertical;min-height:90px;}
    .field-row{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
    .field-err{color:#e53e3e;font-size:11px;margin-top:3px;}
    .agree-box{display:flex;align-items:flex-start;gap:8px;background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:8px;padding:10px;margin-bottom:14px;}
    .agree-box input{width:15px;height:15px;margin-top:1px;accent-color:#f59e0b;}
    .agree-box label{font-size:12px;color:#4a5568;line-height:1.5;}
    .btn-main{width:100%;padding:11px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;}
    .err-box{background:#fff5f5;border:0.5px solid #fed7d7;color:#c53030;border-radius:8px;padding:10px;font-size:13px;margin-bottom:14px;}
    .sb{display:flex;flex-direction:column;gap:12px;}
    .sb-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:9px;overflow:hidden;}
    .sb-hd{padding:10px 14px;border-bottom:0.5px solid #e2e8f0;font-size:13px;font-weight:600;}
    .sb-body{padding:12px 14px;}
    .tip-item{display:flex;gap:8px;padding:5px 0;border-bottom:0.5px solid #f1f5f9;font-size:12px;color:#374151;}
    .tip-item:last-child{border-bottom:none;}
    @media(max-width:768px){.wrap{grid-template-columns:1fr;}.sb{display:none;}.main-cats{grid-template-columns:1fr 1fr;}}
  </style>
</head>
<body>

<nav class="nav">
  <a href="/public/" style="display:flex;align-items:center;gap:8px;">
    <div class="logo-box"><svg viewBox="0 0 24 24"><path d="M3 21h18M3 7l9-4 9 4M4 7v14M20 7v14M9 21v-6h6v6"/></svg></div>
    <span class="logo-t">БНБ — Барилгын нэгдсэн бааз</span>
  </a>
  <div class="nav-r">
    <a href="/public/" class="nb nb-o">Нүүр</a>
    <a href="/ads/" class="nb nb-o">Зарууд</a>
  </div>
</nav>

<div class="breadcrumb">
  <a href="/public/">Нүүр</a> › <a href="/ads/">Зарууд</a> › Шинэ зар оруулах
</div>

<div class="wrap">
  <div>
    <div class="form-card">
      <div class="form-hd">
        <div class="form-hd-icon">📢</div>
        <div><div class="form-hd-t">Шинэ зар оруулах</div></div>
      </div>
      <div class="form-body">

        {% if errors %}
        <div class="err-box">{% for k,v in errors.items %}{{ v }}<br>{% endfor %}</div>
        {% endif %}

        <form method="post" enctype="multipart/form-data" id="ad-form">
          {% csrf_token %}
          <input type="hidden" name="category" id="h_category" value="material">
          <input type="hidden" name="material_subcategory" id="h_subcat" value="">
          <input type="hidden" name="material_item" id="h_item" value="">

          <div class="sec-label">1. Зарын ангилал</div>
          <div class="main-cats">
            <div class="main-cat on" onclick="setMainCat(this,'material')">
              <span class="ic">🧱</span><span>Материал</span>
            </div>
            <div class="main-cat" onclick="setMainCat(this,'house')">
              <span class="ic">🏠</span><span>Орон сууц</span>
            </div>
            <div class="main-cat" onclick="setMainCat(this,'worker')">
              <span class="ic">👷</span><span>Ажилтан</span>
            </div>
            <div class="main-cat" onclick="setMainCat(this,'repair')">
              <span class="ic">🔧</span><span>Засвар</span>
            </div>
            <div class="main-cat" onclick="setMainCat(this,'design')">
              <span class="ic">📐</span><span>Зураг төсөл</span>
            </div>
            <div class="main-cat" onclick="setMainCat(this,'other')">
              <span class="ic">📦</span><span>Бусад</span>
            </div>
          </div>

          <!-- Материалын дэд ангилал -->
          <div class="material-section show" id="material-section">
            <div class="sec-label">2. Материалын төрөл</div>
            <div class="subcat-grid" id="subcat-grid"></div>
          </div>

          <div class="sec-label" id="basic-label">3. Үндсэн мэдээлэл</div>
          <div class="field">
            <label>Гарчиг <span style="color:#e53e3e;">*</span></label>
            <input type="text" name="title" placeholder="Зарын гарчиг бичих" value="{{ post_data.title|default:'' }}">
            {% if errors.title %}<div class="field-err">{{ errors.title }}</div>{% endif %}
          </div>
          <div class="field">
            <label>Тайлбар</label>
            <textarea name="description" placeholder="Дэлгэрэнгүй мэдээлэл бичнэ үү...">{{ post_data.description|default:'' }}</textarea>
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
                <option value="">--- ---</option>
                <option value="BGD">Баянгол</option>
                <option value="BZD">Баянзүрх</option>
                <option value="SBD">Сүхбаатар</option>
                <option value="HUD">Хан-Уул</option>
                <option value="CHD">Чингэлтэй</option>
                <option value="SHD">Сонгинохайрхан</option>
              </select>
            </div>
          </div>

          <div class="sec-label">Зураг оруулах</div>
          <div class="field">
            <label>Зураг 1</label>
            <input type="file" name="image1" accept="image/*">
          </div>
          <div class="field">
            <label>Зураг 2</label>
            <input type="file" name="image2" accept="image/*">
          </div>

          <div class="sec-label">Холбоо барих</div>
          <div class="field-row">
            <div class="field">
              <label>Нэр</label>
              <input type="text" name="contact_name" placeholder="Таны нэр" value="{{ post_data.contact_name|default:'' }}">
            </div>
            <div class="field">
              <label>Утас <span style="color:#e53e3e;">*</span></label>
              <input type="text" name="contact_phone" placeholder="9911-2233" value="{{ post_data.contact_phone|default:'' }}">
              {% if errors.contact_phone %}<div class="field-err">{{ errors.contact_phone }}</div>{% endif %}
            </div>
          </div>
          <div class="field">
            <label>И-мэйл</label>
            <input type="email" name="contact_email" placeholder="email@example.mn" value="{{ post_data.contact_email|default:'' }}">
          </div>

          <div class="agree-box">
            <input type="checkbox" id="agree" name="agree" required>
            <label for="agree">Зарын дүрэм журамтай танилцаж зөвшөөрсөн.</label>
          </div>

          <button type="submit" class="btn-main">📢 Зар нийтлэх</button>
        </form>
      </div>
    </div>
  </div>

  <div class="sb">
    <div class="sb-card">
      <div class="sb-hd">💡 Зөвлөмж</div>
      <div class="sb-body">
        <div class="tip-item"><span>📸</span><span>Зураг оруулснаар 3 дахин их үзэгдэнэ</span></div>
        <div class="tip-item"><span>✏️</span><span>Гарчигт үндсэн мэдээллийг тодорхой бичнэ</span></div>
        <div class="tip-item"><span>💰</span><span>Үнийг заасан зар хурдан зарагддаг</span></div>
        <div class="tip-item"><span>📞</span><span>Утасны дугаараа зөв оруулна уу</span></div>
      </div>
    </div>
    <div class="sb-card">
      <div class="sb-hd">ℹ️ Мэдээлэл</div>
      <div class="sb-body" style="font-size:12px;color:#64748b;line-height:1.6;">
        <p>• Зар 30 хоног идэвхтэй байна</p>
        <p style="margin-top:4px;">• Нэг хэрэглэгч 10 зар оруулна</p>
        <p style="margin-top:4px;">• Зар шалгасны дараа нийтлэгдэнэ</p>
      </div>
    </div>
  </div>
</div>

<script>
const ITEMS = """ + items_js + """;

const SUBCAT_LABELS = {
  foundation: "1. Барилгын үндсэн хийц материал",
  interior: "2. Засал чимэглэл",
  outdoor: "3. Гадна тохижилт",
  plumbing: "4. Сан, халаалт, агааржуулалт",
  electrical: "5. Цахилгаан, холбоо, дохиолол",
  machinery: "6. Машин механизм тоног төхөөрөмж",
  furniture: "7. Тавилга",
  software: "8. Программ хангамж, ном гарын авлага",
  safety: "9. ХАБЭА",
};

function buildSubcats() {
  const grid = document.getElementById("subcat-grid");
  grid.innerHTML = "";
  Object.entries(SUBCAT_LABELS).forEach(([code, label]) => {
    const wrap = document.createElement("div");
    wrap.className = "subcat-item";
    const hd = document.createElement("div");
    hd.className = "subcat-hd";
    hd.innerHTML = label + '<span style="font-size:11px;opacity:0.6;">' + Object.keys(ITEMS[code]||{}).length + ' төрөл ▼</span>';
    const itemsDiv = document.createElement("div");
    itemsDiv.className = "subcat-items";
    (Object.entries(ITEMS[code]||{})).forEach(([icode, ilabel]) => {
      const pill = document.createElement("span");
      pill.className = "item-pill";
      pill.textContent = ilabel;
      pill.onclick = function() {
        document.querySelectorAll(".item-pill").forEach(p => p.classList.remove("on"));
        this.classList.add("on");
        document.getElementById("h_item").value = icode;
      };
      itemsDiv.appendChild(pill);
    });
    hd.onclick = function() {
      const showing = itemsDiv.classList.contains("show");
      document.querySelectorAll(".subcat-items").forEach(d => d.classList.remove("show"));
      document.querySelectorAll(".subcat-hd").forEach(h => h.classList.remove("on"));
      if (!showing) {
        itemsDiv.classList.add("show");
        hd.classList.add("on");
        document.getElementById("h_subcat").value = code;
      } else {
        document.getElementById("h_subcat").value = "";
      }
    };
    wrap.appendChild(hd);
    wrap.appendChild(itemsDiv);
    grid.appendChild(wrap);
  });
}

function setMainCat(el, code) {
  document.querySelectorAll(".main-cat").forEach(c => c.classList.remove("on"));
  el.classList.add("on");
  document.getElementById("h_category").value = code;
  const ms = document.getElementById("material-section");
  const lbl = document.getElementById("basic-label");
  if (code === "material") {
    ms.classList.add("show");
    lbl.textContent = "3. Үндсэн мэдээлэл";
  } else {
    ms.classList.remove("show");
    lbl.textContent = "2. Үндсэн мэдээлэл";
  }
}

buildSubcats();
</script>
</body>
</html>"""

with open("apps/registry/templates/registry/ad_create.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK — ad_create.html бэлэн")