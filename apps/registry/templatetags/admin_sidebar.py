from django import template
from apps.public.models import Banner, PublicPost, Ad, SliderAd

register = template.Library()

@register.inclusion_tag("admin/_sidebar_registry.html")
def registry_admin_sidebar():
    banners = list(
        Banner.objects.filter(is_active=True).order_by("sort_order", "-created_at")[:6]
    )
    posts = list(
        PublicPost.objects.filter(is_published=True)
        .select_related("author")
        .order_by("-created_at")[:8]
    )
    ads = list(
        Ad.objects.filter(status="active").order_by("-created_at")[:6]
    )
    slider_ads = list(
        SliderAd.objects.filter(is_active=True).order_by("sort_order")[:5]
    )
    ads_total = Ad.objects.count()
    ads_active = Ad.objects.filter(status="active").count()
    return {
        "sidebar_banners": banners,
        "sidebar_posts": posts,
        "sidebar_ads": ads,
        "slider_ads": slider_ads,
        "ads_total": ads_total,
        "ads_active": ads_active,
    }
