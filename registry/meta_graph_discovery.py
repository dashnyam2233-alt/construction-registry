import os
import requests


class MetaGraphError(Exception):
    pass


def _graph_base() -> str:
    version = os.environ.get("META_GRAPH_VERSION", "v21.0")
    return f"https://graph.facebook.com/{version}"


def _require_env(name: str) -> str:
    val = os.environ.get(name, "").strip()
    if not val:
        raise MetaGraphError(f"Missing required environment variable: {name}")
    return val


def _get(path: str, params: dict) -> dict:
    url = f"{_graph_base()}/{path.lstrip('/')}"
    r = requests.get(url, params=params, timeout=60)
    try:
        payload = r.json()
    except Exception:
        raise MetaGraphError(f"Response not JSON. Status={r.status_code}, text={r.text}")

    if r.status_code >= 400 or "error" in payload:
        raise MetaGraphError(f"Graph API error: {payload}")

    return payload


def debug_token(user_access_token: str) -> dict:
    return _get("me", {"fields": "id,name", "access_token": user_access_token})


def list_pages(user_access_token: str) -> dict:
    return _get("me/accounts", {"access_token": user_access_token})


def page_info(page_id: str, page_access_token: str) -> dict:
    fields = "id,name,instagram_business_account"
    return _get(page_id, {"fields": fields, "access_token": page_access_token})


def discover_from_user_token() -> dict:
    user_token = _require_env("META_USER_ACCESS_TOKEN")

    me = debug_token(user_token)
    pages = list_pages(user_token)

    results = {
        "me": me,
        "pages": [],
    }

    for p in pages.get("data", []):
        page_id = p.get("id")
        page_name = p.get("name")
        page_token = p.get("access_token")

        item = {
            "page_id": page_id,
            "page_name": page_name,
            "has_page_access_token": bool(page_token),
            "page_access_token_preview": (page_token[:12] + "...") if page_token else None,
            "page_details": None,
        }

        if page_id and page_token:
            try:
                item["page_details"] = page_info(page_id, page_token)
            except MetaGraphError as e:
                item["page_details"] = {"error": str(e)}

        results["pages"].append(item)

    return results
