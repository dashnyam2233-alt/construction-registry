from django.db import models
from django.conf import settings

from apps.core.models import SearchNormalizedMixin


class PublicPost(SearchNormalizedMixin, models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="public_posts",
        verbose_name="Нийтэлсэн хэрэглэгч",
    )
    title = models.CharField("Гарчиг", max_length=200)
    body = models.TextField("Агуулга", blank=True, default="")
    created_at = models.DateTimeField("Үүссэн огноо", auto_now_add=True)
    updated_at = models.DateTimeField("Шинэчилсэн огноо", auto_now=True)
    is_published = models.BooleanField("Нийтлэх эсэх", default=True)

    class Meta:
        verbose_name = "Нээлттэй пост"
        verbose_name_plural = "Нээлттэй постууд"
        ordering = ("-created_at",)
        db_table = "registry_publicpost"

    def __str__(self):
        return self.title or f"Post #{self.pk}"

    def get_search_source_text(self):
        a_username = getattr(self.author, "username", "") or ""
        a_email = getattr(self.author, "email", "") or ""
        return " ".join([self.title or "", self.body or "", a_username, a_email])


class Banner(SearchNormalizedMixin, models.Model):
    title = models.CharField("Нэр/тайлбар", max_length=200, blank=True, default="")
    image = models.ImageField("Зураг (File)", upload_to="banners/", null=True, blank=True)
    image_url = models.CharField("Зургийн URL", max_length=500, blank=True, default="")
    link_url = models.CharField("Дарахад орох холбоос (URL)", max_length=500, blank=True, default="")
    sort_order = models.IntegerField("Эрэмбэ", default=0)
    is_active = models.BooleanField("Идэвхтэй эсэх", default=True)
    created_at = models.DateTimeField("Үүссэн огноо", auto_now_add=True)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннерууд"
        ordering = ("-is_active", "sort_order", "-created_at")
        db_table = "registry_banner"

    def __str__(self):
        return self.title or f"Banner #{self.pk}"

    @property
    def display_image_url(self):
        if self.image:
            try:
                return self.image.url
            except Exception:
                return ""
        return (self.image_url or "").strip()

    def get_search_source_text(self):
        return " ".join([self.title or "", self.image_url or "", self.link_url or ""])


class HeroBanner(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = "image", "Зураг"
        VIDEO = "video", "Видео"

    title = models.CharField("Гарчиг", max_length=200, blank=True, default="")
    subtitle = models.TextField("Дэд гарчиг / тайлбар", blank=True, default="")
    media_type = models.CharField("Медиа төрөл", max_length=10, choices=MediaType.choices, default=MediaType.IMAGE)
    image = models.ImageField("Зураг (upload)", upload_to="hero/", null=True, blank=True)
    image_url = models.CharField("Зургийн URL", max_length=500, blank=True, default="")
    video = models.FileField("Видео (upload)", upload_to="hero_video/", null=True, blank=True)
    video_url = models.CharField("Видео URL (YouTube/MP4)", max_length=500, blank=True, default="")
    btn1_text = models.CharField("Товч 1 текст", max_length=100, blank=True, default="")
    btn1_url = models.CharField("Товч 1 холбоос", max_length=500, blank=True, default="")
    btn2_text = models.CharField("Товч 2 текст", max_length=100, blank=True, default="")
    btn2_url = models.CharField("Товч 2 холбоос", max_length=500, blank=True, default="")
    is_active = models.BooleanField("Идэвхтэй эсэх", default=True)
    sort_order = models.IntegerField("Эрэмбэ", default=0)
    created_at = models.DateTimeField("Үүссэн огноо", auto_now_add=True)

    class Meta:
        verbose_name = "Hero баннер (зүүн 1/3 зураг/видео)"
        verbose_name_plural = "Hero баннерууд (зүүн 1/3 зураг/видео)"
        ordering = ("sort_order", "-created_at")
        db_table = "registry_herobanner"

    def __str__(self):
        return self.title or f"HeroBanner #{self.pk}"

    @property
    def display_media_url(self):
        if self.media_type == self.MediaType.VIDEO:
            if self.video:
                try:
                    return self.video.url
                except Exception:
                    return ""
            return (self.video_url or "").strip()
        else:
            if self.image:
                try:
                    return self.image.url
                except Exception:
                    return ""
            return (self.image_url or "").strip()


class SliderAd(models.Model):
    title = models.CharField("Гарчиг", max_length=200)
    description = models.CharField("Богино тайлбар", max_length=300, blank=True, default="")
    image = models.ImageField("Зураг (upload)", upload_to="slider_ads/", null=True, blank=True)
    image_url = models.CharField("Зургийн URL", max_length=500, blank=True, default="")
    link_url = models.CharField("Холбоос (дарахад орох)", max_length=500, blank=True, default="")
    is_active = models.BooleanField("Идэвхтэй эсэх", default=True)
    sort_order = models.IntegerField("Эрэмбэ", default=0)
    created_at = models.DateTimeField("Үүссэн огноо", auto_now_add=True)

    class Meta:
        verbose_name = "Урсдаг зар"
        verbose_name_plural = "Урсдаг зарууд"
        ordering = ("sort_order", "-created_at")
        db_table = "registry_sliderad"

    def __str__(self):
        return self.title or f"SliderAd #{self.pk}"

    @property
    def display_image_url(self):
        if self.image:
            try:
                return self.image.url
            except Exception:
                return ""
        return (self.image_url or "").strip()


class SubBanner(models.Model):
    title = models.CharField("Нэр/тайлбар", max_length=200, blank=True, default="")
    image = models.ImageField("Зураг (upload)", upload_to="sub_banners/", null=True, blank=True)
    image_url = models.CharField("Зургийн URL", max_length=500, blank=True, default="")
    link_url = models.CharField("Холбоос (дарахад орох)", max_length=500, blank=True, default="")
    is_active = models.BooleanField("Идэвхтэй эсэх", default=True)
    sort_order = models.IntegerField("Эрэмбэ", default=0)
    created_at = models.DateTimeField("Үүссэн огноо", auto_now_add=True)

    class Meta:
        verbose_name = "Дэд баннер (баруун дээд хэсэг)"
        verbose_name_plural = "Дэд баннерууд (баруун дээд хэсэг)"
        ordering = ("sort_order", "-created_at")
        db_table = "registry_subbanner"

    def __str__(self):
        return self.title or f"SubBanner #{self.pk}"

    @property
    def display_image_url(self):
        if self.image:
            try:
                return self.image.url
            except Exception:
                return ""
        return (self.image_url or "").strip()

class Ad(models.Model):
    class Category(models.TextChoices):
        MATERIAL = "material", "Материал"
        EQUIPMENT = "equipment", "Тоног төхөөрөмж"
        RENTAL = "rental", "Түрээс"
        REALESTATE = "realestate", "Үл хөдлөх хөрөнгө"
        SERVICE = "service", "Барилгын үйлчилгээ"
        DESIGN = "design", "Зураг төсөв, дизайн"
        WORKER = "worker", "Ажилтан, ажлын зар"
        TENDER = "tender", "Тендер, төсөл"
        COMPANY = "company", "Компаниуд"
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
    material_subcategory = models.CharField(
        "Материалын үндсэн ангилал", max_length=30, blank=True, default=""
    )
    material_item = models.CharField(
        "Материалын дэд ангилал", max_length=30, blank=True, default=""
    )
    price_unit = models.CharField(
        "Үнийн нэгж", max_length=20, blank=True, default="",
        choices=[
            ("ton", "₮ / тонн"),
            ("piece", "₮ / ш"),
            ("m2", "₮ / м²"),
            ("m3", "₮ / м³"),
            ("kg", "₮ / кг"),
            ("meter", "₮ / м"),
            ("negotiable", "Тохиролцоно"),
        ]
    )
    house_rooms = models.CharField(
        "Өрөөний тоо", max_length=20, blank=True, default="",
        choices=[
            ("r1", "1 өрөө"),
            ("r2", "2 өрөө"),
            ("r3", "3 өрөө"),
            ("r3plus", "3-аас дээш өрөө"),
            ("duplex", "Дуплекс"),
            ("studio", "Студи"),
        ]
    )
    house_location = models.CharField(
        "Байршил (дүүрэг/аймаг)", max_length=30, blank=True, default=""
    )
    house_location_type = models.CharField(
        "Байршлын төрөл", max_length=10, blank=True, default="",
        choices=[("ub", "Улаанбаатар"), ("province", "Орон нутаг")]
    )
    house_type = models.CharField(
        "Зарын төрөл", max_length=20, blank=True, default="",
        choices=[
            ("sale", "Зарна"),
            ("rent", "Түрээслэнэ"),
            ("buy", "Худалдаж авна"),
            ("rent_partial", "Хэсэгчлэн түрээслэнэ"),
        ]
    )
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


class Tender(models.Model):
    title = models.CharField("Тендерийн нэр", max_length=500)
    organization = models.CharField("Захиалагч", max_length=300, blank=True, default="")
    price = models.CharField("Үнэ", max_length=100, blank=True, default="")
    deadline = models.CharField("Хугацаа", max_length=20, blank=True, default="")
    open_date = models.CharField("Нээгдэх огноо", max_length=20, blank=True, default="")
    method = models.CharField("ХАА журам", max_length=200, blank=True, default="")
    tender_code = models.CharField("Тендерийн дугаар", max_length=100, blank=True, default="")
    url = models.URLField("Холбоос", max_length=500, blank=True, default="")
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
            ("consulting", "Зөвлөх"),
            ("service", "Үйлчилгээ"),
            ("other", "Бусад"),
        ]
    )
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


