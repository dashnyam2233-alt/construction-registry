content = open("templates/admin/index.html", "r", encoding="utf-8").read()

price_block = """
  <!-- Үнийн мэдээлэл -->
  <div style="border:1px solid #e5e7eb;border-radius:10px;padding:18px;margin-bottom:18px;background:#fff;">
    <div style="font-size:16px;font-weight:700;color:#1e293b;margin-bottom:12px;">💰 Үнийн мэдээлэл</div>
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px;">
      <a href="/admin/public/materialprice/?category__startswith=mat_" style="display:flex;flex-direction:column;align-items:center;padding:14px;background:#fef3c7;border-radius:8px;text-decoration:none;border:1px solid #f59e0b;">
        <span style="font-size:24px;margin-bottom:6px;">🧱</span>
        <span style="font-size:12px;font-weight:600;color:#1e3a4a;">Материал</span>
      </a>
      <a href="/admin/public/materialprice/?category__startswith=labor_" style="display:flex;flex-direction:column;align-items:center;padding:14px;background:#f0fdf4;border-radius:8px;text-decoration:none;border:1px solid #86efac;">
        <span style="font-size:24px;margin-bottom:6px;">👷</span>
        <span style="font-size:12px;font-weight:600;color:#1e3a4a;">Цалин</span>
      </a>
      <a href="/admin/public/materialprice/?category__startswith=transport_" style="display:flex;flex-direction:column;align-items:center;padding:14px;background:#eff6ff;border-radius:8px;text-decoration:none;border:1px solid #93c5fd;">
        <span style="font-size:24px;margin-bottom:6px;">🚛</span>
        <span style="font-size:12px;font-weight:600;color:#1e3a4a;">Тээвэр</span>
      </a>
      <a href="/admin/public/materialprice/?category__startswith=machine_" style="display:flex;flex-direction:column;align-items:center;padding:14px;background:#fdf4ff;border-radius:8px;text-decoration:none;border:1px solid #d8b4fe;">
        <span style="font-size:24px;margin-bottom:6px;">🔩</span>
        <span style="font-size:12px;font-weight:600;color:#1e3a4a;">Машин механизм</span>
      </a>
      <a href="/admin/public/materialprice/?category__startswith=other_" style="display:flex;flex-direction:column;align-items:center;padding:14px;background:#f8fafc;border-radius:8px;text-decoration:none;border:1px solid #e2e8f0;">
        <span style="font-size:24px;margin-bottom:6px;">📦</span>
        <span style="font-size:12px;font-weight:600;color:#1e3a4a;">Бусад</span>
      </a>
    </div>
    <div style="margin-top:10px;text-align:right;">
      <a href="/admin/public/materialprice/" style="font-size:12px;color:#2f6477;">Бүх үнэ харах →</a>
      &nbsp;|&nbsp;
      <a href="/admin/public/materialprice/add/" style="font-size:12px;color:#22c55e;">+ Үнэ нэмэх</a>
    </div>
  </div>
"""

# Баннер блокийн өмнө нэмэх
old = '  <!-- ✅ Admin index дээрх тайлбар блок -->'
new = price_block + '  <!-- ✅ Admin index дээрх тайлбар блок -->'

if old in content:
    content = content.replace(old, new, 1)
    open("templates/admin/index.html", "w", encoding="utf-8").write(content)
    print("OK — үнийн блок нэмэгдлээ")
else:
    print("NOT FOUND")
    # Өөр газар хайх
    idx = content.find("{% block content %}")
    print(repr(content[idx:idx+200]))