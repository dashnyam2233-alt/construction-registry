from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


def normalize_search_text(value: str) -> str:
    s = (value or "").strip().lower()
    if not s:
        return ""
    return "".join(ch for ch in s if ch.isalnum())


class SearchNormalizedMixin(models.Model):
    search_normalized = models.TextField("Search (normalized)", blank=True, default="", editable=False, db_index=True)

    class Meta:
        abstract = True

    def get_search_source_text(self) -> str:
        return ""

    def save(self, *args, **kwargs):
        self.search_normalized = normalize_search_text(self.get_search_source_text())
        super().save(*args, **kwargs)


CITY_CHOICES = [
    ("UB", "Улаанбаатар"), ("AR", "Архангай"), ("BA", "Баян-Өлгий"),
    ("BY", "Баянхонгор"), ("BU", "Булган"), ("GA", "Говь-Алтай"),
    ("GD", "Говьсүмбэр"), ("DA", "Дархан-Уул"), ("DO", "Дорноговь"),
    ("DU", "Дорнод"), ("DZ", "Дундговь"), ("ZA", "Завхан"),
    ("OR", "Орхон"), ("UV", "Өвөрхангай"), ("OM", "Өмнөговь"),
    ("SU", "Сүхбаатар"), ("SE", "Сэлэнгэ"), ("TO", "Төв"),
    ("UVS", "Увс"), ("HO", "Ховд"), ("HU", "Хөвсгөл"), ("HE", "Хэнтий"),
]

UB_DISTRICT_CHOICES = [
    ("", "---------"), ("BGD", "Баянгол"), ("BZD", "Баянзүрх"),
    ("CHD", "Чингэлтэй"), ("SHD", "Сонгинохайрхан"), ("SBD", "Сүхбаатар"),
    ("HUD", "Хан-Уул"), ("ND", "Налайх"), ("BD", "Багануур"), ("BHD", "Багахангай"),
]

COMPANY_ACTIVITY_DIRECTION_CHOICES = [
    ("CONSTRUCTION", "Барилга угсралт"), ("DESIGN", "Барилгын зураг төсөл"),
    ("ELECTRICAL_INTERNAL", "Барилгын дотор цахилгаан угсралтын ажил"),
    ("PLUMBING_INTERNAL", "Барилгын ус хангамж, ариутгах татуургын угсралт"),
    ("HVAC", "Халаалт, агаар сэлгэлт"), ("COMM_SYSTEM", "Холбоо, дохиолол"),
    ("ENGINEERING_NETWORK", "Инженерийн шугам сүлжээ"), ("EXTERNAL_ROAD", "Гадна зам, талбай"),
    ("MATERIAL_PRODUCTION", "Барилгын материал үйлдвэрлэл"),
    ("MATERIAL_TRADE", "Барилгын материалын худалдаа"),
    ("SUPERVISION", "Барилгын хяналт, зөвлөх үйлчилгээ"),
    ("GEODESY_GEOTECH", "Геодези, геотехник"), ("EQUIPMENT_RENT", "Машин механизм түрээс"),
]

RESPONSIBLE_ROLE_CHOICES = [
    ("GENERAL_DIRECTOR", "Ерөнхий захирал"), ("EXECUTIVE_DIRECTOR", "Гүйцэтгэх захирал"),
    ("CHIEF_ENGINEER", "Ерөнхий инженер"), ("MANAGER", "Менежер"),
    ("ENGINEER", "Инженер"), ("FOREMAN", "Барилгын даамал"),
    ("FINANCIER", "Санхүүч"), ("ECONOMIST", "Эдийн засагч"),
    ("BRIGADE_LEADER", "Бригадын дарга"), ("WORKER", "Ажилтан"), ("OTHER", "Бусад"),
]

