path = r"templates\admin\base_site.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# {% block nav-global %} дотор нэмэх
old = '{% block nav-global %}\n<div style="background:#1e3a4a;border-top:1px solid #2d4f63;padding:3px 16px;display:flex;align-items:center;gap:6px;flex-wrap:wrap;">'

new = '''{% block nav-global %}
<div style="background:#1e3a4a;border-top:1px solid #2d4f63;padding:3px 16px;display:flex;align-items:center;gap:6px;flex-wrap:wrap;">'''

# Эхлээд хуучин норм хэсгийг хасах
import re
# Style + div хэсгийг хасах
style_start = content.find('\n<style>\n.norm-nav-bar')
if style_start >= 0:
    content = content[:style_start]
    print("OK - хуучин норм хэсэг хасагдлаа")

# {% endblock %} олж норм цэсийг тэндээс өмнө нэмэх
# nav-global block-ын endblock-г олох
nav_block_start = content.find('{% block nav-global %}')
nav_block_end = content.find('{% endblock %}', nav_block_start)

if nav_block_start >= 0 and nav_block_end >= 0:
    norm_nav = '''
<div style="background:#152e3e;border-top:1px solid #2d4f63;padding:4px 16px;display:flex;align-items:center;gap:6px;flex-wrap:wrap;">
  <span style="color:#64a0b4;font-size:11px;font-weight:700;">📐 НОРМ:</span>
  <a href="/admin/public/materialnorm/?building_type=low_rise" style="color:#86efac;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🏡 Амины</a>
  <a href="/admin/public/materialnorm/?building_type=mid_rise" style="color:#86efac;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🏢 Олон айлын</a>
  <a href="/admin/public/materialnorm/?building_type=high_rise" style="color:#86efac;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🏙 Өндөр давхар</a>
  <a href="/admin/public/materialnorm/?building_type=office" style="color:#86efac;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🏢 Оффис</a>
  <a href="/admin/public/materialnorm/?building_type=warehouse" style="color:#86efac;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">🏭 Агуулах</a>
  <a href="/admin/public/materialnorm/" style="color:#f59e0b;font-size:11px;padding:2px 8px;border-radius:4px;background:#2d4f63;text-decoration:none;">📋 Бүгд</a>
  <a href="/admin/public/materialnorm/add/" style="color:#fff;font-size:11px;padding:2px 8px;border-radius:4px;background:#22c55e;text-decoration:none;">➕ Нэмэх</a>
</div>'''
    
    content = content[:nav_block_end] + norm_nav + '\n' + content[nav_block_end:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("OK - норм цэс block дотор нэмэгдлээ")
else:
    print(f"NOT FOUND: nav_block_start={nav_block_start}, nav_block_end={nav_block_end}")