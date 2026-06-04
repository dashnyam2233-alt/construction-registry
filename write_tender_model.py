addon = '''

class Tender(models.Model):
    title = models.CharField("Тендерийн нэр", max_length=500)
    organization = models.CharField("Захиалагч", max_length=300, blank=True, default="")
    price = models.CharField("Үнэ", max_length=100, blank=True, default="")
    deadline = models.CharField("Хугацаа", max_length=20, blank=True, default="")
    method = models.CharField("ХАА журам", max_length=200, blank=True, default="")
    tender_code = models.CharField("Тендерийн дугаар", max_length=100, blank=True, default="")
    url = models.URLField("Холбоос", max_length=500, blank=True, default="")
    is_construction = models.BooleanField("Барилгатай холбоотой", default=False)
    created_at = models.DateTimeField("Нэмсэн огноо", auto_now_add=True)
    updated_at = models.DateTimeField("Шинэчилсэн огноо", auto_now=True)

    class Meta:
        verbose_name = "Тендер"
        verbose_name_plural = "Тендерүүд"
        ordering = ("-created_at",)
        db_table = "public_tender"

    def __str__(self):
        return self.title
'''

content = open("apps/public/models.py", "r", encoding="utf-8").read()
if "class Tender(" not in content:
    with open("apps/public/models.py", "a", encoding="utf-8") as f:
        f.write(addon)
    print("OK — Tender model нэмэгдлээ")
else:
    print("Аль хэдийн байна")