ENGINEER_SPECIALTY_CHOICES = [
    ("CIVIL_INDUSTRIAL", "Иргэний ба үйлдвэрлэлийн барилгын инженер"),
    ("SAN_TECH", "Сан техникийн инженер"), ("ROAD_BRIDGE", "Зам гүүрийн инженер"),
    ("GEODESY_SURVEY", "Геодези, маркшейдерийн инженер"),
    ("WATER_SEWER", "Ус хангамж, ариутгах татуургын инженер"),
    ("BUILDING_MATERIALS", "Барилгын материалын инженер"), ("MECHANICAL", "Механик инженер"),
    ("AUTOMOTIVE", "Авто машины инженер"), ("ELECTRICAL", "Цахилгааны инженер"),
    ("POWER", "Эрчим хүчний инженер"), ("HEATING", "Дулааны инженер"),
    ("RENEWABLE", "Сэргээгдэх эрчим хүчний инженер (нар, салхи)"),
    ("AUTOMATION", "Автоматжуулалтын инженер"), ("SOFTWARE", "Програм хангамжийн инженер"),
    ("COMPUTER", "Компьютерийн инженер"), ("NETWORK", "Сүлжээний инженер"),
    ("INFO_SYSTEM", "Мэдээллийн системийн инженер"), ("TELECOM", "Харилцаа холбооны инженер"),
    ("MINING", "Уул уурхайн инженер"), ("GEOLOGY", "Геологийн инженер"),
    ("CHEMICAL", "Химийн инженер"), ("FOOD", "Хүнсний инженер"),
    ("BIOTECH", "Биотехнологийн инженер"), ("ENVIRONMENT", "Байгаль орчны инженер"),
]


class GovernmentOrganization(SearchNormalizedMixin, models.Model):
    name = models.CharField("Нэр", max_length=255)
    register_no = models.CharField("РД/Бүртгэлийн №", max_length=50, blank=True, default="")
    address = models.CharField("Хаяг", max_length=255, blank=True, default="")
    phone = models.CharField("Утас", max_length=50, blank=True, default="")
    email = models.EmailField("Имэйл", blank=True, default="")
    website = models.CharField("Вэб", max_length=255, blank=True, default="")
    note = models.TextField("Тайлбар", blank=True, default="")

    class Meta:
        verbose_name = "Салбарын төрийн байгууллага"
        verbose_name_plural = "Салбарын төрийн байгууллагууд"
        ordering = ("name",)

    def __str__(self): return self.name

    def get_search_source_text(self):
        return " ".join([self.name or "", self.register_no or "", self.address or "",
                         self.phone or "", self.email or "", self.website or "", self.note or ""])


class NonGovernmentOrganization(SearchNormalizedMixin, models.Model):
    name = models.CharField("Нэр", max_length=255)
    register_no = models.CharField("РД/Бүртгэлийн №", max_length=50, blank=True, default="")
    address = models.CharField("Хаяг", max_length=255, blank=True, default="")
    phone = models.CharField("Утас", max_length=50, blank=True, default="")
    email = models.EmailField("Имэйл", blank=True, default="")
    website = models.CharField("Вэб", max_length=255, blank=True, default="")
    note = models.TextField("Тайлбар", blank=True, default="")

    class Meta:
        verbose_name = "Салбарын төрийн бус байгууллага"
        verbose_name_plural = "Салбарын төрийн бус байгууллагууд"
        ordering = ("name",)

    def __str__(self): return self.name

    def get_search_source_text(self):
        return " ".join([self.name or "", self.register_no or "", self.address or "",
                         self.phone or "", self.email or "", self.website or "", self.note or ""])


