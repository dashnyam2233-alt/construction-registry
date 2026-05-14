from django.db import models
from django.conf import settings


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
        db_table = "registry_messagelog"

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
        db_table = "registry_siteconfig"

    def __str__(self):
        return f"Системийн тохиргоо ({self.sender_email or 'тохируулаагүй'})"

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj