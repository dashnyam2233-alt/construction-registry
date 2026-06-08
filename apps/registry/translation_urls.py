from django.urls import path
from . import translation_views as views

urlpatterns = [
    path("content/", views.translate_content, name="translate_content"),
    path("set-lang/<str:lang_code>/", views.set_language, name="set_language"),
]