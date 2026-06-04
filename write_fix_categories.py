content = open("apps/public/models.py", "r", encoding="utf-8").read()

old = '''    class Category(models.TextChoices):
        HOUSE = "house", "Орон сууц & Барилга"
        MATERIAL = "material", "Материал & Тоног"
        WORKER = "worker", "Ажилтан & Бригад"
        REPAIR = "repair", "Засвар & Үйлчилгээ"
        DESIGN = "design", "Зураг төсөл"
        OTHER = "other", "Бусад"'''

new = '''    class Category(models.TextChoices):
        MATERIAL = "material", "Материал"
        EQUIPMENT = "equipment", "Тоног төхөөрөмж"
        RENTAL = "rental", "Түрээс"
        REALESTATE = "realestate", "Үл хөдлөх хөрөнгө"
        SERVICE = "service", "Барилгын үйлчилгээ"
        DESIGN = "design", "Зураг төсөв, дизайн"
        WORKER = "worker", "Ажилтан, ажлын зар"
        TENDER = "tender", "Тендер, төсөл"
        COMPANY = "company", "Компаниуд"
        OTHER = "other", "Бусад"'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/public/models.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    # Таб/зайн ялгаа байна — шууд replace
    import re
    pattern = r'class Category\(models\.TextChoices\):.*?OTHER = "other"[^\n]*'
    replacement = '''class Category(models.TextChoices):
        MATERIAL = "material", "Материал"
        EQUIPMENT = "equipment", "Тоног төхөөрөмж"
        RENTAL = "rental", "Түрээс"
        REALESTATE = "realestate", "Үл хөдлөх хөрөнгө"
        SERVICE = "service", "Барилгын үйлчилгээ"
        DESIGN = "design", "Зураг төсөв, дизайн"
        WORKER = "worker", "Ажилтан, ажлын зар"
        TENDER = "tender", "Тендер, төсөл"
        COMPANY = "company", "Компаниуд"
        OTHER = "other", "Бусад"'''
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if new_content != content:
        open("apps/public/models.py", "w", encoding="utf-8").write(new_content)
        print("OK — regex-ээр засагдлаа")
    else:
        print("FAILED")