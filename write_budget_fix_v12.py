path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

fixes = [
    # 1. Барилгачдын коэффициент нэмэх
    (
        """    if total_area <= 200:
        worker_coef = 1.5
    elif total_area <= 500:
        worker_coef = 1.2
    elif total_area <= 1500:
        worker_coef = 0.9
    elif total_area <= 3000:
        worker_coef = 0.7
    else:
        worker_coef = 0.5
    general_worker_days = round(total_area * worker_coef)""",
        """    if total_area <= 200:
        worker_coef = 1.5
    elif total_area <= 500:
        worker_coef = 1.8
    elif total_area <= 1500:
        worker_coef = 2.0
    elif total_area <= 3000:
        worker_coef = 1.8
    else:
        worker_coef = 1.5
    general_worker_days = round(total_area * worker_coef)""",
        "Барилгачид коэффициент"
    ),
    # 2. Туслах ажилтан коэффициент
    (
        """    if total_area <= 200:
        helper_coef = 0.6
    elif total_area <= 1500:
        helper_coef = 0.4
    else:
        helper_coef = 0.25
    helper_days = round(total_area * helper_coef)""",
        """    if total_area <= 200:
        helper_coef = 0.6
    elif total_area <= 1500:
        helper_coef = 0.7
    else:
        helper_coef = 0.6
    helper_days = round(total_area * helper_coef)""",
        "Туслах коэффициент"
    ),
    # 3. Мужаан коэффициент
    (
        """    if total_area <= 200:
        carp_coef = 0.3
    elif total_area <= 1500:
        carp_coef = 0.2
    else:
        carp_coef = 0.12
    carpenter_days = round(total_area * carp_coef)""",
        """    if total_area <= 200:
        carp_coef = 0.3
    elif total_area <= 1500:
        carp_coef = 0.35
    else:
        carp_coef = 0.3
    carpenter_days = round(total_area * carp_coef)""",
        "Мужаан коэффициент"
    ),
    # 4. Керамик плита ханын — хэт их байсныг засах
    (
        "    wet_wall_area = round(wa * 2.5)  # ванн өрөөний хана",
        "    wet_wall_area = round(wa * 1.5)  # ванн өрөөний хана",
        "Керамик плита хана"
    ),
    # 5. Цахилгааны ажилчин — нэмэх
    (
        "    edp = round(total_area / 10)",
        "    edp = round(total_area / 6)",
        "Цахилгаанчин"
    ),
    # 6. Сантехникч — нэмэх
    (
        "    plumber_days = round(total_area / 8)",
        "    plumber_days = round(total_area / 5)",
        "Сантехникч"
    ),
]

for old, new, name in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        print(f"OK - {name}")
    else:
        print(f"NOT FOUND - {name}")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("\nDONE")