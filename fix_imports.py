import os
import re

FILES = [
    r"apps\registry\admin.py",
    r"apps\registry\admin_messaging_view.py",
    r"apps\registry\forms.py",
    r"apps\registry\import_resources.py",
    r"apps\registry\import_templates.py",
    r"apps\registry\resources.py",
    r"apps\registry\views.py",
]

# Names that moved to apps.core.models
CORE_NAMES = {
    "Company", "Worker", "Brigade", "BrigadeMember", "FamilyMember",
    "GovernmentOrganization", "NonGovernmentOrganization",
    "CITY_CHOICES", "UB_DISTRICT_CHOICES", "COMPANY_ACTIVITY_DIRECTION_CHOICES",
    "RESPONSIBLE_ROLE_CHOICES", "ENGINEER_SPECIALTY_CHOICES",
    "normalize_search_text", "SearchNormalizedMixin",
}

# Names that stay in apps.registry.models
REGISTRY_NAMES = {"MessageLog", "SiteConfig"}


def split_names(names_str):
    """Parse comma-separated import names, handling 'as' aliases."""
    items = []
    for n in names_str.split(","):
        n = n.strip().rstrip(",")
        if n:
            items.append(n)
    return items


def get_base_name(item):
    """Get the imported name (left of 'as' if present)."""
    return item.split(" as ")[0].strip()


for path in FILES:
    if not os.path.exists(path):
        print(f"SKIP (not found): {path}")
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    def process_import(names_str, is_multiline=False):
        items = split_names(names_str)
        core_items = []
        registry_items = []
        for item in items:
            base = get_base_name(item)
            if base in CORE_NAMES:
                core_items.append(item)
            else:
                registry_items.append(item)

        lines = []
        if registry_items:
            if is_multiline:
                lines.append("from .models import (\n    " + ",\n    ".join(registry_items) + ",\n)")
            else:
                lines.append("from .models import " + ", ".join(registry_items))
        if core_items:
            if is_multiline:
                lines.append("from apps.core.models import (\n    " + ",\n    ".join(core_items) + ",\n)")
            else:
                lines.append("from apps.core.models import " + ", ".join(core_items))
        return "\n".join(lines)

    # Multi-line: from .models import (\n  ...\n)
    def repl_multi(m):
        return process_import(m.group(1), is_multiline=True)

    content = re.sub(
        r"from \.models import \(([^)]+)\)",
        repl_multi,
        content,
    )

    # Single-line: from .models import A, B, C
    def repl_single(m):
        return process_import(m.group(1), is_multiline=False)

    content = re.sub(
        r"from \.models import ([^\n\(]+)",
        repl_single,
        content,
    )

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"UPDATED: {path}")
    else:
        print(f"NO CHANGE: {path}")

print("Done.")