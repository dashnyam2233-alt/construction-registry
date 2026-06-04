# View нэмэх
view_code = '''

def budget_calculator(request):
    from django.conf import settings
    result = None
    error = None
    
    if request.method == "POST":
        import anthropic
        
        building_type = request.POST.get("building_type", "")
        area = request.POST.get("area", "")
        floors = request.POST.get("floors", "1")
        location = request.POST.get("location", "Улаанбаатар")
        quality = request.POST.get("quality", "дунд")
        extra = request.POST.get("extra", "")
        
        prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн. Дараах барилгын төсвийг тооцоолж өгнө үү.

Барилгын мэдээлэл:
- Төрөл: {building_type}
- Талбай: {area} м²
- Давхар: {floors}
- Байршил: {location}
- Чанарын түвшин: {quality}
- Нэмэлт мэдээлэл: {extra}

Монголын 2024-2025 оны үнийн мэдээлэлд үндэслэн дараах бүтэцтэй тооцоо гаргаж өгнө үү:

1. МАТЕРИАЛЫН ЗАРДАЛ (₮):
   - Бетон, арматур, цемент
   - Тоосго, блок
   - Дээвэр
   - Цонх, хаалга
   - Дотор засал (будаг, шал, тааз)
   - Сантехник, цахилгаан
   - Бусад материал
   
2. АЖИЛЧДЫН ЗАРДАЛ (₮):
   - Барилгачид
   - Инженер, хяналт
   - Тусгай ажилтан
   
3. БУСАД ЗАРДАЛ (₮):
   - Тоног төхөөрөмж түрээс
   - Зураг төсөл
   - Зөвшөөрөл, бүртгэл
   
4. НИЙТ ТӨСӨВ (₮)
5. 1 М² ҮНЭ (₮)
6. БАРИЛГЫН ХУГАЦАА (сар)
7. АНХААРАХ ЗҮЙЛС

Тооцоог тодорхой, задаргаатай, бодитой тоогоор гаргана уу. Монгол хэлээр бичнэ үү."""

        try:
            client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
            message = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            result = message.content[0].text
        except Exception as e:
            error = f"Алдаа гарлаа: {str(e)}"
    
    return render(request, "registry/budget_calculator.html", {
        "result": result,
        "error": error,
        "post_data": request.POST,
        "display_name": get_display_name(request.user),
    })
'''

# View-г нэмэх
content = open("apps/registry/views.py", "r", encoding="utf-8").read()
if "def budget_calculator" not in content:
    with open("apps/registry/views.py", "a", encoding="utf-8") as f:
        f.write(view_code)
    print("OK — view нэмэгдлээ")
else:
    print("Аль хэдийн байна")

# URL нэмэх
urls = open("apps/registry/urls.py", "r", encoding="utf-8").read()
if "budget_calculator" not in urls:
    urls = urls.replace(
        "from .views import (",
        "from .views import (\n    budget_calculator,"
    )
    urls = urls.replace(
        'path("tender/", tender_list, name="tender_list"),',
        'path("tender/", tender_list, name="tender_list"),\n    path("budget/", budget_calculator, name="budget_calculator"),'
    )
    open("apps/registry/urls.py", "w", encoding="utf-8").write(urls)
    print("OK — URL нэмэгдлээ")
else:
    print("URL аль хэдийн байна")

