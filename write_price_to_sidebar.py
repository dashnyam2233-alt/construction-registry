content = open("templates/admin/_sidebar_registry.html", "r", encoding="utf-8").read()

# Файлын эхэнд үнийн хэсэг нэмэх
price_section = """<!-- Үнийн мэдээлэл -->
<div class="cr-box">
  <div class="cr-box__title">
    <span>💰 Үнийн мэдээлэл</span>
    <a href="/admin/public/materialprice/">Бүгд</a>
  </div>
  <div class="cr-list">
    <a href="/admin/public/materialprice/?category__startswith=mat_" class="cr-item" style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:0.5px solid #f1f5f9;text-decoration:none;color:#1e293b;font-size:12px;">
      <span>🧱</span><span>Материал</span>
    </a>
    <a href="/admin/public/materialprice/?category__startswith=labor_" class="cr-item" style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:0.5px solid #f1f5f9;text-decoration:none;color:#1e293b;font-size:12px;">
      <span>👷</span><span>Цалин</span>
    </a>
    <a href="/admin/public/materialprice/?category__startswith=transport_" class="cr-item" style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:0.5px solid #f1f5f9;text-decoration:none;color:#1e293b;font-size:12px;">
      <span>🚛</span><span>Тээвэр</span>
    </a>
    <a href="/admin/public/materialprice/?category__startswith=machine_" class="cr-item" style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:0.5px solid #f1f5f9;text-decoration:none;color:#1e293b;font-size:12px;">
      <span>🔩</span><span>Машин механизм</span>
    </a>
    <a href="/admin/public/materialprice/?category__startswith=other_" class="cr-item" style="display:flex;align-items:center;gap:8px;padding:6px 0;text-decoration:none;color:#1e293b;font-size:12px;">
      <span>📦</span><span>Бусад</span>
    </a>
  </div>
  <a href="/admin/public/materialprice/add/" class="cr-add-btn">+ Үнэ нэмэх</a>
</div>

"""

if "Үнийн мэдээлэл" not in content:
    content = price_section + content
    open("templates/admin/_sidebar_registry.html", "w", encoding="utf-8").write(content)
    print("OK — үнийн хэсэг нэмэгдлээ")
else:
    print("Аль хэдийн байна")