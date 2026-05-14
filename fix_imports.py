import os
import re

FILES = [
    r"apps\registry\admin.py",
    r"apps\registry\admin_messaging_view.py",
    r"apps\registry\messaging.py",
]

MESSAGING_NAMES = {"MessageLog", "SiteConfig"}


def split_names(names_str):
    items = []
    for n in names_str.split(","):
        n = n.strip().rstrip(",")
        if n:
            items.append(n)
    return items


def get_base_name(item):
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
        messaging_items = []
        keep_items = []
        for item in items:
            base = get_base_name(item)
            if base in MESSAGING_NAMES:
                messaging_items.append(item)
            else:
                keep_items.append(item)

        lines = []
        if keep_items:
            if is_multiline:
                lines.append("from .models import (\n    " + ",\n    ".join(keep_items) + ",\n)")
            else:
                lines.append("from .models import " + ", ".join(keep_items))
        if messaging_items:
            if is_multiline:
                lines.append("from apps.messaging.models import (\n    " + ",\n    ".join(messaging_items) + ",\n)")
            else:
                lines.append("from apps.messaging.models import " + ", ".join(messaging_items))
        return "\n".join(lines)

    def repl_multi(m):
        return process_import(m.group(1), is_multiline=True)

    content = re.sub(r"from \.models import \(([^)]+)\)", repl_multi, content)

    def repl_single(m):
        return process_import(m.group(1), is_multiline=False)

    content = re.sub(r"from \.models import ([^\n\(]+)", repl_single, content)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"UPDATED: {path}")
    else:
        print(f"NO CHANGE: {path}")

print("Done.")