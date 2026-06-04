content = open("apps/public/models.py", "r", encoding="utf-8").read()

old = '    is_construction = models.BooleanField("Барилгатай холбоотой", default=False)'
new = '''    category = models.CharField(
        "Ангилал", max_length=50, blank=True, default="other",
        choices=[
            ("construction", "Барилга угсралт"),
            ("repair", "Засвар"),
            ("design", "Зураг төсөл"),
            ("road", "Зам, гүүр"),
            ("engineering", "Инженерийн шугам"),
            ("material", "Материал"),
            ("equipment", "Тоног төхөөрөмж"),
            ("consulting", "Зөвлөх"),
            ("service", "Үйлчилгээ"),
            ("other", "Бусад"),
        ]
    )
    is_construction = models.BooleanField("Барилгатай холбоотой", default=False)'''

if "category" not in content[content.find("class Tender("):content.find("class Tender(")+500]:
    content = content.replace(old, new, 1)
    open("apps/public/models.py", "w", encoding="utf-8").write(content)
    print("OK — category нэмэгдлээ")
else:
    print("Байна")