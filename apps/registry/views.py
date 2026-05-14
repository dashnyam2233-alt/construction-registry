from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from apps.core.models import Company, Worker, Brigade
from apps.public.models import Banner, PublicPost, HeroBanner, SliderAd, SubBanner
from apps.accounts.models import AdminGroup, UserCompanyProfile


def home(request):
    if request.user.is_authenticated:
        return redirect("personal_profile")
    return redirect("/public/")


def get_display_name(user):
    if not user.is_authenticated:
        return ""
    full_name = user.get_full_name()
    if full_name:
        return full_name
    return user.username


def _build_public_context(request, tab_override=None):
    user = request.user
    tab = (tab_override or request.GET.get("tab") or "home").strip()

    is_admin_like = (
        user.is_authenticated
        and (
            user.is_superuser
            or user.is_staff
            or user.groups.filter(name__in=["ADMIN_FULL"]).exists()
        )
    )

    banners_qs = Banner.objects.filter(is_active=True).order_by("sort_order", "-created_at", "-id")
    banners = list(banners_qs[:50])

    posts_qs = PublicPost.objects.filter(is_published=True).select_related("author").order_by("-created_at", "-id")

    featured_admin_post = (
        posts_qs.filter(author__is_superuser=True).first()
        or posts_qs.filter(author__is_staff=True).first()
        or posts_qs.filter(author__groups__name__in=["ADMIN_FULL"]).distinct().first()
    )

    chat_stream = list(posts_qs[:200])
    hero_banner = HeroBanner.objects.filter(is_active=True).order_by("sort_order", "-created_at").first()
    slider_ads = list(SliderAd.objects.filter(is_active=True).order_by("sort_order", "-created_at")[:10])
    sub_banner = SubBanner.objects.filter(is_active=True).order_by("sort_order", "-created_at").first()

    contact = {
        "title": "Холбоо барих",
        "subtitle": "Санал хүсэлт, хамтын ажиллагаа, зар сурталчилгаа зэрэгт бидэнтэй холбогдоорой.",
        "phone": "+976 9911-2233",
        "email": "info@construction.mn",
        "address": "Улаанбаатар хот, СБД, 1-р хороо",
        "hours": "Даваа–Баасан 09:00–18:00",
        "facebook": "https://facebook.com/",
        "website": "https://example.com",
    }

    return {
        "tab": tab,
        "contact": contact,
        "banners": banners,
        "featured_admin_post": featured_admin_post,
        "chat_stream": chat_stream,
        "is_admin_like": is_admin_like,
        "can_post": user.is_authenticated,
        "display_name": get_display_name(user),
        "hero_banner": hero_banner,
        "slider_ads": slider_ads,
        "sub_banner": sub_banner,
    }


def public_home(request):
    user = request.user
    post_error = ""
    if request.method == "POST" and request.POST.get("action") == "new_post":
        if not user.is_authenticated:
            return redirect("/login/")
        title = (request.POST.get("post_title") or "").strip()
        body = (request.POST.get("post_body") or "").strip()
        if not body:
            post_error = "Чатын бичвэр хоосон байна."
        else:
            if not title:
                title = timezone.now().strftime("Чат %Y-%m-%d %H:%M")
            PublicPost.objects.create(author=user, title=title, body=body, is_published=True)
            return redirect("/public/")

    context = _build_public_context(request)
    context["post_error"] = post_error
    return render(request, "registry/public_home.html", context)


def public_login(request):
    if request.user.is_authenticated:
        return redirect("/public/")

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("/public/")

    context = _build_public_context(request, tab_override="home")
    context["login_form"] = form
    context["show_login"] = True
    return render(request, "registry/public_home.html", context)


# =====================================================
# ✅ ШИНЭ: Компанийн нийтийн хуудас
# =====================================================
def company_profile(request, slug):
    company = get_object_or_404(Company, slug=slug)

    workers_qs = Worker.objects.filter(company=company).order_by("responsible_role", "first_name")
    brigades_qs = Brigade.objects.filter(companies=company).distinct()

    is_auth = request.user.is_authenticated

    is_owner = False
    if is_auth:
        prof = getattr(request.user, "company_profile", None)
        if prof and prof.company_id == company.id:
            is_owner = True
        if request.user.is_superuser or request.user.is_staff:
            is_owner = True

    context = {
        "company": company,
        "workers": list(workers_qs) if is_auth else list(workers_qs[:3]),
        "workers_total": workers_qs.count(),
        "brigades": list(brigades_qs) if is_auth else list(brigades_qs[:2]),
        "brigades_total": brigades_qs.count(),
        "is_auth": is_auth,
        "is_owner": is_owner,
        "display_name": get_display_name(request.user),
    }
    return render(request, "registry/company_profile.html", context)


@login_required
def personal_profile(request):
    user = request.user

    if request.session.get("profile_unlocked") is True:
        profile = UserCompanyProfile.objects.filter(user=user).select_related("company").first()
        company = profile.company if profile else None
        return render(request, "registry/profile.html", {"company": company})

    error = ""
    if request.method == "POST":
        password = (request.POST.get("password") or "").strip()
        if not password:
            error = "Нууц үгээ оруулна уу."
        else:
            authed = authenticate(request, username=user.get_username(), password=password)
            if authed is None:
                error = "Нууц үг буруу байна."
            else:
                request.session["profile_unlocked"] = True
                return redirect("personal_profile")

    return render(request, "registry/profile.html", {"lock_mode": True, "error": error})


def auth_facebook(request):
    return render(request, "registry/auth_stub.html", {"provider": "Facebook"})


def auth_emongolia(request):
    return render(request, "registry/auth_stub.html", {"provider": "e-Mongolia"})


def auth_bank(request):
    return render(request, "registry/auth_stub.html", {"provider": "Банкны код"})
