from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models

from apps.core.models import (
    SearchNormalizedMixin,
    Company,
)


class AdminGroup(Group):
    class Meta:
        proxy = True
        app_label = "auth"
        verbose_name = "Админ"
        verbose_name_plural = "Админууд"


class UserCompanyProfile(SearchNormalizedMixin, models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="company_profile",
        verbose_name="Хэрэглэгч",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name="user_profiles",
        verbose_name="Харьяалах компани",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Хэрэглэгчийн компани"
        verbose_name_plural = "Хэрэглэгчийн компаниуд"
        db_table = "registry_usercompanyprofile"

    def __str__(self):
        u = getattr(self.user, "username", None) or str(self.user)
        c = str(self.company) if self.company else "-"
        return f"{u} -> {c}"

    def get_search_source_text(self):
        u_username = getattr(self.user, "username", "") or ""
        u_email = getattr(self.user, "email", "") or ""
        c_name = getattr(self.company, "name", "") if self.company_id else ""
        c_reg = getattr(self.company, "register_no", "") if self.company_id else ""
        return " ".join([u_username, u_email, c_name or "", c_reg or ""])


class Role(models.Model):
    """RBAC үүрэг — Admin, Operator, Viewer, Brigade Leader гэх мэт"""

    class Code(models.TextChoices):
        ADMIN_FULL = "ADMIN_FULL", "Бүрэн админ"
        COMPANY_ADMIN = "COMPANY_ADMIN", "Компанийн админ"
        COMPANY_OPERATOR = "COMPANY_OPERATOR", "Компанийн оператор"
        BRIGADE_LEADER = "BRIGADE_LEADER", "Бригадын ахлагч"
        VIEWER = "VIEWER", "Зөвхөн харах"

    code = models.CharField("Кодлол", max_length=32, choices=Code.choices, unique=True)
    name = models.CharField("Нэр", max_length=100)
    description = models.TextField("Тайлбар", blank=True, default="")
    is_active = models.BooleanField("Идэвхтэй", default=True)
    created_at = models.DateTimeField("Үүссэн огноо", auto_now_add=True)

    class Meta:
        verbose_name = "Үүрэг"
        verbose_name_plural = "Үүргүүд"
        ordering = ("code",)

    def __str__(self):
        return self.name or self.get_code_display()


class UserRole(models.Model):
    """Хэрэглэгч ↔ Үүрэг холбоо (компанийн scope-той)"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_roles",
        verbose_name="Хэрэглэгч",
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        related_name="user_roles",
        verbose_name="Үүрэг",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="user_roles",
        verbose_name="Компанийн scope (хоосон = бүх компани)",
        null=True,
        blank=True,
    )
    granted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="granted_roles",
        verbose_name="Олгосон хэрэглэгч",
    )
    granted_at = models.DateTimeField("Олгосон огноо", auto_now_add=True)
    is_active = models.BooleanField("Идэвхтэй", default=True)

    class Meta:
        verbose_name = "Хэрэглэгчийн үүрэг"
        verbose_name_plural = "Хэрэглэгчийн үүргүүд"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "role", "company"],
                name="uniq_user_role_company",
            ),
        ]
        ordering = ("-granted_at",)

    def __str__(self):
        u = getattr(self.user, "username", str(self.user))
        c = f" @ {self.company}" if self.company else " (бүх)"
        return f"{u} — {self.role}{c}"