class MaterialPrice(models.Model):
    CATEGORIES = [
        # 1. Материал
        ("mat_cement", "1. Материал — Цемент, шохой"),
        ("mat_sand", "1. Материал — Элс, хайрга, дайрга"),
        ("mat_brick", "1. Материал — Тоосго, блок"),
        ("mat_rebar", "1. Материал — Арматур, төмөр"),
        ("mat_wood", "1. Материал — Модон материал"),
        ("mat_roof", "1. Материал — Дээврийн материал"),
        ("mat_insulation", "1. Материал — Дулаалга"),
        ("mat_window", "1. Материал — Цонх, хаалга"),
        ("mat_interior", "1. Материал — Дотор засал"),
        ("mat_plumbing", "1. Материал — Сантехник"),
        ("mat_electrical", "1. Материал — Цахилгаан"),
        ("mat_other", "1. Материал — Бусад материал"),
        # 2. Цалин
        ("labor_general", "2. Цалин — Барилгачин"),
        ("labor_special", "2. Цалин — Мэргэжилтэн"),
        ("labor_engineer", "2. Цалин — Инженер, хяналт"),
        # 3. Тээвэр
        ("transport_material", "3. Тээвэр — Материал тээвэр"),
        ("transport_waste", "3. Тээвэр — Хог зайлуулах"),
        ("transport_other", "3. Тээвэр — Бусад тээвэр"),
        # 4. Машин механизм
        ("machine_crane", "4. Машин механизм — Кран"),
        ("machine_excavator", "4. Машин механизм — Экскаватор"),
        ("machine_concrete", "4. Машин механизм — Бетон зуурагч"),
        ("machine_other", "4. Машин механизм — Бусад машин"),
        # 5. Бусад
        ("other_design", "5. Бусад — Зураг төсөл"),
        ("other_vat", "5. Бусад — НӨАТ"),
        ("other_permit", "5. Бусад — Зөвшөөрөл, бүртгэл"),
        ("other_insurance", "5. Бусад — Даатгал"),
        ("other_misc", "5. Бусад — Бусад"),
    ]

    category = models.CharField("Ангилал", max_length=30, choices=CATEGORIES)
    name = models.CharField("Материалын нэр", max_length=200)
    unit = models.CharField("Нэгж", max_length=30)
    price_min = models.DecimalField("Доод үнэ", max_digits=12, decimal_places=0)
    price_max = models.DecimalField("Дээд үнэ", max_digits=12, decimal_places=0)
    note = models.CharField("Тайлбар", max_length=300, blank=True, default="")
    updated_at = models.DateTimeField("Шинэчилсэн", auto_now=True)
    is_active = models.BooleanField("Идэвхтэй", default=True)

    class Meta:
        verbose_name = "Материалын үнэ"
        verbose_name_plural = "Материалын үнэнүүд"
        ordering = ("category", "name")

    def __str__(self):
        return f"{self.name} — {self.price_min:,}₮/{self.unit}"
    
    @property
    def price_avg(self):
        return (self.price_min + self.price_max) / 2

from django.db import models

class MaterialNorm(models.Model):
    BUILDING_TYPES = [
        ('low_rise', 'Амины орон сууц (1-2 давхар)'),
        ('mid_rise', 'Олон айлын орон сууц (3-9 давхар)'),
        ('high_rise', 'Өндөр давхар (10+ давхар)'),
        ('office', 'Оффисын барилга'),
        ('warehouse', 'Агуулах'),
        ('other', 'Бусад'),
    ]
    WORK_TYPES = [
        ('foundation', 'Суурь'),
        ('wall', 'Хана'),
        ('insulation', 'Дулаалга'),
        ('slab', 'Хучилт'),
        ('roof', 'Дээвэр'),
        ('floor', 'Шал'),
        ('interior', 'Дотор засал'),
        ('window', 'Цонх, хаалга'),
        ('engineering', 'Инженерийн систем'),
        ('labor', 'Ажилчид'),
        ('other', 'Бусад'),
    ]
    building_type = models.CharField('Барилгын төрөл', max_length=20, choices=BUILDING_TYPES)
    work_type = models.CharField('Ажлын төрөл', max_length=20, choices=WORK_TYPES)
    material_name = models.CharField('Материалын нэр', max_length=200)
    norm_per_m2 = models.DecimalField('1м²-д орох норм', max_digits=10, decimal_places=4)
    unit = models.CharField('Нэгж', max_length=20)
    db_category = models.CharField('DB ангилал', max_length=50, blank=True)
    db_name_contains = models.CharField('DB нэр хайх', max_length=100, blank=True)
    notes = models.TextField('Тайлбар', blank=True)
    is_active = models.BooleanField('Идэвхтэй', default=True)

    class Meta:
        verbose_name = 'Материалын норм'
        verbose_name_plural = 'Материалын нормууд'
        ordering = ['building_type', 'work_type']

    def __str__(self):
        return f"{self.get_building_type_display()} | {self.material_name} | {self.norm_per_m2}{self.unit}/м²"
