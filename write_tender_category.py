import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()

# Migration файл үүсгэх
addon = """
    category = models.CharField(
        "Ангилал", max_length=50, blank=True, default="other",
        choices=[
            ("construction", "Барилга угсралт"),
            ("repair", "Засвар"),
            ("design", "Зураг төсөл"),
            ("road", "Зам, гүүр"),
            ("engineering", "Инженерийн шугам"),
            ("material", "Материал"),
            ("equipment", "Тоног төхөөрөмж"),
            ("service", "Үйлчилгээ"),
            ("consulting", "Зөвлөх"),
            ("other", "Бусад"),
        ]
    )
"""

content = open("apps/public/models.py", "r", encoding="utf-8").read()
if '"category"' not in content and "category = models.CharField" not in content:
    # is_construction-ий өмнө нэмэх
    content = content.replace(
        '    is_construction = models.BooleanField',
        addon + '    is_construction = models.BooleanField'
    )
    open("apps/public/models.py", "w", encoding="utf-8").write(content)
    print("OK — category талбар нэмэгдлээ")
else:
    print("Аль хэдийн байна")