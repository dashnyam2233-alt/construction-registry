from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Q, Count
from django.utils import timezone

from .models import Worker, UserCompanyProfile, Brigade

# ✅ Banner + PublicPost models байгаа гэж үзээд импортлоно
# (Танайд model нэр өөр байвал энд алдаа гарна — тэр үед model нэрийг нь хэлээрэй.)
from apps.public.models import Banner, PublicPost


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect(f'{reverse("login")}?next={reverse("dashboard")}')


def public_home(request):
    """
    ✅ Business.mn-төстэй PUBLIC нүүр.
    - Login шаардахгүй
    - Демо маягаар Banner/PublicPost-оос уншина (байгаа бол)
    - Хэрвээ model байхгүй эсвэл хоосон байвал page зүгээр харагдана
    """
    # Баннерууд (public дээр)
    banners_qs = (
        Banner.objects
        .filter(is_active=True)
        .order_by("sort_order", "-created_at", "-id")
    )
    banners = list(banners_qs[:6])

    # Постууд (public дээр)
    posts_qs = (
        PublicPost.objects
        .filter(is_published=True)
        .select_related("author")
        .order_by("-created_at", "-id")
    )
    posts = list(posts_qs[:25])

    # Featured болгож 1-г тусад нь гаргана
    featured = posts[0] if posts else None
    rest_posts = posts[1:] if len(posts) > 1 else []

    context = {
        "banners": banners,
        "featured": featured,
        "posts": rest_posts,
    }
    return render(request, "registry/public_home.html", context)


@login_required
def dashboard(request):
    user = request.user

    profile = (
        UserCompanyProfile.objects
        .filter(user=user)
        .select_related("company")
        .first()
    )
    company = profile.company if profile else None

    # ✅ "Admin сонгосон хэсэг" = group / staff / superuser-ээр удирдана
    is_admin_like = (
        user.is_superuser
        or user.is_staff
        or user.groups.filter(name__in=["ADMIN_FULL"]).exists()
    )

    # ✅ Баннерууд (login хийсэн бүх хүнд харагдана)
    banners_qs = (
        Banner.objects
        .filter(is_active=True)
        .order_by("sort_order", "-created_at", "-id")
    )
    banners = list(banners_qs[:5])

    # ✅ Постууд (login хийсэн бүх хүнд харагдана)
    posts_qs = (
        PublicPost.objects
        .filter(is_published=True)
        .select_related("author")
        .order_by("-created_at", "-id")
    )

    post_error = ""

    # ✅ Шинэ пост нэмэх (dashboard дээрээс)
    if request.method == "POST" and request.POST.get("action") == "new_post":
        title = (request.POST.get("post_title") or "").strip()
        body = (request.POST.get("post_body") or "").strip()

        if not body:
            post_error = "Пост бичвэр хоосон байна."
        else:
            if not title:
                title = timezone.now().strftime("Пост %Y-%m-%d %H:%M")

            PublicPost.objects.create(
                author=user,
                title=title,
                body=body,
                is_published=True,
            )

            return redirect("dashboard")

    posts = list(posts_qs[:20])

    q = (request.GET.get("q") or "").strip()

    if not company:
        context = {
            "company": None,
            "q": q,
            "workers": [],
            "workers_count": 0,
            "company_workers_total": 0,
            "brigades": [],
            "brigades_count": 0,
            "show_sensitive": is_admin_like,

            # ✅ sidebar
            "banners": banners,
            "posts": posts,
            "post_error": post_error,
        }
        return render(request, "dashboard.html", context)

    # ========== Workers ==========
    workers_qs = Worker.objects.filter(company=company).order_by("last_name", "first_name", "id")
    company_workers_total = workers_qs.count()

    if q:
        workers_qs = workers_qs.filter(
            Q(first_name__icontains=q)
            | Q(last_name__icontains=q)
            | Q(parent_name__icontains=q)
            | Q(register_no__icontains=q)
            | Q(phone__icontains=q)
            | Q(email__icontains=q)
        )

    # ========== Brigades ==========
    brigades_qs = (
        Brigade.objects
        .filter(companies=company)
        .distinct()
        .annotate(member_count=Count("members"))
        .order_by("name", "id")
    )

    context = {
        "company": company,
        "q": q,
        "workers": list(workers_qs[:200]),
        "workers_count": workers_qs.count(),
        "company_workers_total": company_workers_total,
        "brigades": list(brigades_qs[:200]),
        "brigades_count": brigades_qs.count(),
        "show_sensitive": is_admin_like,

        # ✅ sidebar
        "banners": banners,
        "posts": posts,
        "post_error": post_error,
    }
    return render(request, "dashboard.html", context)