# Template хийх
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
    .hero{background:linear-gradient(135deg,#1e3a4a,#2f6477);padding:32px 20px;text-align:center;}
    .hero-t{color:#fff;font-size:22px;font-weight:700;margin-bottom:8px;}
    .hero-s{color:#94a3b8;font-size:14px;}
    .wrap{max-width:900px;margin:24px auto;padding:0 20px;display:grid;grid-template-columns:1fr 1fr;gap:20px;}
    .card{background:#fff;border:0.5px solid #e2e8f0;border-radius:12px;padding:24px;}
    .card-title{font-size:15px;font-weight:700;color:#1e293b;margin-bottom:16px;display:flex;align-items:center;gap:8px;}
    .field{margin-bottom:14px;}
    .field label{display:block;font-size:12px;font-weight:600;color:#4a5568;margin-bottom:5px;}
    .field select,.field input,.field textarea{width:100%;padding:9px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:13px;color:#1e293b;outline:none;}
    .field select:focus,.field input:focus,.field textarea:focus{border-color:#f59e0b;}
    .field textarea{resize:vertical;min-height:80px;}
    .field-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
    .btn{width:100%;padding:12px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;margin-top:6px;}
    .btn:hover{background:#e08c00;}
    .btn:disabled{background:#94a3b8;cursor:not-allowed;}
    .result-card{background:#fff;border:0.5px solid #e2e8f0;border-radius:12px;padding:24px;white-space:pre-wrap;font-size:13px;line-height:1.7;color:#1e293b;}
    .result-title{font-size:15px;font-weight:700;color:#1e293b;margin-bottom:16px;display:flex;align-items:center;gap:8px;}
    .loading{display:none;text-align:center;padding:40px;color:#64748b;}
    .loading.show{display:block;}
    .spinner{width:40px;height:40px;border:3px solid #e2e8f0;border-top-color:#f59e0b;border-radius:50%;animation:spin 1s linear infinite;margin:0 auto 12px;}
    @keyframes spin{to{transform:rotate(360deg);}}
    .err-box{background:#fff5f5;border:0.5px solid #fed7d7;color:#c53030;border-radius:8px;padding:12px;font-size:13px;margin-bottom:14px;}
    .empty-result{text-align:center;padding:40px;color:#94a3b8;}
    .tip{background:#fef3c7;border:0.5px solid #f59e0b;border-radius:8px;padding:12px;font-size:12px;color:#854d0e;margin-bottom:16px;}
    @media(max-width:768px){.wrap{grid-template-columns:1fr;}.field-row{grid-template-columns:1fr;}}
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
  <div class="hero-s">Барилгын мэдээлэл оруулахад AI автоматаар төсөв бодно</div>
</div>

<div class="wrap">
  <div>
    <div class="card">
      <div class="card-title">📋 Барилгын мэдээлэл</div>
      
      <div class="tip">💡 Мэдээллийг аль болох дэлгэрэнгүй оруулах тусам тооцоо илүү нарийн гарна.</div>

      {% if error %}
      <div class="err-box">{{ error }}</div>
      {% endif %}

      <form method="post" id="calc-form">
        {% csrf_token %}
        
        <div class="field">
          <label>Барилгын төрөл *</label>
          <select name="building_type">
            <option value="">— Сонгоно уу —</option>
            <option value="Нэг өрөө орон сууц" {% if post_data.building_type == "Нэг өрөө орон сууц" %}selected{% endif %}>🏠 Нэг өрөө орон сууц</option>
            <option value="Хоёр өрөө орон сууц" {% if post_data.building_type == "Хоёр өрөө орон сууц" %}selected{% endif %}>🏠 Хоёр өрөө орон сууц</option>
            <option value="Гурван өрөө орон сууц" {% if post_data.building_type == "Гурван өрөө орон сууц" %}selected{% endif %}>🏠 Гурван өрөө орон сууц</option>
            <option value="Амины орон сууц" {% if post_data.building_type == "Амины орон сууц" %}selected{% endif %}>🏡 Амины орон сууц</option>
            <option value="Оффис" {% if post_data.building_type == "Оффис" %}selected{% endif %}>🏢 Оффис</option>
            <option value="Үйлчилгээний барилга" {% if post_data.building_type == "Үйлчилгээний барилга" %}selected{% endif %}>🏪 Үйлчилгээний барилга</option>
            <option value="Агуулах, үйлдвэр" {% if post_data.building_type == "Агуулах, үйлдвэр" %}selected{% endif %}>🏭 Агуулах, үйлдвэр</option>
            <option value="Цэцэрлэг, сургууль" {% if post_data.building_type == "Цэцэрлэг, сургууль" %}selected{% endif %}>🏫 Цэцэрлэг, сургууль</option>
          </select>
        </div>

        <div class="field-row">
          <div class="field">
            <label>Нийт талбай (м²) *</label>
            <input type="number" name="area" placeholder="Жишээ: 80" value="{{ post_data.area|default:'' }}" min="10" max="10000">
          </div>
          <div class="field">
            <label>Давхарын тоо</label>
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
          <textarea name="extra" placeholder="Жишээ: Газар доорх паркинтай, дулаалга сайн байх, гипрок хуваалттай...">{{ post_data.extra|default:'' }}</textarea>
        </div>

        <button type="submit" class="btn" id="calc-btn">🤖 AI-аар төсөв бодох</button>
      </form>
    </div>
  </div>

  <div>
    <div class="loading" id="loading">
      <div class="spinner"></div>
      <div style="font-size:14px;font-weight:600;color:#1e293b;">AI тооцоолж байна...</div>
      <div style="font-size:12px;color:#94a3b8;margin-top:6px;">10-20 секунд болно</div>
    </div>

    {% if result %}
    <div class="result-card">
      <div class="result-title">✅ Төсвийн тооцоо</div>
      {{ result }}
    </div>
    {% else %}
    <div class="card">
      <div class="empty-result">
        <div style="font-size:48px;margin-bottom:12px;">🏗</div>
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
});
</script>
</body>
</html>"""

with open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK — template бэлэн")

print("\nДараах командыг ажиллуулна уу:")
print("python manage.py check")