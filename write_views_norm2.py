import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

views_path = r"apps\registry\views.py"

with open(views_path, "r", encoding="utf-8") as f:
    content = f.read()

# calculate_budget_norm функц байгаа эсэх шалгах
if "calculate_budget_norm" not in content:
    print("NOT FOUND - эхлээд write_views_norm.py ажиллуулна уу")
    exit()

# budget_calculator функцийн POST хэсгийг орлуулах
old = '''    if request.method == "POST":
        import anthropic
        
        building_type = request.POST.get("building_type", "")'''

new = '''    if request.method == "POST":
        building_type = request.POST.get("building_type", "")'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK1 - anthropic import хасагдлаа")
else:
    print("SKIP1 - аль хэдийн засагдсан байна")

# AI дуудах хэсгийг орлуулах — try блокоос эхлэн
old2 = '''        prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн.

ДААЛГАВАР: Зөвхөн материал, ажил, тээвэр, бусад зүйлсийн ЖАГСААЛТ гарга.
Тооцоо хийхгүй — зөвхөн нэр, нэгж, тоо хэмжээ, нэгж үнэ бич.
Python-д тооцоолно тул total, grand_total-г 0 гэж орхи."""'''

new2 = '''        # Python норм тооцоо — AI ашиглахгүй'''

if old2 in content:
    content = content.replace(old2, new2, 1)
    print("OK2 - prompt хасагдлаа")
else:
    print("SKIP2")

with open(views_path, "w", encoding="utf-8") as f:
    f.write(content)

print("\nОдоо budget_calculator функцийн try блокийг шалгана...")
# Функцийн байрлалыг олох
idx = content.find("def budget_calculator(request):")
if idx >= 0:
    snippet = content[idx:idx+500]
    print(snippet)