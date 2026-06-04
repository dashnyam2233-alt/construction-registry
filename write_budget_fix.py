import os

views_path = r"apps\registry\views.py"

with open(views_path, "r", encoding="utf-8") as f:
    content = f.read()

# Хуучин budget_calculator функцийн prompt хэсгийг олж орлуулна
old_part = '''        prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн. Дараах барилгын төсвийг тооцоолж өгнө үү.'''

new_part = '''        prompt = f"""Та Монголын барилгын салбарын мэргэжилтэн.

ДААЛГАВАР: Зөвхөн материал, ажил, тээвэр, бусад зүйлсийн ЖАГСААЛТ гарга.
Тооцоо хийхгүй — зөвхөн нэр, нэгж, тоо хэмжээ, нэгж үнэ бич.
Python-д тооцоолно тул total, grand_total-г 0 гэж орхи.'''

if old_part in content:
    print("FOUND - орлуулж байна...")
    content = content.replace(old_part, new_part, 1)
    with open(views_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("DONE - views.py шинэчлэгдлээ")
else:
    print("NOT FOUND - текст таарахгүй байна")