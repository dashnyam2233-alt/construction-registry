from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .views import (
    home,
    public_home,
    public_login,
    personal_profile,
    company_profile,
    auth_facebook,
    auth_emongolia,
    auth_bank,
)

urlpatterns = [
    path("", RedirectView.as_view(url="/public/", permanent=False), name="home"),
    path("home/", home, name="home_page"),
    path("public/", public_home, name="public_home"),
    path("login/", public_login, name="login"),
    path("profile/", personal_profile, name="personal_profile"),

    # ✅ ШИНЭ: Компанийн нийтийн хуудас
    path("company/<slug:slug>/", company_profile, name="company_profile"),

    # Social / SSO / Bank
    path("auth/facebook/", auth_facebook, name="auth_facebook"),
    path("auth/emongolia/", auth_emongolia, name="auth_emongolia"),
    path("auth/bank/", auth_bank, name="auth_bank"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/public/"), name="logout"),
    path("dashboard/", RedirectView.as_view(url="/public/", permanent=False)),
]
