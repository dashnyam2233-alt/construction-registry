path = r"write_budget_norm.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

fixes = [
    # Барилгачид — том барилгад хязгаар
    (
        "    general_worker_days = round(total_area * 1.5)",
        """    # Барилгачид — зэрэг ажилладаг тул хүн-өдөр хязгаарлах
    # Жижиг барилга (≤200м²): 1.5өдөр/м²
    # Том барилга: багасдаг — зэрэг ажиллах коэффициент
    if total_area <= 200:
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
        "Барилгачид"
    ),
    # Туслах ажилтан
    (
        "    helper_days = round(total_area * 0.6)",
        """    if total_area <= 200:
        helper_coef = 0.6
    elif total_area <= 1500:
        helper_coef = 0.4
    else:
        helper_coef = 0.25
    helper_days = round(total_area * helper_coef)""",
        "Туслах"
    ),
    # Мужаан
    (
        "    carpenter_days = round(total_area * 0.3)",
        """    if total_area <= 200:
        carp_coef = 0.3
    elif total_area <= 1500:
        carp_coef = 0.2
    else:
        carp_coef = 0.12
    carpenter_days = round(total_area * carp_coef)""",
        "Мужаан"
    ),
    # Гипрок тааз — float биш int болгох
    (
        "        labor.append({'name': 'Гипрок тааз хийх', 'unit': 'м²', 'qty': total_area, 'unit_price': gypsum_work, 'total': total_area*gypsum_work})",
        "        labor.append({'name': 'Гипрок тааз хийх', 'unit': 'м²', 'qty': total_area, 'unit_price': gypsum_work, 'total': round(total_area*gypsum_work)})",
        "Гипрок"
    ),
    # Металл профиль — float биш int
    (
        "        {'name': 'Металл профиль — таазны каркас', 'unit': 'м²', 'qty': total_area, 'unit_price': gypsum_profile, 'total': total_area*gypsum_profile},",
        "        {'name': 'Металл профиль — таазны каркас', 'unit': 'м²', 'qty': total_area, 'unit_price': gypsum_profile, 'total': round(total_area*gypsum_profile)},",
        "Металл профиль"
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
print("DONE")