class Company(SearchNormalizedMixin, models.Model):
    class ActivityType(models.TextChoices):
        DESIGN = "design", "Зураг төсөл"
        CONSTRUCTION = "construction", "Барилга угсралт"
        SUPPLY = "supply", "Материал нийлүүлэлт"
        CONSULTING = "consulting", "Зөвлөх үйлчилгээ"
        OTHER = "other", "Бусад"

    name = models.CharField("Компанийн нэр", max_length=255)
    slug = models.SlugField("URL нэр (slug)", max_length=120, unique=True, blank=True, default="")
    logo = models.ImageField("Лого зураг", upload_to="company_logos/", null=True, blank=True)
    logo_url = models.CharField("Лого URL", max_length=500, blank=True, default="")
    cover = models.ImageField("Ковер зураг", upload_to="company_covers/", null=True, blank=True)
    description = models.TextField("Компанийн тухай (дэлгэрэнгүй)", blank=True, default="")
    established_year = models.CharField("Үүсгэн байгуулагдсан он", max_length=10, blank=True, default="")
    employee_count = models.CharField("Ажилчдын тоо", max_length=50, blank=True, default="")
    facebook_url = models.CharField("Facebook хаяг", max_length=500, blank=True, default="")
    register_no = models.CharField("РД/Бүртгэлийн №", max_length=50, blank=True, default="")
    activity_type = models.CharField("Үйл ажиллагааны төрөл", max_length=32, choices=ActivityType.choices, default=ActivityType.OTHER)
    activity_direction = models.CharField("Үйл ажиллагааны чиглэл", max_length=50, choices=COMPANY_ACTIVITY_DIRECTION_CHOICES, blank=True, default="")
    activity_sub_direction = models.CharField("Дэд сонголт", max_length=120, blank=True, default="")
    city = models.CharField("Хот/Аймаг", max_length=8, choices=CITY_CHOICES, blank=True, default="")
    district = models.CharField("Дүүрэг (УБ үед)", max_length=8, choices=UB_DISTRICT_CHOICES, blank=True, default="")
    address = models.CharField("Дэлгэрэнгүй хаяг", max_length=255, blank=True, default="")
    phone = models.CharField("Утас", max_length=50, blank=True, default="")
    email = models.EmailField("Имэйл", blank=True, default="")
    website = models.CharField("Вэб", max_length=255, blank=True, default="")
    note = models.TextField("Тайлбар", blank=True, default="")

    class Meta:
        verbose_name = "Компани"
        verbose_name_plural = "Компаниудын мэдээлэл"
        ordering = ("name",)

    def __str__(self): return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("company_profile", kwargs={"slug": self.slug})

    @property
    def display_logo_url(self):
        if self.logo:
            try: return self.logo.url
            except Exception: return ""
        return (self.logo_url or "").strip()

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            import re
            base = re.sub(r"[^\w\s-]", "", self.name.lower())
            base = re.sub(r"[\s_-]+", "-", base).strip("-")
            if not base:
                base = f"company-{self.pk or 'new'}"
            slug = base[:80]
            from django.db import models as _m
            qs = Company.objects.filter(slug=slug)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            counter = 1
            orig = slug
            while qs.exists():
                slug = f"{orig}-{counter}"
                counter += 1
                qs = Company.objects.filter(slug=slug)
                if self.pk:
                    qs = qs.exclude(pk=self.pk)
            self.slug = slug
        super().save(*args, **kwargs)

    def get_search_source_text(self):
        return " ".join([self.name or "", self.register_no or "", self.activity_type or "",
                         self.activity_direction or "", self.activity_sub_direction or "",
                         self.city or "", self.district or "", self.address or "",
                         self.phone or "", self.email or "", self.website or "", self.note or ""])


