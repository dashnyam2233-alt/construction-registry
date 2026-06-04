addon = """

class Ad(models.Model):
    class Category(models.TextChoices):
        HOUSE = "house", "Орон сууц & Барилга"
        MATERIAL = "material", "Материал & Тоног"
        WORKER = "worker", "Ажилтан & Бригад"
        REPAIR = "repair", "Засвар & Үйлчилгээ"
        DESIGN = "design", "Зураг төсөл"
        OTHER = "other", "Бусад"

    class PriceType(models.TextChoices):
        MNT = "mnt", "₮ (Төгрөг)"
        USD = "usd", "$ (Доллар)"
        NEGOTIABLE = "negotiable", "Тохиролцоно"
        FREE = "free", "Үнэгүй"

    class Status(models.TextChoices):
        ACTIVE = "active", "Идэвхтэй"
        INACTIVE = "inactive", "Идэвхгүй"
        PENDING = "pending", "Хүлээгдэж байна"

    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE,
        related_name="ads", verbose_name="Оруулсан хэрэглэгч"
    )
    category = models.CharField(
        "Ангилал", max_length=20,
        choices=Category.choices, default=Category.OTHER
    )
    title = models.CharField("Гарчиг", max_length=200)
    description = models.TextField("Тайлбар", blank=True, default="")
    price = models.DecimalField(
        "Үнэ", max_digits=14, decimal_places=2,
        null=True, blank=True
    )
    price_type = models.CharField(
        "Үнийн төрөл", max_length=20,
        choices=PriceType.choices, default=PriceType.NEGOTIABLE
    )
    city = models.CharField("Хот/Аймаг", max_length=8, blank=True, default="UB")
    district = models.CharField("Дүүрэг/Сум", max_length=8, blank=True, default="")
    contact_name = models.CharField("Холбоо барих нэр", max_length=100, blank=True, default="")
    contact_phone = models.CharField("Утас", max_length=20, blank=True, default="")
    contact_email = models.EmailField("И-мэйл", blank=True, default="")
    image1 = models.ImageField("Зураг 1", upload_to="ads/", null=True, blank=True)
    image2 = models.ImageField("Зураг 2", upload_to="ads/", null=True, blank=True)
    image3 = models.ImageField("Зураг 3", upload_to="ads/", null=True, blank=True)
    status = models.CharField(
        "Төлөв", max_length=20,
        choices=Status.choices, default=Status.ACTIVE
    )
    views = models.PositiveIntegerField("Үзсэн тоо", default=0)
    created_at = models.DateTimeField("Үүсгэсэн огноо", auto_now_add=True)
    updated_at = models.DateTimeField("Шинэчилсэн огноо", auto_now=True)
    expires_at = models.DateTimeField("Дуусах огноо", null=True, blank=True)

    class Meta:
        verbose_name = "Зар"
        verbose_name_plural = "Зарууд"
        ordering = ("-created_at",)
        db_table = "public_ad"

    def __str__(self):
        return self.title

    def get_price_display_full(self):
        if self.price_type == self.PriceType.NEGOTIABLE:
            return "Тохиролцоно"
        if self.price_type == self.PriceType.FREE:
            return "Үнэгүй"
        if self.price:
            symbol = "₮" if self.price_type == self.PriceType.MNT else "$"
            return f"{symbol} {self.price:,.0f}"
        return "—"
"""

content = open("apps/public/models.py", "r", encoding="utf-8").read()
if "class Ad(" not in content:
    with open("apps/public/models.py", "a", encoding="utf-8") as f:
        f.write(addon)
    print("OK — Ad model нэмэгдлээ")
else:
    print("Ad model аль хэдийн байна")