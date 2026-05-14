from django.db import models
from django.conf import settings

from apps.registry.models import SearchNormalizedMixin


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