class Worker(SearchNormalizedMixin, models.Model):
    class Gender(models.TextChoices):
        MALE = "male", "Эр"
        FEMALE = "female", "Эм"

    class Profession(models.TextChoices):
        ENGINEER = "engineer", "Инженер"
        ARCHITECT = "architect", "Архитектор"
        FOREMAN = "foreman", "Даамал"
        ACCOUNTANT = "accountant", "Нягтлан"
        HR = "hr", "Хүний нөөц"
        MANAGER = "manager", "Менежер"
        WORKER = "worker", "Ажилчин"
        OTHER = "other", "Бусад"

    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="workers", verbose_name="Харьяалах компани", null=True, blank=True)
    responsible_role = models.CharField("Хариуцсан ажил", max_length=50, choices=RESPONSIBLE_ROLE_CHOICES, blank=True, default="")
    responsible_role_other = models.CharField("Хариуцсан ажил (Бусад үед)", max_length=255, blank=True, default="")
    engineer_specialty = models.CharField("Инженерийн төрөл", max_length=50, choices=ENGINEER_SPECIALTY_CHOICES, blank=True, default="")
    last_name = models.CharField("Ургийн овог", max_length=100, blank=True, default="")
    parent_name = models.CharField("Эцэг/эхийн нэр", max_length=100, blank=True, default="")
    first_name = models.CharField("Нэр", max_length=100)
    gender = models.CharField("Хүйс", max_length=8, choices=Gender.choices, blank=True, default="")
    register_no = models.CharField("Регистр", max_length=20, blank=True, default="")
    birth_date = models.DateField("Төрсөн огноо", null=True, blank=True)
    birth_place_city = models.CharField("Төрсөн газар - Аймаг/Хот", max_length=8, choices=CITY_CHOICES, blank=True, default="")
    birth_place_sub = models.CharField("Төрсөн газар - Сум/Дүүрэг", max_length=64, blank=True, default="")
    married = models.BooleanField("Гэрлэсэн эсэх", default=False)
    profession = models.CharField("Мэргэжил", max_length=32, choices=Profession.choices, default=Profession.OTHER)
    profession_other = models.CharField("Мэргэжил (Бусад үед)", max_length=255, blank=True, default="")
    phone = models.CharField("Утас", max_length=50, blank=True, default="")
    email = models.EmailField("Имэйл", blank=True, default="")
    facebook_url = models.CharField("Facebook хаяг", max_length=255, blank=True, default="")
    instagram_url = models.CharField("Instagram хаяг", max_length=255, blank=True, default="")
    viber = models.CharField("Viber хаяг/дугаар", max_length=100, blank=True, default="")
    city = models.CharField("Хот/Аймаг", max_length=8, choices=CITY_CHOICES, blank=True, default="")
    district = models.CharField("Дүүрэг (УБ үед)", max_length=8, choices=UB_DISTRICT_CHOICES, blank=True, default="")
    address = models.CharField("Оршин суугаа газрын хаяг", max_length=255, blank=True, default="")
    note = models.TextField("Тайлбар", blank=True, default="")

    class Meta:
        verbose_name = "Ажилтан"
        verbose_name_plural = "Ажиллагсадын мэдээлэл"
        ordering = ("first_name", "last_name")

    def clean(self):
        errors = {}
        if (self.profession or "") == self.Profession.OTHER:
            if not (self.profession_other or "").strip():
                errors["profession_other"] = "Мэргэжил 'Бусад' сонгосон тул заавал бичнэ."
        if (self.responsible_role or "") == "OTHER":
            if not (self.responsible_role_other or "").strip():
                errors["responsible_role_other"] = "Хариуцсан ажил 'Бусад' сонгосон тул заавал бичнэ."
        if errors:
            raise ValidationError(errors)
        super().clean()

    def __str__(self):
        full = f"{self.last_name} {self.parent_name} {self.first_name}".strip()
        return " ".join(full.split()).strip() or self.first_name

    def get_search_source_text(self):
        c_name = getattr(self.company, "name", "") or "" if self.company_id and self.company else ""
        c_reg = getattr(self.company, "register_no", "") or "" if self.company_id and self.company else ""
        full = " ".join(f"{self.last_name} {self.parent_name} {self.first_name}".split()).strip()
        return " ".join([full, self.last_name or "", self.parent_name or "", self.first_name or "",
                         self.register_no or "", self.phone or "", self.email or "",
                         self.facebook_url or "", self.instagram_url or "", self.viber or "",
                         self.city or "", self.district or "", self.address or "",
                         self.birth_place_city or "", self.birth_place_sub or "",
                         self.responsible_role or "", self.responsible_role_other or "",
                         self.engineer_specialty or "", self.profession or "", self.profession_other or "",
                         c_name, c_reg, self.note or ""])


class Brigade(SearchNormalizedMixin, models.Model):
    name = models.CharField("Бригадын нэр", max_length=255)
    activity_directions_csv = models.TextField("Үйл ажиллагааны чиглэлүүд", blank=True, default="")
    activity_sub_directions_csv = models.TextField("Дэд сонголтууд", blank=True, default="")
    companies = models.ManyToManyField(Company, related_name="contract_brigades", verbose_name="Хамтарч ажилладаг компаниуд", blank=True)
    leader_worker = models.ForeignKey(Worker, on_delete=models.PROTECT, related_name="lead_brigades", verbose_name="Бригадын ахлагч (Ажиллагсаас сонгох)", null=True, blank=True)
    note = models.TextField("Тайлбар", blank=True, default="")

    class Meta:
        verbose_name = "Барилгын бригад"
        verbose_name_plural = "Барилгын бригадууд"
        ordering = ("name",)

    def __str__(self): return self.name or f"Бригад #{self.pk}"

    def get_activity_direction_codes(self):
        s = (self.activity_directions_csv or "").strip().strip(",")
        return [x for x in s.split(",") if x] if s else []

    def set_activity_direction_codes(self, codes):
        codes = [c.strip() for c in (codes or []) if (c or "").strip()]
        self.activity_directions_csv = ("," + ",".join(codes) + ",") if codes else ""

    def get_activity_sub_codes(self):
        s = (self.activity_sub_directions_csv or "").strip().strip(",")
        return [x for x in s.split(",") if x] if s else []

    def set_activity_sub_codes(self, codes):
        codes = [c.strip() for c in (codes or []) if (c or "").strip()]
        self.activity_sub_directions_csv = ("," + ",".join(codes) + ",") if codes else ""

    def get_activity_directions_display(self):
        code_to_label = dict(COMPANY_ACTIVITY_DIRECTION_CHOICES)
        return ", ".join([code_to_label.get(c, c) for c in self.get_activity_direction_codes()])

    def get_search_source_text(self):
        leader_txt = str(self.leader_worker) if self.leader_worker_id and self.leader_worker else ""
        companies_txt = ""
        try:
            companies_txt = " ".join([str(c) for c in self.companies.all()])
        except Exception:
            pass
        return " ".join([self.name or "", self.activity_directions_csv or "",
                         self.activity_sub_directions_csv or "", leader_txt, companies_txt, self.note or ""])


