import os

path = r"apps\registry\templates\registry\budget_calculator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. humanize load нэмэх
old1 = "{% load static %}"
new1 = "{% load static humanize %}"

# 2. Тоонуудыг таслалтай болгох — floatformat:0 → intcomma
# grand_total
old2 = '<div class="val">{{ result.summary.grand_total|floatformat:0 }}₮</div>'
new2 = '<div class="val">{{ result.summary.grand_total|intcomma }}₮</div>'

# price_per_m2
old3 = '<div class="val">{{ result.summary.price_per_m2|floatformat:0 }}₮</div>'
new3 = '<div class="val">{{ result.summary.price_per_m2|intcomma }}₮</div>'

# Хүснэгт дэх unit_price, total
old4 = '<td class="r">{{ item.unit_price|floatformat:0 }}₮</td><td class="r">{{ item.total|floatformat:0 }}₮</td></tr>\n        {% endfor %}\n        <tr class="total-row"><td colspan="4">Материалын нийт</td><td class="r">{{ result.summary.materials_total|floatformat:0 }}₮</td></tr>'
new4 = '<td class="r">{{ item.unit_price|intcomma }}₮</td><td class="r">{{ item.total|intcomma }}₮</td></tr>\n        {% endfor %}\n        <tr class="total-row"><td colspan="4">Материалын нийт</td><td class="r">{{ result.summary.materials_total|intcomma }}₮</td></tr>'

old5 = '<td class="r">{{ item.unit_price|floatformat:0 }}₮</td><td class="r">{{ item.total|floatformat:0 }}₮</td></tr>\n        {% endfor %}\n        <tr class="total-row"><td colspan="4">Ажилчдын нийт</td><td class="r">{{ result.summary.labor_total|floatformat:0 }}₮</td></tr>'
new5 = '<td class="r">{{ item.unit_price|intcomma }}₮</td><td class="r">{{ item.total|intcomma }}₮</td></tr>\n        {% endfor %}\n        <tr class="total-row"><td colspan="4">Ажилчдын нийт</td><td class="r">{{ result.summary.labor_total|intcomma }}₮</td></tr>'

old6 = '<td class="r">{{ item.unit_price|floatformat:0 }}₮</td><td class="r">{{ item.total|floatformat:0 }}₮</td></tr>\n        {% endfor %}\n        <tr class="total-row"><td colspan="4">Тээврийн нийт</td><td class="r">{{ result.summary.transport_total|floatformat:0 }}₮</td></tr>'
new6 = '<td class="r">{{ item.unit_price|intcomma }}₮</td><td class="r">{{ item.total|intcomma }}₮</td></tr>\n        {% endfor %}\n        <tr class="total-row"><td colspan="4">Тээврийн нийт</td><td class="r">{{ result.summary.transport_total|intcomma }}₮</td></tr>'

old7 = '<td class="r">{{ item.unit_price|floatformat:0 }}₮</td><td class="r">{{ item.total|floatformat:0 }}₮</td></tr>\n        {% endfor %}\n        <tr class="total-row"><td colspan="4">Бусад нийт</td><td class="r">{{ result.summary.other_total|floatformat:0 }}₮</td></tr>'
new7 = '<td class="r">{{ item.unit_price|intcomma }}₮</td><td class="r">{{ item.total|intcomma }}₮</td></tr>\n        {% endfor %}\n        <tr class="total-row"><td colspan="4">Бусад нийт</td><td class="r">{{ result.summary.other_total|intcomma }}₮</td></tr>'

# grand-box дахь grand_total
old8 = '<div class="val">{{ result.summary.grand_total|floatformat:0 }}₮</div>'
new8 = '<div class="val">{{ result.summary.grand_total|intcomma }}₮</div>'

replacements = [
    (old1, new1),
    (old2, new2),
    (old3, new3),
    (old4, new4),
    (old5, new5),
    (old6, new6),
    (old7, new7),
    (old8, new8),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        print(f"OK: {old[:50]}...")
    else:
        print(f"NOT FOUND: {old[:50]}...")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("\nDONE - template шинэчлэгдлээ")