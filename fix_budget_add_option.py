content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

old = '<div class="hero-t">🏗 AI Төсөв Тооцоолох</div>\n  <div class="hero-s">Барилгын мэдээллийг алхам алхмаар оруулахад бодитой төсөв гарна</div>'

new = '''<div class="hero-t">🏗 AI Төсөв Тооцоолох</div>
  <div class="hero-s">Барилгын мэдээллийг алхам алхмаар оруулахад бодитой төсөв гарна</div>
  <div style="display:flex;gap:10px;justify-content:center;margin-top:14px;flex-wrap:wrap;">
    <div style="background:#f59e0b;color:#1e3a4a;padding:8px 20px;border-radius:8px;font-size:13px;font-weight:700;">⚡ Хурдан тооцоо — одоо байна</div>
    <a href="/budget/file/" style="background:#22c55e;color:#fff;padding:8px 20px;border-radius:8px;font-size:13px;font-weight:700;text-decoration:none;">📊 Нарийн тооцоо — файл оруулах</a>
  </div>'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")