class BrigadeMember(SearchNormalizedMixin, models.Model):
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, related_name="members", verbose_name="Бригад")
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT, related_name="brigade_memberships", verbose_name="Бригадын гишүүн (Ажиллагсаас сонгох)")

    class Meta:
        verbose_name = "Бригадын гишүүн"
        verbose_name_plural = "Бригадын гишүүд"
        constraints = [models.UniqueConstraint(fields=["brigade", "worker"], name="uniq_brigade_worker")]
        ordering = ("brigade", "worker")

    def __str__(self): return f"{self.brigade} - {self.worker}"

    def get_search_source_text(self):
        return " ".join([str(self.brigade) if self.brigade_id else "", str(self.worker) if self.worker_id else ""])


class FamilyMember(SearchNormalizedMixin, models.Model):
    class RelationType(models.TextChoices):
        SPOUSE = "spouse", "Эхнэр/Нөхөр"
        CHILD = "child", "Хүүхэд"
        PARENT = "parent", "Эцэг/Эх"
        SIBLING = "sibling", "Ах/Эгч/Дүү"
        OTHER = "other", "Бусад"

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="family_members", verbose_name="Ажилтан")
    relation_type = models.CharField("Хамаарал", max_length=16, choices=RelationType.choices, default=RelationType.OTHER)
    last_name = models.CharField("Овог", max_length=120, blank=True, default="")
    first_name = models.CharField("Нэр", max_length=120, blank=True, default="")
    register_no = models.CharField("Регистрийн дугаар", max_length=20, blank=True, default="")
    full_name = models.CharField("Овог нэр (хуучин)", max_length=255, blank=True, default="")
    birth_date = models.DateField("Төрсөн өдөр", null=True, blank=True)
    phone = models.CharField("Утас", max_length=50, blank=True, default="")
    email = models.EmailField("И-мэйл", blank=True, default="")
    facebook_url = models.CharField("Facebook хаяг", max_length=255, blank=True, default="")
    instagram_url = models.CharField("Instagram хаяг", max_length=255, blank=True, default="")
    viber = models.CharField("Viber хаяг/дугаар", max_length=100, blank=True, default="")
    note = models.TextField("Тайлбар", blank=True, default="")

    class Meta:
        verbose_name = "Ажилтаны хамаарал"
        verbose_name_plural = "Ажилтаны хамаарал"
        ordering = ("worker", "first_name", "last_name")

    def save(self, *args, **kwargs):
        composed = " ".join(f"{self.last_name} {self.first_name}".split()).strip()
        if composed:
            self.full_name = composed
        super().save(*args, **kwargs)

    def __str__(self):
        name = " ".join(f"{self.last_name} {self.first_name}".split()).strip() or (self.full_name or "").strip() or "Нэргүй"
        return f"{name} ({self.get_relation_type_display()})"

    def get_search_source_text(self):
        person = " ".join(" ".join([self.last_name or "", self.first_name or ""]).split()).strip()
        worker_txt = str(self.worker) if self.worker_id else ""
        return " ".join([person, self.full_name or "", self.register_no or "",
                         self.phone or "", self.email or "", self.facebook_url or "",
                         self.instagram_url or "", self.viber or "", worker_txt, self.note or ""])


