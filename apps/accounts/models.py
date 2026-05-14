from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models

from apps.registry.models import (
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