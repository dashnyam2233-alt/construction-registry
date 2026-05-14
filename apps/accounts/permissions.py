"""
RBAC туслах функцууд.

Хэрэглээ:
    from apps.accounts.permissions import has_role, get_user_roles, user_companies

    if has_role(request.user, "ADMIN_FULL"):
        ...
"""
from .models import UserRole, Role


def get_user_roles(user):
    """Хэрэглэгчийн идэвхтэй бүх үүргийн code-уудыг буцаана"""
    if not user or not user.is_authenticated:
        return []
    return list(
        UserRole.objects.filter(user=user, is_active=True, role__is_active=True)
        .values_list("role__code", flat=True)
    )


def has_role(user, *role_codes):
    """Хэрэглэгч өгсөн үүргүүдийн ядаж нэгтэй эсэхийг шалгана"""
    if not user or not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    return UserRole.objects.filter(
        user=user,
        is_active=True,
        role__is_active=True,
        role__code__in=role_codes,
    ).exists()


def is_admin(user):
    """Бүрэн админ эсэхийг шалгана (superuser эсвэл ADMIN_FULL)"""
    if not user or not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    return has_role(user, Role.Code.ADMIN_FULL)


def user_companies(user):
    """Хэрэглэгчийн scope-той компаниудын ID жагсаалт.
    ADMIN_FULL бол None (бүх компани) буцаана."""
    if not user or not user.is_authenticated:
        return []
    if is_admin(user):
        return None  # бүх компани
    return list(
        UserRole.objects.filter(user=user, is_active=True, company__isnull=False)
        .values_list("company_id", flat=True)
        .distinct()
    )


def has_company_access(user, company):
    """Тухайн компанид хандах эрх байгаа эсэх"""
    if is_admin(user):
        return True
    companies = user_companies(user)
    if companies is None:
        return True
    return company.id in companies if hasattr(company, "id") else company in companies