class MessageLog(models.Model):
    CHANNEL_CHOICES = [
        ("email",    "Email"),
        ("sms",      "SMS (Утас)"),
        ("telegram", "Telegram"),
        ("facebook", "Facebook Messenger"),
        ("viber",    "Viber"),
    ]
    STATUS_CHOICES = [
        ("sent",    "Илгээсэн"),
        ("failed",  "Амжилтгүй"),
        ("pending", "Хүлээгдэж байна"),
    ]
    TARGET_CHOICES = [
        ("all_companies", "Бүх компани"),
        ("all_workers",   "Бүх ажиллагсад"),
        ("all_brigades",  "Бүх бригад"),
        ("selected",      "Сонгосон"),
    ]

    sent_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="sent_messages", verbose_name="Илгээсэн хэрэглэгч",
    )
    channel = models.CharField("Суваг", max_length=20, choices=CHANNEL_CHOICES)
    target_type = models.CharField("Хүлээн авагч төрөл", max_length=30, choices=TARGET_CHOICES, default="selected")
    recipient_name = models.CharField("Хүлээн авагчийн нэр", max_length=255, blank=True, default="")
    recipient_address = models.CharField("Хүлээн авагчийн хаяг/дугаар", max_length=255, blank=True, default="")
    subject = models.CharField("Гарчиг", max_length=300, blank=True, default="")
    body = models.TextField("Мессежийн агуулга")
    status = models.CharField("Төлөв", max_length=10, choices=STATUS_CHOICES, default="pending")
    error_message = models.TextField("Алдааны мессеж", blank=True, default="")
    created_at = models.DateTimeField("Илгээсэн огноо", auto_now_add=True)

    class Meta:
        verbose_name = "Мессежийн бүртгэл"
        verbose_name_plural = "Мессежийн бүртгэлүүд"
        ordering = ("-created_at",)

    def __str__(self):
        return f"[{self.get_channel_display()}] {self.recipient_name} — {self.subject or self.body[:50]}"


class SiteConfig(models.Model):
    """Нэг л бичлэгтэй — системийн тохиргоо"""

    sender_name = models.CharField("Илгээгчийн нэр", max_length=100, default="БНБ Систем")
    sender_email = models.EmailField("Илгээгчийн Email", blank=True, default="")
    sender_phone = models.CharField("Илгээгчийн утас", max_length=50, blank=True, default="")

    email_host = models.CharField("SMTP сервер", max_length=255, default="smtp.gmail.com")
    email_port = models.IntegerField("SMTP порт", default=587)
    email_use_tls = models.BooleanField("TLS ашиглах", default=True)
    email_host_user = models.CharField("SMTP хэрэглэгч (email)", max_length=255, blank=True, default="")
    email_host_password = models.CharField("SMTP нууц үг / App Password", max_length=255, blank=True, default="")

    sms_gateway_url = models.CharField("SMS Gateway URL", max_length=500, blank=True, default="")
    sms_gateway_token = models.CharField("SMS Gateway Token", max_length=500, blank=True, default="")
    sms_sender_name = models.CharField("SMS илгээгчийн нэр", max_length=50, default="BNB")

    telegram_bot_token = models.CharField("Telegram Bot Token", max_length=300, blank=True, default="")

    facebook_page_token = models.CharField("Facebook Page Access Token", max_length=500, blank=True, default="")

    viber_auth_token = models.CharField("Viber Auth Token", max_length=300, blank=True, default="")

    site_name = models.CharField("Сайтын нэр", max_length=100, default="Барилгачдын нэгдсэн мэдээллийн бааз")
    site_phone = models.CharField("Сайтын утас", max_length=100, blank=True, default="")
    site_email = models.EmailField("Сайтын email", blank=True, default="")
    site_address = models.CharField("Хаяг", max_length=255, blank=True, default="")
    site_facebook = models.CharField("Facebook хуудас URL", max_length=300, blank=True, default="")

    updated_at = models.DateTimeField("Шинэчилсэн огноо", auto_now=True)

    class Meta:
        verbose_name = "Системийн тохиргоо"
        verbose_name_plural = "Системийн тохиргоо"

    def __str__(self):
        return f"Системийн тохиргоо ({self.sender_email or 'тохируулаагүй'})"

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj