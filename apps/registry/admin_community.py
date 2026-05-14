import os
import uuid

from django import forms
from django.conf import settings
from django.contrib import admin
from django.core.files.storage import default_storage

from .models import Banner, PublicPost


# =========================
# ✅ Banner upload form (models өөрчлөхгүй)
# =========================
class BannerAdminForm(forms.ModelForm):
    image_file = forms.FileField(
        label="Зураг оруулах (FILE)",
        required=False,
        help_text="Файл оруулбал автоматаар media/ дотор хадгалаад image_url-г бөглөнө.",
    )

    class Meta:
        model = Banner
        fields = "__all__"

    def save(self, commit=True):
        obj = super().save(commit=False)

        f = self.cleaned_data.get("image_file")
        if f:
            ext = os.path.splitext(f.name)[1].lower() or ".jpg"
            name = f"banners/{uuid.uuid4().hex}{ext}"
            saved_name = default_storage.save(name, f)

            # image_url-г автоматаар media url болгож өгнө
            obj.image_url = f"{settings.MEDIA_URL}{saved_name}".replace("\\", "/")

        if commit:
            obj.save()
            self.save_m2m()
        return obj


# =========================
# ✅ Давхар register-ээс хамгаалах (unregister -> register)
# =========================
try:
    admin.site.unregister(Banner)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(PublicPost)
except admin.sites.NotRegistered:
    pass


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    form = BannerAdminForm
    list_display = ("title", "is_active", "sort_order", "created_at", "image_url", "link_url")
    list_filter = ("is_active",)
    search_fields = ("title", "image_url", "link_url")
    ordering = ("-is_active", "sort_order", "-created_at")


@admin.register(PublicPost)
class PublicPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_published", "created_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "body", "author__username", "author__email")
    ordering = ("-created_at",)
