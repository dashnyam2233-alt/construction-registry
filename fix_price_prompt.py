content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''        # DB-аас үнийн мэдээлэл татах
        from apps.public.models import MaterialPrice
        prices = MaterialPrice.objects.filter(is_active=True).order_by("category", "name")
        price_text = "\\n".join([
            f"- {p.name}: {p.price_min:,}₮-{p.price_max:,}₮ / {p.unit}"
            for p in prices
        ])'''

new = '''        # DB-аас үнийн мэдээлэл татах — ангиллаар дундаж үнэ
        from apps.public.models import MaterialPrice
        from django.db.models import Avg

        # Ангиллаар бүлэглэж дундаж үнэ авах
        key_prices = [
            # Материал
            ("mat_cement", "Цемент М400"),
            ("mat_sand", "Элс"),
            ("mat_brick", "Тоосго"),
            ("mat_rebar", "Арматур"),
            ("mat_wood", "Мод"),
            ("mat_roof", "Дээврийн материал"),
            ("mat_insulation", "Дулаалга"),
            ("mat_window", "Цонх, хаалга"),
            ("mat_interior", "Дотор засал"),
            ("mat_plumbing", "Сантехник"),
            ("mat_electrical", "Цахилгаан"),
            # Ажилчид
            ("labor_general", "Барилгачин"),
            ("labor_special", "Мэргэжилтэн"),
            # Тээвэр
            ("transport_material", "Тээвэр"),
            # Машин
            ("machine_crane", "Кран"),
            ("machine_excavator", "Экскаватор"),
            ("machine_concrete", "Бетон зуурагч"),
        ]

        price_lines = []
        for cat, label in key_prices:
            items = MaterialPrice.objects.filter(is_active=True, category=cat)[:3]
            if items:
                for p in items:
                    price_lines.append(f"- {p.name}: {int(p.price_min):,}₮-{int(p.price_max):,}₮/{p.unit}")
            else:
                price_lines.append(f"- {label}: үнэ тодорхойгүй")

        price_text = "\\n".join(price_lines[:50])  # Хамгийн ихдээ 50 мөр'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")