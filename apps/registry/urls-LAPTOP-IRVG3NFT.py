from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home, dashboard, public_home

urlpatterns = [
    path("", home, name="home"),

    # ✅ Public нүүр (business.mn-төстэй)
    path("public/", public_home, name="public-home"),

    # ✅ Login амжилттай бол dashboard руу явна
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            redirect_authenticated_user=True,
            next_page="/dashboard/",
        ),
        name="login",
    ),

    # ✅ Logout нь POST. Гарсны дараа /login/ руу
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),

    path("dashboard/", dashboard, name="dashboard"),
]
