import os
import re
from pathlib import Path

ROOT = Path("apps/registry")
MODELS = ["PublicPost", "Banner", "HeroBanner", "SliderAd", "SubBanner"]

for py in ROOT.rglob("*.py"):
    text = py.read_text(encoding="utf-8")
    orig = text

    # Replace: from .models import X, Y, Z  (where X/Y/Z includes our 5)
    # Strategy: scan import lines and split them
    def replace_import(match):
        prefix = match.group(1)  # "from .models import" or "from apps.registry.models import"
        items_raw = match.group(2)
        items = [i.strip() for i in items_raw.split(",")]
        public_items = [i for i in items if i in MODELS]
        registry_items = [i for i in items if i not in MODELS and i]
        lines = []
        if registry_items:
            lines.append(f"{prefix} {', '.join(registry_items)}")
        if public_items:
            lines.append(f"from apps.public.models import {', '.join(public_items)}")
        return "\n".join(lines)

    # Single-line imports
    text = re.sub(
        r"(from \.models import|from apps\.registry\.models import)\s+([A-Za-z_, ]+)",
        replace_import,
        text,
    )

    if text != orig:
        py.write_text(text, encoding="utf-8")
        print(f"Updated: {py}")

print("Done.")