from registry.admin_messaging_view import messaging_admin_view
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

from registry.admin_meta_publish import meta_publish_view

urlpatterns = [
    # ✅ Root domain (/) орж ирвэл /public/ руу шууд чиглүүлнэ
    re_path(r"^$", RedirectView.as_view(url="/public/", permanent=False), name="root-to-public"),

    # ✅ Бусад бүх route хэвээр registry.urls дотроо шийдэгдэнэ
    path("", include("registry.urls")),

path("admin/messaging/", admin.site.admin_view(messaging_admin_view), name="admin-messaging"),   
 path("admin/meta-publish/", admin.site.admin_view(meta_publish_view), name="meta-publish"),
    path("admin/", admin.site.urls),
]

# ✅ DEV дээр media (file upload зураг) харагдуулах
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
