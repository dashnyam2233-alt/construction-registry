import os
import requests


class MetaGraphError(Exception):
    pass


def _graph_base() -> str:
    # Default to a stable recent version; you can override via env.
    version = os.environ.get("META_GRAPH_VERSION", "v21.0")
    return f"https://graph.facebook.com/{version}"


def _require_env(name: str) -> str:
    val = os.environ.get(name, "").strip()
    if not val:
        raise MetaGraphError(f"Missing required environment variable: {name}")
    return val


def post_to_facebook_page(message: str, link: str | None = None) -> dict:
    """
    Publish a text (and optional link) post to a Facebook Page.

    Docs: POST /{page-id}/feed (Pages API)
    """
    page_id = _require_env("FB_PAGE_ID")
    page_access_token = _require_env("FB_PAGE_ACCESS_TOKEN")

    url = f"{_graph_base()}/{page_id}/feed"
    data = {
        "message": message,
        "access_token": page_access_token,
    }
    if link:
        data["link"] = link

    r = requests.post(url, data=data, timeout=60)
    try:
        payload = r.json()
    except Exception:
        raise MetaGraphError(f"Facebook response not JSON. Status={r.status_code}, text={r.text}")

    if r.status_code >= 400 or "error" in payload:
        raise MetaGraphError(f"Facebook publish failed: {payload}")

    return payload


def publish_instagram_image(image_url: str, caption: str) -> dict:
    """
    Publish a single-image post to Instagram Business account.

    Flow (Docs):
      1) POST /{ig-user-id}/media  -> create container
      2) POST /{ig-user-id}/media_publish -> publish container

    IMPORTANT:
      - image_url MUST be publicly reachable HTTPS URL (Instagram servers fetch it).
    """
    ig_user_id = _require_env("IG_USER_ID")  # Instagram Business Account ID
    access_token = _require_env("IG_ACCESS_TOKEN")  # Usually same long-lived token, but keep explicit.

    # Step 1: Create media container
    url_create = f"{_graph_base()}/{ig_user_id}/media"
    data_create = {
        "image_url": image_url,
        "caption": caption,
        "access_token": access_token,
    }

    r1 = requests.post(url_create, data=data_create, timeout=60)
    try:
        p1 = r1.json()
    except Exception:
        raise MetaGraphError(f"IG container response not JSON. Status={r1.status_code}, text={r1.text}")

    if r1.status_code >= 400 or "error" in p1 or "id" not in p1:
        raise MetaGraphError(f"IG container create failed: {p1}")

    creation_id = p1["id"]

    # Step 2: Publish
    url_publish = f"{_graph_base()}/{ig_user_id}/media_publish"
    data_publish = {
        "creation_id": creation_id,
        "access_token": access_token,
    }

    r2 = requests.post(url_publish, data=data_publish, timeout=60)
    try:
        p2 = r2.json()
    except Exception:
        raise MetaGraphError(f"IG publish response not JSON. Status={r2.status_code}, text={r2.text}")

    if r2.status_code >= 400 or "error" in p2:
        raise MetaGraphError(f"IG publish failed: {p2}")

    return {
        "container": p1,
        "published": p2,
    }
