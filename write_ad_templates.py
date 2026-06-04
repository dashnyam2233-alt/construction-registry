import os

# ad_create.html
create_html = """{% load static %}
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
    .logo-box{width:32px;height:32px;background:#f59e0b;border-radius:7px;display:flex;align-items:center;justify-content:center;}
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
    .form-hd{padding:16px 20px;border-bottom:0.5px solid #e2e8f0;display:flex;align-items:center;gap:10px;}
    .form-hd-icon{width:32px;height:32px;background:#fef3c7;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:16px;}
    .form-hd-t{font-size:15px;font-weight:600;color:#1e293b;}
    .form-hd-s{font-size:12px;color:#64748b;margin-top:1px;}
    .form-body{padding:20px;}
    .sec-label{font-size:11px;font-weight:600;color:#94a3b8;letter-spacing:0.05em;text-transform:uppercase;margin-bottom:10px;margin-top:20px;}
    .sec-label:first-child{margin-top:0;}
    .cat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;}
    .cat-btn{padding:10px 8px;border:1.5px solid #e2e8f0;border-radius:8px;text-align:center;cursor:pointer;background:#fff;}
    .cat-btn.on{border-color:#f59e0b;background:#fef3c7;}
    .cat-ic{font-size:20px;display:block;margin-bottom:4px;}
    .cat-t{font-size:12px;font-weight:500;color:#374151;}
    .field{margin-bottom:14px;}
    .field label{display:block;font-size:12px;font-weight:600;color:#4a5568;margin-bottom:5px;}
    .field input,.field select,.field textarea{width:100%;padding:9px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:13px;color:#1e293b;outline:none;background:#fff;}
    .field input:focus,.field select:focus,.field textarea:focus{border-color:#f59e0b;}
    .field textarea{resize:vertical;min-height:100px;}
    .field input::placeholder,.field textarea::placeholder{color:#b0bac9;font-size:12px;}
    .field-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
    .field-err{color:#e53e3e;font-size:11px;margin-top:3px;}
    .img-upload{border:2px dashed #e2e8f0;border-radius:8px;padding:20px;text-align:center;cursor:pointer;background:#f8fafc;margin-bottom:8px;}
    .img-upload:hover{border-color:#f59e0b;}
    .img-upload input{display:none;}
    .agree-box{display:flex;align-items:flex-start;gap:8px;background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:8px;padding:10px 12px;margin-bottom:14px;}
    .agree-box input{width:15px;height:15px;margin-top:1px;accent-color:#f59e0b;}
    .agree-box label{font-size:12px;color:#4a5568;line-height:1.5;}
    .btn-main{width:100%;padding:11px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;}
    .err-box{background:#fff5f5;border:0.5px solid #fed7d7;color:#c53030;border-radius:8px;padding:10px 12px;font-size:13px;margin-bottom:14px;}
    .sb{display:flex;flex-direction:column;gap:12px;}
    .sb-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:9px;overflow:hidden;}
    .sb-hd{padding:10px 14px;border-bottom:0.5px solid #e2e8f0;font-size:13px;font-weight:600;}
    .sb-body{padding:12px 14px;}
    .tip-item{display:flex;gap:8px;padding:6px 0;border-bottom:0.5px solid #f1f5f9;font-size:12px;color:#374151;}
    .tip-item:last-child{border-bottom:none;}
    @media(max-width:768px){.wrap{grid-template-columns:1fr;}.sb{display:none;}.cat-grid{grid-template-columns:1fr 1fr;}}
  </style>
</head>
<body>

<nav class="nav">
  <a href="/public/" class="logo-box" style="text-decoration:none;">
    <svg viewBox="0 0 24 24"><path d="M3 21h18M3 7l9-4 9 4M4 7v14M20 7v14M9 21v-6h6v6"/></svg>
  </a>
  <span class="logo-t">БНБ — Барилгын нэгдсэн бааз</span>
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
        <div><div class="form-hd-t">Шинэ зар оруулах</div><div class="form-hd-s">Бүх талбарыг үнэн зөв бөглөнө үү</div></div>
      </div>
      <div class="form-body">
        {% if errors %}
        <div class="err-box">
          {% for k, v in errors.items %}{{ v }}<br>{% endfor %}
        </div>
        {% endif %}

        <form method="post" enctype="multipart/form-data">
          {% csrf_token %}

          <div class="sec-label">Зарын ангилал сонгох</div>
          <div class="cat-grid">
            <label class="cat-btn {% if post_data.category == 'house' or not post_data.category %}on{% endif %}">
              <input type="radio" name="category" value="house" style="display:none;" {% if post_data.category == 'house' or not post_data.category %}checked{% endif %}>
              <span class="cat-ic">🏠</span><span class="cat-t">Орон сууц & Барилга</span>
            </label>
            <label class="cat-btn {% if post_data.category == 'material' %}on{% endif %}">
              <input type="radio" name="category" value="material" style="display:none;" {% if post_data.category == 'material' %}checked{% endif %}>
              <span class="cat-ic">🧱</span><span class="cat-t">Материал & Тоног</span>
            </label>
            <label class="cat-btn {% if post_data.category == 'worker' %}on{% endif %}">
              <input type="radio" name="category" value="worker" style="display:none;" {% if post_data.category == 'worker' %}checked{% endif %}>
              <span class="cat-ic">👷</span><span class="cat-t">Ажилтан & Бригад</span>
            </label>
            <label class="cat-btn {% if post_data.category == 'repair' %}on{% endif %}">
              <input type="radio" name="category" value="repair" style="display:none;" {% if post_data.category == 'repair' %}checked{% endif %}>
              <span class="cat-ic">🔧</span><span class="cat-t">Засвар & Үйлчилгээ</span>
            </label>
            <label class="cat-btn {% if post_data.category == 'design' %}on{% endif %}">
              <input type="radio" name="category" value="design" style="display:none;" {% if post_data.category == 'design' %}checked{% endif %}>
              <span class="cat-ic">📐</span><span class="cat-t">Зураг төсөл</span>
            </label>
            <label class="cat-btn {% if post_data.category == 'other' %}on{% endif %}">
              <input type="radio" name="category" value="other" style="display:none;" {% if post_data.category == 'other' %}checked{% endif %}>
              <span class="cat-ic">📢</span><span class="cat-t">Бусад</span>
            </label>
          </div>

          <div class="sec-label" style="margin-top:20px;">Үндсэн мэдээлэл</div>
          <div class="field">
            <label>Зарын гарчиг <span style="color:#e53e3e;">*</span></label>
            <input type="text" name="title" placeholder="Жишээ: 2 өрөө байр зарна — Хан-Уул дүүрэг" value="{{ post_data.title|default:'' }}">
            {% if errors.title %}<div class="field-err">{{ errors.title }}</div>{% endif %}
          </div>
          <div class="field">
            <label>Тайлбар</label>
            <textarea name="description" placeholder="Зарын дэлгэрэнгүй мэдээлэл бичнэ үү...">{{ post_data.description|default:'' }}</textarea>
          </div>
          <div class="field-row">
            <div class="field">
              <label>Үнэ</label>
              <input type="text" name="price" placeholder="180,000,000" value="{{ post_data.price|default:'' }}">
            </div>
            <div class="field">
              <label>Валют / Нөхцөл</label>
              <select name="price_type">
                <option value="mnt" {% if post_data.price_type == 'mnt' %}selected{% endif %}>₮ Төгрөг</option>
                <option value="usd" {% if post_data.price_type == 'usd' %}selected{% endif %}>$ Доллар</option>
                <option value="negotiable" {% if not post_data.price_type or post_data.price_type == 'negotiable' %}selected{% endif %}>Тохиролцоно</option>
                <option value="free" {% if post_data.price_type == 'free' %}selected{% endif %}>Үнэгүй</option>
              </select>
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label>Хот/Аймаг <span style="color:#e53e3e;">*</span></label>
              <select name="city">
                <option value="UB">Улаанбаатар</option>
                <option value="DA">Дархан</option>
                <option value="OR">Эрдэнэт</option>
                <option value="BA">Баян-Өлгий</option>
                <option value="OTHER">Бусад</option>
              </select>
            </div>
            <div class="field">
              <label>Дүүрэг/Сум</label>
              <select name="district">
                <option value="">--- сонгоно уу ---</option>
                <option value="BGD">Баянгол</option>
                <option value="BZD">Баянзүрх</option>
                <option value="SBD">Сүхбаатар</option>
                <option value="HUD">Хан-Уул</option>
                <option value="CHD">Чингэлтэй</option>
                <option value="SHD">Сонгинохайрхан</option>
                <option value="ND">Налайх</option>
              </select>
            </div>
          </div>

          <div class="sec-label">Зураг оруулах</div>
          <div class="img-upload" onclick="this.querySelector('input').click()">
            <input type="file" name="image1" accept="image/*">
            <div style="font-size:28px;margin-bottom:6px;">📷</div>
            <div style="font-size:13px;font-weight:500;color:#374151;margin-bottom:3px;">Зураг 1 оруулах</div>
            <div style="font-size:11px;color:#94a3b8;">PNG, JPG · Макс 5MB</div>
          </div>
          <div class="img-upload" onclick="this.querySelector('input').click()">
            <input type="file" name="image2" accept="image/*">
            <div style="font-size:28px;margin-bottom:6px;">📷</div>
            <div style="font-size:13px;font-weight:500;color:#374151;margin-bottom:3px;">Зураг 2 оруулах</div>
            <div style="font-size:11px;color:#94a3b8;">PNG, JPG · Макс 5MB</div>
          </div>

          <div class="sec-label" style="margin-top:20px;">Холбоо барих</div>
          <div class="field-row">
            <div class="field">
              <label>Нэр <span style="color:#e53e3e;">*</span></label>
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
            <label for="agree">Зарын дүрэм журамтай танилцаж зөвшөөрсөн. Худал мэдээлэл оруулбал зарыг устгах эрхтэй.</label>
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
        <div class="tip-item"><span>📸</span><span>Чанартай зураг оруулснаар зар 3 дахин их үзэгдэнэ</span></div>
        <div class="tip-item"><span>✏️</span><span>Гарчигт үндсэн мэдээллийг тодорхой бичнэ үү</span></div>
        <div class="tip-item"><span>💰</span><span>Үнийг заасан зар 2 дахин хурдан зарагддаг</span></div>
        <div class="tip-item"><span>📍</span><span>Байршлаа заавал оруулна уу</span></div>
        <div class="tip-item"><span>📞</span><span>Утасны дугаараа зөв оруулна уу</span></div>
      </div>
    </div>
    <div class="sb-card">
      <div class="sb-hd">ℹ️ Мэдээлэл</div>
      <div class="sb-body" style="font-size:12px;color:#64748b;line-height:1.6;">
        <p>• Зар 30 хоног идэвхтэй байна</p>
        <p style="margin-top:4px;">• Зарыг Admin шалгасны дараа нийтлэгдэнэ</p>
        <p style="margin-top:4px;">• Нэг хэрэглэгч 5 зар оруулж болно</p>
      </div>
    </div>
  </div>
</div>

<script>
document.querySelectorAll('.cat-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('on'));
    this.classList.add('on');
  });
});
</script>
</body>
</html>"""

