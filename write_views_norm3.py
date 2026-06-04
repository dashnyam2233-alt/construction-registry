import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

views_path = r"apps\registry\views.py"

with open(views_path, "r", encoding="utf-8") as f:
    content = f.read()

# budget_calculator дотор try блокийг олох
idx = content.find("def budget_calculator(request):")
chunk = content[idx:idx+8000]

# try блокийн байрлал
try_idx = chunk.find("        try:")
if try_idx >= 0:
    print("TRY блок олдлоо:")
    print(repr(chunk[try_idx:try_idx+200]))
else:
    print("try блок олдсонгүй")
    # prompt хайх
    p_idx = chunk.find("prompt")
    print(f"prompt байрлал: {p_idx}")
    if p_idx >= 0:
        print(repr(chunk[p_idx:p_idx+200]))