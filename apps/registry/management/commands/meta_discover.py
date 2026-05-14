import json
from django.core.management.base import BaseCommand, CommandError

from apps.registry.meta_graph_discovery import MetaGraphError, discover_from_user_token


class Command(BaseCommand):
    help = "Discover Facebook Pages and connected Instagram Business account using META_USER_ACCESS_TOKEN."

    def handle(self, *args, **options):
        try:
            res = discover_from_user_token()
        except MetaGraphError as e:
            raise CommandError(str(e))

        self.stdout.write(json.dumps(res, indent=2, ensure_ascii=False))

        self.stdout.write("\n=== SUMMARY ===")
        me = res.get("me", {})
        self.stdout.write(f"User: {me.get('name')} (id={me.get('id')})")

        pages = res.get("pages", [])
        self.stdout.write(f"Pages found: {len(pages)}\n")

        for i, p in enumerate(pages, start=1):
            page_id = p.get("page_id")
            page_name = p.get("page_name")
            details = (p.get("page_details") or {})
            ig = details.get("instagram_business_account") if isinstance(details, dict) else None

            self.stdout.write(f"{i}) Page: {page_name} (id={page_id})")
            if isinstance(details, dict) and details.get("error"):
                self.stdout.write(f"   Page details error: {details.get('error')}")
            else:
                if ig and isinstance(ig, dict) and ig.get("id"):
                    self.stdout.write(f"   ✅ Connected IG Business Account ID (IG_USER_ID): {ig.get('id')}")
                else:
                    self.stdout.write("   ❌ No instagram_business_account connected (or no permission/token)")
