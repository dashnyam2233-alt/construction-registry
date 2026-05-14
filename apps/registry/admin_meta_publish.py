from django import forms
from django.contrib import admin, messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import path

from .integrations.meta_graph import (
    MetaConfig,
    MetaAPIError,
    publish_facebook_text_or_link,
    publish_facebook_photo,
    publish_instagram_image,
)


class MetaPublishForm(forms.Form):
    TARGET_CHOICES = [
        ("fb", "Facebook Page"),
        ("ig", "Instagram Business"),
        ("both", "Facebook + Instagram"),
    ]

    target = forms.ChoiceField(choices=TARGET_CHOICES, initial="both")
    message = forms.CharField(
        label="Text / Caption",
        widget=forms.Textarea(attrs={"rows": 5}),
        required=True,
    )
    link = forms.URLField(
        label="Optional link (Facebook only)",
        required=False,
    )
    image_url = forms.URLField(
        label="Optional image URL (public https)",
        required=False,
    )


def _render_admin_page(request: HttpRequest, form: MetaPublishForm) -> TemplateResponse:
    context = {
        **admin.site.each_context(request),
        "title": "Publish to Facebook / Instagram",
        "form": form,
    }
    return TemplateResponse(request, "admin/meta_publish.html", context)


@staff_member_required
def meta_publish_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = MetaPublishForm(request.POST)
        if not form.is_valid():
            return _render_admin_page(request, form)

        target = form.cleaned_data["target"]
        message = form.cleaned_data["message"].strip()
        link = form.cleaned_data["link"] or None
        image_url = form.cleaned_data["image_url"] or None

        try:
            config = MetaConfig.from_env()

            fb_result = None
            ig_result = None

            if target in ("fb", "both"):
                if image_url:
                    fb_result = publish_facebook_photo(config, image_url=image_url, caption=message)
                else:
                    fb_result = publish_facebook_text_or_link(config, message=message, link=link)

            if target in ("ig", "both"):
                if not image_url:
                    raise MetaAPIError("Instagram publish хийхийн тулд image_url заавал хэрэгтэй.")
                ig_result = publish_instagram_image(config, image_url=image_url, caption=message)

            if fb_result:
                messages.success(request, f"Facebook publish OK. id={fb_result}")
            if ig_result:
                messages.success(request, f"Instagram publish OK. id={ig_result}")

            return redirect("admin:meta-publish")

        except MetaAPIError as e:
            messages.error(request, f"Meta API Error: {e}")
        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")

        return _render_admin_page(request, form)

    form = MetaPublishForm()
    return _render_admin_page(request, form)


def get_meta_admin_urls():
    return [
        path("meta-publish/", admin.site.admin_view(meta_publish_view), name="meta-publish"),
    ]
