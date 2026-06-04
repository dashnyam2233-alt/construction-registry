html = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Төсөв тооцоолох — БНБ</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f1f5f9;}
    a{text-decoration:none;color:inherit;}
    .nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;position:sticky;top:0;z-index:1000;}
    .logo-t{color:#fff;font-size:13px;font-weight:700;}
    .nav-r{margin-left:auto;display:flex;gap:8px;}
    .nb{padding:5px 12px;border-radius:6px;font-size:12px;font-weight:500;border:1px solid #2d4f63;color:#cbd5e1;background:transparent;}
    .hero{background:linear-gradient(135deg,#1e3a4a,#2f6477);padding:28px 20px;text-align:center;}
    .hero-t{color:#fff;font-size:22px;font-weight:700;margin-bottom:6px;}
    .hero-s{color:#94a3b8;font-size:13px;}
    .page{max-width:1100px;margin:20px auto;padding:0 20px;display:grid;grid-template-columns:380px 1fr;gap:20px;}
    .card{background:#fff;border:0.5px solid #e2e8f0;border-radius:12px;padding:20px;}
    .card-title{font-size:14px;font-weight:700;color:#1e293b;margin-bottom:14px;}
    .field{margin-bottom:12px;}
    .field label{display:block;font-size:11px;font-weight:600;color:#4a5568;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.04em;}
    .field select,.field input,.field textarea{width:100%;padding:8px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:13px;color:#1e293b;outline:none;}
    .field select:focus,.field input:focus,.field textarea:focus{border-color:#f59e0b;}
    .field textarea{resize:vertical;min-height:70px;}
    .field-row{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
    .btn{width:100%;padding:11px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;margin-top:4px;}
    .btn:hover{background:#e08c00;}
    .tip{background:#fef3c7;border-radius:8px;padding:10px 12px;font-size:12px;color:#854d0e;margin-bottom:12px;}
    .err-box{background:#fff5f5;border:0.5px solid #fed7d7;color:#c53030;border-radius:8px;padding:10px;font-size:13px;margin-bottom:12px;}
    .loading{display:none;text-align:center;padding:60px 20px;}
    .loading.show{display:block;}
    .spinner{width:48px;height:48px;border:4px solid #e2e8f0;border-top-color:#f59e0b;border-radius:50%;animation:spin 1s linear infinite;margin:0 auto 16px;}
    @keyframes spin{to{transform:rotate(360deg);}}
    .empty{text-align:center;padding:60px 20px;color:#94a3b8;}
    .result-wrap{display:flex;flex-direction:column;gap:14px;}
    .info-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:4px;}
    .info-box{background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:8px;padding:12px;text-align:center;}
    .info-box .val{font-size:18px;font-weight:700;color:#f59e0b;}
    .info-box .lbl{font-size:11px;color:#64748b;margin-top:3px;}
    .section-title{font-size:13px;font-weight:700;color:#1e293b;padding:10px 0 6px;border-bottom:2px solid #f59e0b;margin-bottom:8px;}
    table{width:100%;border-collapse:collapse;font-size:12px;}
    th{background:#f8fafc;padding:8px 10px;text-align:left;font-weight:600;color:#4a5568;border-bottom:1px solid #e2e8f0;}
    th.num{text-align:right;}
    td{padding:7px 10px;border-bottom:0.5px solid #f1f5f9;color:#1e293b;}
    td.num{text-align:right;font-weight:500;}
    tr:hover td{background:#fffbeb;}
    .total-row td{font-weight:700;color:#1e293b;background:#fef3c7;border-top:2px solid #f59e0b;}
    .grand-box{background:linear-gradient(135deg,#1e3a4a,#2f6477);border-radius:10px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;}
    .grand-box .lbl{color:#94a3b8;font-size:13px;}
    .grand-box .val{color:#f59e0b;font-size:24px;font-weight:700;}
    .notes-box{background:#f0fdf4;border:0.5px solid #86efac;border-radius:8px;padding:12px;font-size:12px;color:#166534;line-height:1.6;}
    .download-btn{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;background:#22c55e;color:#fff;border:none;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;text-decoration:none;}
    .download-btn:hover{background:#16a34a;}
    @media(max-width:900px){.page{grid-template-columns:1fr;}.info-grid{grid-template-columns:1fr 1fr;}.field-row{grid-template-columns:1fr;}}
  </style>
</head>
<body>

<nav class="nav">
  <a href="/public/" class="logo-t">БНБ — Барилгын нэгдсэн бааз</a>
  <div class="nav-r">
    <a href="/public/" class="nb">Нүүр</a>
    <a href="/ads/" class="nb">Зарууд</a>
    <a href="/tender/" class="nb">Тендер</a>
  </div>
</nav>

<div class="hero">
  <div class="hero-t">🤖 AI Төсөв Тооцоолох</div>
  <div class="hero-s">Барилгын мэдээлэл оруулахад AI автоматаар бодитой төсөв тооцоолно</div>
</div>

<div class="page">
  <div>
    <div class="card">
      <div class="card-title">📋 Барилгын мэдээлэл оруулах</div>
      <div class="tip">💡 Мэдээллийг дэлгэрэнгүй оруулах тусам тооцоо нарийн гарна.</div>

      {% if error %}<div class="err-box">{{ error }}</div>{% endif %}

      <form method="post" id="calc-form">
        {% csrf_token %}
        <div class="field">
          <label>Барилгын төрөл *</label>
          <select name="building_type">
            <option value="">— Сонгоно уу —</option>
            <option value="Нэг өрөө орон сууц">🏠 Нэг өрөө орон сууц</option>
            <option value="Хоёр өрөө орон сууц">🏠 Хоёр өрөө орон сууц</option>
            <option value="Гурван өрөө орон сууц">🏠 Гурван өрөө орон сууц</option>
            <option value="Амины орон сууц">🏡 Амины орон сууц</option>
            <option value="Оффис">🏢 Оффис</option>
            <option value="Үйлчилгээний барилга">🏪 Үйлчилгээний барилга</option>
            <option value="Агуулах, үйлдвэр">🏭 Агуулах, үйлдвэр</option>
            <option value="Цэцэрлэг, сургууль">🏫 Цэцэрлэг, сургууль</option>
          </select>
        </div>
        <div class="field-row">
          <div class="field">
            <label>Талбай (м²) *</label>
            <input type="number" name="area" placeholder="80" value="{{ post_data.area|default:'' }}" min="10">
          </div>
          <div class="field">
            <label>Давхар</label>
            <input type="number" name="floors" placeholder="1" value="{{ post_data.floors|default:'1' }}" min="1" max="20">
          </div>
        </div>
        <div class="field-row">
          <div class="field">
            <label>Байршил</label>
            <select name="location">
              <option value="Улаанбаатар">Улаанбаатар</option>
              <option value="Дархан">Дархан</option>
              <option value="Эрдэнэт">Эрдэнэт</option>
              <option value="Орон нутаг">Орон нутаг</option>
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
        <div class="field">
          <label>Нэмэлт мэдээлэл</label>
          <textarea name="extra" placeholder="Жишээ: газар доорх паркинтай, дулаалга сайн...">{{ post_data.extra|default:'' }}</textarea>
        </div>
        <button type="submit" class="btn" id="calc-btn">🤖 AI-аар төсөв бодох</button>
      </form>
    </div>
  </div>

  <div>
    <div class="loading" id="loading">
      <div class="spinner"></div>
      <div style="font-size:15px;font-weight:600;color:#1e293b;">AI тооцоолж байна...</div>
      <div style="font-size:12px;color:#94a3b8;margin-top:6px;">15-20 секунд болно</div>
    </div>

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
          <div class="card-title" style="margin:0;">🧱 Материалын зардал</div>
          <a href="/budget/excel/?data={{ result|urlencode }}" class="download-btn" id="excel-btn">📥 Excel татах</a>
        </div>
        <table>
          <tr><th>Материал</th><th>Нэгж</th><th class="num">Тоо</th><th class="num">Нэгж үнэ</th><th class="num">Нийт</th></tr>
          {% for item in result.materials %}
          <tr>
            <td>{{ item.name }}</td>
            <td>{{ item.unit }}</td>
            <td class="num">{{ item.qty }}</td>
            <td class="num">{{ item.unit_price|floatformat:0 }}₮</td>
            <td class="num">{{ item.total|floatformat:0 }}₮</td>
          </tr>
          {% endfor %}
          <tr class="total-row">
            <td colspan="4">Материалын нийт дүн</td>
            <td class="num">{{ result.summary.materials_total|floatformat:0 }}₮</td>
          </tr>
        </table>
      </div>

      <div class="card">
        <div class="card-title">👷 Ажилчдын зардал</div>
        <table>
          <tr><th>Ажил</th><th>Нэгж</th><th class="num">Тоо</th><th class="num">Нэгж үнэ</th><th class="num">Нийт</th></tr>
          {% for item in result.labor %}
          <tr>
            <td>{{ item.name }}</td>
            <td>{{ item.unit }}</td>
            <td class="num">{{ item.qty }}</td>
            <td class="num">{{ item.unit_price|floatformat:0 }}₮</td>
            <td class="num">{{ item.total|floatformat:0 }}₮</td>
          </tr>
          {% endfor %}
          <tr class="total-row">
            <td colspan="4">Ажилчдын нийт дүн</td>
            <td class="num">{{ result.summary.labor_total|floatformat:0 }}₮</td>
          </tr>
        </table>
      </div>

      <div class="card">
        <div class="card-title">📦 Бусад зардал</div>
        <table>
          <tr><th>Зардал</th><th>Нэгж</th><th class="num">Тоо</th><th class="num">Нэгж үнэ</th><th class="num">Нийт</th></tr>
          {% for item in result.other %}
          <tr>
            <td>{{ item.name }}</td>
            <td>{{ item.unit }}</td>
            <td class="num">{{ item.qty }}</td>
            <td class="num">{{ item.unit_price|floatformat:0 }}₮</td>
            <td class="num">{{ item.total|floatformat:0 }}₮</td>
          </tr>
          {% endfor %}
          <tr class="total-row">
            <td colspan="4">Бусад нийт дүн</td>
            <td class="num">{{ result.summary.other_total|floatformat:0 }}₮</td>
          </tr>
        </table>
      </div>

      <div class="grand-box">
        <div>
          <div class="lbl">{{ result.building_info.type }} · {{ result.building_info.area }} · {{ result.building_info.location }}</div>
          <div style="color:#fff;font-size:13px;margin-top:4px;">НИЙТ ТӨСӨВ</div>
        </div>
        <div class="val">{{ result.summary.grand_total|floatformat:0 }}₮</div>
      </div>

      {% if result.notes %}
      <div class="notes-box">💡 <strong>Анхаарах зүйлс:</strong><br>{{ result.notes }}</div>
      {% endif %}

    </div>

    {% elif result.error %}
    <div class="card"><div class="err-box">{{ result.error }}</div></div>

    {% else %}
    <div class="card">
      <div class="empty">
        <div style="font-size:52px;margin-bottom:14px;">🏗</div>
        <div style="font-weight:600;color:#1e293b;margin-bottom:6px;">Төсөв тооцоолох бэлэн</div>
        <div style="font-size:12px;">Зүүн талд мэдээлэл оруулаад товч дарна уу</div>
      </div>
    </div>
    {% endif %}
  </div>
</div>

<script>
document.getElementById("calc-form").addEventListener("submit", function() {
  document.getElementById("loading").classList.add("show");
  document.getElementById("calc-btn").disabled = true;
  document.getElementById("calc-btn").textContent = "Тооцоолж байна...";
  {% if result %}
  document.querySelector(".result-wrap") && (document.querySelector(".result-wrap").style.display = "none");
  document.querySelector(".card:last-child") && (document.querySelector(".card:last-child").style.display = "none");
  {% endif %}
});
</script>
</body>
</html>"""

with open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK — template бэлэн")