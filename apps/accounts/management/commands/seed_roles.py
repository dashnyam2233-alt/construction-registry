from django.core.management.base import BaseCommand

from apps.accounts.models import Role


ROLES = [
    (Role.Code.ADMIN_FULL, "Бүрэн админ", "Системийн бүх эрх. Бүх компани, бүх ажилтан."),
    (Role.Code.COMPANY_ADMIN, "Компанийн админ", "Тухайн компанийн админ. Өөрийн компанийн бүх мэдээллийг засна."),
    (Role.Code.COMPANY_OPERATOR, "Компанийн оператор", "Зөвхөн өөрийн компанийн ажилтан, бригад нэмж засна."),
    (Role.Code.BRIGADE_LEADER, "Бригадын ахлагч", "Зөвхөн өөрийн бригадын гишүүдийг харж засна."),
    (Role.Code.VIEWER, "Зөвхөн харах", "Зөвхөн харах эрх. Засах боломжгүй."),
]


class Command(BaseCommand):
    help = "Үндсэн RBAC үүргүүдийг үүсгэнэ"

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0
        for code, name, description in ROLES:
            obj, created = Role.objects.get_or_create(
                code=code,
                defaults={"name": name, "description": description, "is_active": True},
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"  + {code}: {name}"))
            else:
                # Update name/description if changed
                changed = False
                if obj.name != name:
                    obj.name = name
                    changed = True
                if obj.description != description:
                    obj.description = description
                    changed = True
                if changed:
                    obj.save()
                    updated_count += 1
                    self.stdout.write(self.style.WARNING(f"  ~ {code}: updated"))
                else:
                    self.stdout.write(f"  = {code}: already exists")

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. Created: {created_count}, Updated: {updated_count}, Total roles: {Role.objects.count()}"
        ))