# ad_list.html
list_html = """{% load static %}
<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Зарууд — БНБ</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f1f5f9;}
    a{text-decoration:none;color:inherit;}
    .nav{background:#1e3a4a;height:52px;display:flex;align-items:center;padding:0 20px;gap:12px;}
    .logo-box{width:32px;height:32px;background:#f59e0b;border-radius:7px;display:flex;align-items:center;justify-content:center;}
    .logo-box svg{width:18px;height:18px;fill:none;stroke:#fff;stroke-width:2;}
    .logo-t{color:#fff;font-size:13px;font-weight:700;margin-left:8px;}
    .nav-r{margin-left:auto;display:flex;gap:6px;}
    .nb{padding:5px 12px;border-radius:6px;font-size:12px;font-weight:500;border:none;cursor:pointer;}
    .nb-o{background:transparent;color:#cbd5e1;border:1px solid #2d4f63;}
    .nb-y{background:#f59e0b;color:#1e3a4a;}
    .hero{background:#1e3a4a;padding:24px 20px;}
    .hero-t{color:#fff;font-size:18px;font-weight:700;margin-bottom:12px;}
    .search-box{max-width:600px;background:#fff;border-radius:10px;padding:6px;display:flex;gap:6px;}
    .search-inp{flex:1;padding:8px 14px;border:none;outline:none;font-size:13px;color:#1e293b;border-radius:7px;}
    .search-sel{padding:8px 10px;border:none;border-left:1px solid #e2e8f0;outline:none;font-size:12px;color:#475569;background:#fff;}
    .search-btn{padding:8px 16px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:7px;font-size:13px;font-weight:700;cursor:pointer;}
    .cats{background:#fff;border-bottom:0.5px solid #e2e8f0;padding:0 20px;display:flex;overflow-x:auto;}
    .cat{display:flex;align-items:center;gap:5px;padding:10px 14px;font-size:12px;color:#64748b;border-bottom:2px solid transparent;white-space:nowrap;}
    .cat:hover{color:#1e3a4a;}
    .cat.on{color:#1e3a4a;border-bottom-color:#f59e0b;font-weight:600;}
    .wrap{max-width:1000px;margin:16px auto;padding:0 20px;}
    .ads-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;}
    .ad-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:10px;overflow:hidden;}
    .ad-card:hover{border-color:#f59e0b;}
    .ad-img{height:140px;background:#f8fafc;display:flex;align-items:center;justify-content:center;font-size:48px;border-bottom:0.5px solid #e2e8f0;overflow:hidden;}
    .ad-img img{width:100%;height:100%;object-fit:cover;}
    .ad-body{padding:12px;}
    .ad-cat{display:inline-block;background:#fef3c7;color:#854f0b;font-size:10px;padding:1px 7px;border-radius:20px;margin-bottom:6px;}
    .ad-t{font-size:13px;font-weight:600;color:#1e293b;line-height:1.35;margin-bottom:6px;}
    .ad-p{font-size:14px;font-weight:700;color:#f59e0b;margin-bottom:6px;}
    .ad-m{font-size:11px;color:#94a3b8;display:flex;gap:8px;}
    .empty{text-align:center;padding:40px;color:#94a3b8;font-size:14px;background:#fff;border-radius:10px;border:0.5px dashed #e2e8f0;}
    .top-bar{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
    .top-bar-t{font-size:14px;font-weight:600;color:#1e293b;}
    .top-bar-r{font-size:12px;color:#64748b;}
    @media(max-width:768px){.ads-grid{grid-template-columns:1fr 1fr;}}
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
    <a href="/ads/create/" class="nb nb-y">+ Зар оруулах</a>
  </div>
</nav>

<div class="hero">
  <div class="hero-t">📢 Зарууд</div>
  <form method="get" action="/ads/" class="search-box">
    <input class="search-inp" name="q" placeholder="Зар хайх..." value="{{ q }}">
    <select class="search-sel" name="cat">
      <option value="">Бүх ангилал</option>
      <option value="house" {% if category == 'house' %}selected{% endif %}>🏠 Орон сууц</option>
      <option value="material" {% if category == 'material' %}selected{% endif %}>🧱 Материал</option>
      <option value="worker" {% if category == 'worker' %}selected{% endif %}>👷 Ажилтан</option>
      <option value="repair" {% if category == 'repair' %}selected{% endif %}>🔧 Засвар</option>
      <option value="design" {% if category == 'design' %}selected{% endif %}>📐 Зураг</option>
    </select>
    <button type="submit" class="search-btn">Хайх</button>
  </form>
</div>

<div class="cats">
  <a href="/ads/" class="cat {% if not category %}on{% endif %}">🏠 Бүгд</a>
  <a href="/ads/?cat=house" class="cat {% if category == 'house' %}on{% endif %}">🏠 Орон сууц</a>
  <a href="/ads/?cat=material" class="cat {% if category == 'material' %}on{% endif %}">🧱 Материал</a>
  <a href="/ads/?cat=worker" class="cat {% if category == 'worker' %}on{% endif %}">👷 Ажилтан</a>
  <a href="/ads/?cat=repair" class="cat {% if category == 'repair' %}on{% endif %}">🔧 Засвар</a>
  <a href="/ads/?cat=design" class="cat {% if category == 'design' %}on{% endif %}">📐 Зураг</a>
  <a href="/ads/?cat=other" class="cat {% if category == 'other' %}on{% endif %}">📢 Бусад</a>
</div>

<div class="wrap">
  <div class="top-bar">
    <div class="top-bar-t">Нийт {{ ads|length }} зар</div>
    <a href="/ads/create/" class="nb nb-y" style="padding:7px 14px;">+ Зар оруулах</a>
  </div>

  {% if ads %}
  <div class="ads-grid">
    {% for ad in ads %}
    <div class="ad-card">
      <div class="ad-img">
        {% if ad.image1 %}
          <img src="{{ ad.image1.url }}" alt="{{ ad.title }}">
        {% else %}
          {% if ad.category == 'house' %}🏠
          {% elif ad.category == 'material' %}🧱
          {% elif ad.category == 'worker' %}👷
          {% elif ad.category == 'repair' %}🔧
          {% elif ad.category == 'design' %}📐
          {% else %}📢{% endif %}
        {% endif %}
      </div>
      <div class="ad-body">
        <span class="ad-cat">{{ ad.get_category_display }}</span>
        <div class="ad-t">{{ ad.title|truncatechars:60 }}</div>
        <div class="ad-p">{{ ad.get_price_display_full }}</div>
        <div class="ad-m">
          <span>📍 {{ ad.city }}</span>
          <span>🕐 {{ ad.created_at|date:"m-d" }}</span>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
  {% else %}
  <div class="empty">
    <div style="font-size:40px;margin-bottom:12px;">📭</div>
    <div>Одоогоор зар байхгүй байна.</div>
    <a href="/ads/create/" style="display:inline-block;margin-top:12px;padding:8px 18px;background:#f59e0b;color:#1e3a4a;border-radius:7px;font-size:13px;font-weight:600;">+ Зар оруулах</a>
  </div>
  {% endif %}
</div>

</body>
</html>"""

os.makedirs("apps/registry/templates/registry", exist_ok=True)
with open("apps/registry/templates/registry/ad_create.html", "w", encoding="utf-8") as f:
    f.write(create_html)
with open("apps/registry/templates/registry/ad_list.html", "w", encoding="utf-8") as f:
    f.write(list_html)
print("OK — template-үүд бэлэн боллоо")