from django import template
from apps.registry.models import Banner, PublicPost

register = template.Library()


@register.inclusion_tag("admin/_sidebar_registry.html")
def registry_admin_sidebar():
    banners = list(
        Banner.objects.filter(is_active=True).order_by("sort_order", "-created_at", "-id")[:10]
    )
    posts = list(
        PublicPost.objects.filter(is_published=True)
        .select_related("author")
        .order_by("-created_at", "-id")[:12]
    )
    return {"sidebar_banners": banners, "sidebar_posts": posts}
