from django.core.management.base import BaseCommand, CommandError

from registry.meta_graph import (
    MetaGraphError,
    post_to_facebook_page,
    publish_instagram_image,
)


class Command(BaseCommand):
    help = "Test publishing to Facebook Page and/or Instagram Business via Meta Graph API."

    def add_arguments(self, parser):
        parser.add_argument("--fb", action="store_true", help="Publish to Facebook Page")
        parser.add_argument("--ig", action="store_true", help="Publish to Instagram Business")
        parser.add_argument("--message", type=str, default="", help="Post text for Facebook (and default caption for IG)")
        parser.add_argument("--link", type=str, default="", help="Optional link for Facebook post")
        parser.add_argument("--image-url", type=str, default="", help="Public HTTPS image URL for Instagram publishing")
        parser.add_argument("--caption", type=str, default="", help="Caption for Instagram (overrides --message if provided)")

    def handle(self, *args, **options):
        do_fb = options["fb"]
        do_ig = options["ig"]
        message = (options["message"] or "").strip()
        link = (options["link"] or "").strip()
        image_url = (options["image_url"] or "").strip()
        caption = (options["caption"] or "").strip() or message

        if not do_fb and not do_ig:
            raise CommandError("Select at least one target: --fb and/or --ig")

        if do_fb and not message:
            raise CommandError("--fb requires --message")

        if do_ig:
            if not image_url:
                raise CommandError("--ig requires --image-url (public HTTPS URL)")
            if not caption:
                raise CommandError("--ig requires --caption or --message")

        try:
            if do_fb:
                self.stdout.write(self.style.NOTICE("Publishing to Facebook Page..."))
                res_fb = post_to_facebook_page(message=message, link=link or None)
                self.stdout.write(self.style.SUCCESS(f"Facebook OK: {res_fb}"))

            if do_ig:
                self.stdout.write(self.style.NOTICE("Publishing to Instagram Business..."))
                res_ig = publish_instagram_image(image_url=image_url, caption=caption)
                self.stdout.write(self.style.SUCCESS(f"Instagram OK: {res_ig}"))

        except MetaGraphError as e:
            raise CommandError(str(e))
