path = r"apps\registry\templates\registry\budget_calculator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# intcomma дангаар биш — floatformat|intcomma хосолсон байх ёстой
# Django-д intcomma float тоонд таслал нэмдэггүй — эхлээд floatformat:0 хэрэглэнэ

old_list = [
    ('{{ result.summary.grand_total|intcomma }}', '{{ result.summary.grand_total|floatformat:0|intcomma }}'),
    ('{{ result.summary.price_per_m2|intcomma }}', '{{ result.summary.price_per_m2|floatformat:0|intcomma }}'),
    ('{{ result.summary.materials_total|intcomma }}', '{{ result.summary.materials_total|floatformat:0|intcomma }}'),
    ('{{ result.summary.labor_total|intcomma }}', '{{ result.summary.labor_total|floatformat:0|intcomma }}'),
    ('{{ result.summary.transport_total|intcomma }}', '{{ result.summary.transport_total|floatformat:0|intcomma }}'),
    ('{{ result.summary.other_total|intcomma }}', '{{ result.summary.other_total|floatformat:0|intcomma }}'),
    ('{{ item.unit_price|intcomma }}', '{{ item.unit_price|floatformat:0|intcomma }}'),
    ('{{ item.total|intcomma }}', '{{ item.total|floatformat:0|intcomma }}'),
]

for old, new in old_list:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"OK ({count}x): {old[:50]}")
    else:
        print(f"SKIP: {old[:50]}")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("\nDONE")