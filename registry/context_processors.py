# registry/context_processors.py

def public_sidebar(request):
    """
    Admin + User аль алинд нь sidebar дээр:
    - banners
    - posts
    өгч өгнө.
    """
    banners = []
    posts = []

    try:
        from .models import Banner
        banners = list(
            Banner.objects.filter(is_active=True)
            .order_by("sort_order", "-created_at", "-id")[:5]
        )
    except Exception:
        banners = []

    try:
        from .models import PublicPost
        posts = list(
            PublicPost.objects.filter(is_published=True)
            .select_related("author")
            .order_by("-created_at", "-id")[:20]
        )
    except Exception:
        posts = []

    return {
        "banners": banners,
        "posts": posts,
    }
