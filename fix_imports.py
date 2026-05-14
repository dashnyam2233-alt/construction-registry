import os
import re

FILES = [
    r"apps\registry\admin.py",
    r"apps\registry\forms.py",
    r"apps\registry\views.py",
    r"apps\registry\resources.py",
]

# Replacements: (pattern, replacement)
REPLACEMENTS = [
    # "from .models import ... UserCompanyProfile ..." -> remove UserCompanyProfile, add import line
    # We'll handle by simple string replace + add new import at top
]

NEW_IMPORT = "from apps.accounts.models import AdminGroup, UserCompanyProfile\n"

for path in FILES:
    if not os.path.exists(path):
        print(f"SKIP (not found): {path}")
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Remove UserCompanyProfile and AdminGroup from existing .models imports
    def clean_models_import(match):
        names = match.group(1)
        items = [n.strip() for n in names.split(",")]
        items = [n for n in items if n and n not in ("UserCompanyProfile", "AdminGroup")]
        if not items:
            return ""
        return f"from .models import {', '.join(items)}"

    # single-line: from .models import A, B, C
    content = re.sub(
        r"from \.models import ([^\n\(]+)",
        clean_models_import,
        content,
    )

    # multi-line: from .models import (\n    A,\n    B,\n)
    def clean_multiline(match):
        names = match.group(1)
        items = [n.strip().rstrip(",") for n in names.split("\n")]
        items = [n for n in items if n and n not in ("UserCompanyProfile", "AdminGroup")]
        if not items:
            return ""
        return "from .models import (\n    " + ",\n    ".join(items) + ",\n)"

    content = re.sub(
        r"from \.models import \(([^)]+)\)",
        clean_multiline,
        content,
    )

    # Add new import after the last "from" or "import" line at top
    if "from apps.accounts.models import" not in content:
        lines = content.split("\n")
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith("from ") or line.startswith("import "):
                insert_idx = i + 1
        lines.insert(insert_idx, NEW_IMPORT.rstrip())
        content = "\n".join(lines)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"UPDATED: {path}")
    else:
        print(f"NO CHANGE: {path}")

print("Done.")