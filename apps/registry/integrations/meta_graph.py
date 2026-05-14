import os
from dataclasses import dataclass
from typing import Optional, Dict, Any

import requests

GRAPH_API_VERSION = os.getenv("META_GRAPH_API_VERSION", "v24.0")
GRAPH_API_BASE = f"https://graph.facebook.com/{GRAPH_API_VERSION}"


class MetaAPIError(Exception):
    pass


@dataclass(frozen=True)
class MetaConfig:
    page_id: str
    page_access_token: str
    ig_user_id: str

    @staticmethod
    def from_env() -> "MetaConfig":
        page_id = os.getenv("META_PAGE_ID", "").strip()
        page_access_token = os.getenv("META_PAGE_ACCESS_TOKEN", "").strip()
        ig_user_id = os.getenv("META_IG_USER_ID", "").strip()

        missing = [k for k, v in {
            "META_PAGE_ID": page_id,
            "META_PAGE_ACCESS_TOKEN": page_access_token,
            "META_IG_USER_ID": ig_user_id,
        }.items() if not v]

        if missing:
            raise MetaAPIError(
                "Missing environment variables: " + ", ".join(missing)
            )

        return MetaConfig(
            page_id=page_id,
            page_access_token=page_access_token,
            ig_user_id=ig_user_id,
        )


def _post(url: str, data: Dict[str, Any], timeout: int = 30) -> Dict[str, Any]:
    r = requests.post(url, data=data, timeout=timeout)
    payload = r.json()
    if r.status_code >= 400 or "error" in payload:
        raise MetaAPIError(payload)
    return payload


def publish_facebook_text_or_link(config: MetaConfig, message: str, link: Optional[str] = None) -> str:
    url = f"{GRAPH_API_BASE}/{config.page_id}/feed"
    data = {
        "message": message,
        "access_token": config.page_access_token,
    }
    if link:
        data["link"] = link
    return _post(url, data).get("id", "")


def publish_facebook_photo(config: MetaConfig, image_url: str, caption: Optional[str] = None) -> str:
    url = f"{GRAPH_API_BASE}/{config.page_id}/photos"
    data = {
        "url": image_url,
        "access_token": config.page_access_token,
    }
    if caption:
        data["caption"] = caption
    return _post(url, data).get("post_id", "")


def publish_instagram_image(config: MetaConfig, image_url: str, caption: str) -> str:
    create_url = f"{GRAPH_API_BASE}/{config.ig_user_id}/media"
    creation = _post(create_url, {
        "image_url": image_url,
        "caption": caption,
        "access_token": config.page_access_token,
    })

    publish_url = f"{GRAPH_API_BASE}/{config.ig_user_id}/media_publish"
    published = _post(publish_url, {
        "creation_id": creation["id"],
        "access_token": config.page_access_token,
    })

    return published.get("id", "")
