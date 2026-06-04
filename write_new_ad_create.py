import json

cats = json.load(open("all_categories.json", encoding="utf-8"))
cats_js = json.dumps({k: {
    "label": v["label"],
    "icon": v["icon"],
    "subs": {sk: sv[0] for sk, sv in v["subs"].items()}
} for k, v in cats.items()}, ensure_ascii=False)

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
    .wrap{max-width:920px;margin:20px auto;padding:0 20px;display:grid;grid-template-columns:1fr 220px;gap:16px;}
    .form-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;overflow:hidden;}
    .form-hd{padding:14px 20px;border-bottom:0.5px solid #e2e8f0;display:flex;align-items:center;gap:10px;}
    .form-hd-t{font-size:15px;font-weight:600;color:#1e293b;}
    .form-body{padding:20px;}
    .sec-label{font-size:11px;font-weight:600;color:#94a3b8;letter-spacing:0.05em;text-transform:uppercase;margin:16px 0 10px;}
    .sec-label:first-child{margin-top:0;}
    .cat-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin-bottom:4px;}
    .cat-btn{padding:8px 6px;border:1.5px solid #e2e8f0;border-radius:8px;text-align:center;cursor:pointer;background:#fff;transition:all .15s;}
    .cat-btn:hover{border-color:#f59e0b;background:#fffbeb;}
    .cat-btn.on{border-color:#f59e0b;background:#fef3c7;}
    .cat-btn .ic{font-size:18px;display:block;margin-bottom:3px;}
    .cat-btn span{font-size:10px;font-weight:500;color:#374151;display:block;line-height:1.2;}
    .subcat-section{display:none;margin-top:10px;}
    .subcat-section.show{display:block;}
    .subcat-wrap{display:flex;flex-wrap:wrap;gap:6px;}
    .subcat-pill{font-size:11px;padding:4px 12px;border-radius:20px;border:0.5px solid #e2e8f0;cursor:pointer;background:#fff;color:#374151;}
    .subcat-pill:hover{background:#f8fafc;}
    .subcat-pill.on{background:#fef3c7;border-color:#f59e0b;color:#854d0e;}
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
    @media(max-width:768px){.wrap{grid-template-columns:1fr;}.sb{display:none;}.cat-grid{grid-template-columns:repeat(3,1fr);}.field-row{grid-template-columns:1fr;}}
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
  <a href="/public/">Нүүр</a> › <a href="/ads/">Зарууд</a> › Шинэ зар оруулах
</div>

<div class="wrap">
  <div>
    <div class="form-card">
      <div class="form-hd">
        <div class="form-hd-t">📢 Шинэ зар оруулах</div>
      </div>
      <div class="form-body">

        {% if errors %}
        <div class="err-box">{% for k,v in errors.items %}{{ v }}<br>{% endfor %}</div>
        {% endif %}

        <form method="post" enctype="multipart/form-data" id="ad-form">
          {% csrf_token %}
          <input type="hidden" name="category" id="h_category" value="{{ post_data.category|default:'material' }}">
          <input type="hidden" name="material_subcategory" id="h_subcat" value="{{ post_data.material_subcategory|default:'' }}">
          <input type="hidden" name="material_item" id="h_item" value="{{ post_data.material_item|default:'' }}">

          <div class="sec-label">1. Зарын ангилал сонгох</div>
          <div class="cat-grid" id="cat-grid"></div>

          <div class="subcat-section" id="subcat-section">
            <div class="sec-label">2. Дэд ангилал</div>
            <div class="subcat-wrap" id="subcat-wrap"></div>
          </div>

          <div class="sec-label" id="basic-label">3. Үндсэн мэдээлэл</div>
          <div class="field">
            <label>Гарчиг <span style="color:#e53e3e;">*</span></label>
            <input type="text" name="title" placeholder="Зарын гарчиг бичих" value="{{ post_data.title|default:'' }}">
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
          <div class="field-row">
            <div class="field"><label>Зураг 1</label><input type="file" name="image1" accept="image/*"></div>
            <div class="field"><label>Зураг 2</label><input type="file" name="image2" accept="image/*"></div>
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
        <p>• Зар 30 хоног идэвхтэй</p>
        <p style="margin-top:4px;">• Нэг хэрэглэгч 10 зар оруулна</p>
        <p style="margin-top:4px;">• Шалгасны дараа нийтлэгдэнэ</p>
      </div>
    </div>
  </div>
</div>

<script>
const CATS = """ + cats_js + """;
const CURRENT_CAT = "{{ post_data.category|default:'material' }}";
const CURRENT_SUBCAT = "{{ post_data.material_subcategory|default:'' }}";

function buildCatGrid() {
  const grid = document.getElementById("cat-grid");
  grid.innerHTML = "";
  Object.entries(CATS).forEach(([code, cat]) => {
    const btn = document.createElement("div");
    btn.className = "cat-btn" + (code === CURRENT_CAT ? " on" : "");
    btn.innerHTML = '<span class="ic">' + cat.icon + '</span><span>' + cat.label.replace(/^[^ ]+ /, '') + '</span>';
    btn.onclick = function() {
      document.querySelectorAll(".cat-btn").forEach(b => b.classList.remove("on"));
      this.classList.add("on");
      document.getElementById("h_category").value = code;
      document.getElementById("h_subcat").value = "";
      document.getElementById("h_item").value = "";
      buildSubcats(code);
    };
    grid.appendChild(btn);
  });
}

function buildSubcats(catCode) {
  const sec = document.getElementById("subcat-section");
  const wrap = document.getElementById("subcat-wrap");
  const cat = CATS[catCode];
  if (!cat || !cat.subs || Object.keys(cat.subs).length === 0) {
    sec.classList.remove("show");
    document.getElementById("basic-label").textContent = "2. Үндсэн мэдээлэл";
    return;
  }
  wrap.innerHTML = "";
  Object.entries(cat.subs).forEach(([code, label]) => {
    const pill = document.createElement("span");
    pill.className = "subcat-pill" + (code === CURRENT_SUBCAT ? " on" : "");
    pill.textContent = label;
    pill.onclick = function() {
      document.querySelectorAll(".subcat-pill").forEach(p => p.classList.remove("on"));
      this.classList.add("on");
      document.getElementById("h_subcat").value = code;
    };
    wrap.appendChild(pill);
  });
  sec.classList.add("show");
  document.getElementById("basic-label").textContent = "3. Үндсэн мэдээлэл";
}

buildCatGrid();
buildSubcats(CURRENT_CAT);
</script>
</body>
</html>"""

with open("apps/registry/templates/registry/ad_create.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK — ad_create.html бэлэн")