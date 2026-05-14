"""
RBAC декоратор/mixin-ууд.

Хэрэглээ (function-based view):
    from apps.accounts.decorators import require_role

    @require_role("ADMIN_FULL", "COMPANY_ADMIN")
    def my_view(request):
        ...

Хэрэглээ (class-based view):
    from apps.accounts.decorators import RoleRequiredMixin

    class MyView(RoleRequiredMixin, ListView):
        required_roles = ["ADMIN_FULL", "COMPANY_ADMIN"]
        ...
"""
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from .permissions import has_role, is_admin, user_companies


def require_role(*role_codes, raise_exception=True):
    """Декоратор: хэрэглэгч өгсөн үүргүүдийн ядаж нэгтэй байх ёстой.

    raise_exception=True бол 403 алдаа гаргана.
    raise_exception=False бол login руу чиглүүлнэ.
    """

    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped(request, *args, **kwargs):
            if has_role(request.user, *role_codes):
                return view_func(request, *args, **kwargs)
            if raise_exception:
                raise PermissionDenied("Энэ үйлдлийг гүйцэтгэх эрх алга.")
            return redirect("login")

        return _wrapped

    return decorator


def admin_required(view_func):
    """Зөвхөн бүрэн админ (superuser эсвэл ADMIN_FULL)"""

    @wraps(view_func)
    @login_required
    def _wrapped(request, *args, **kwargs):
        if is_admin(request.user):
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("Зөвхөн админ хандах боломжтой.")

    return _wrapped


class RoleRequiredMixin:
    """Class-based view-д зориулсан mixin.

    required_roles = ["ADMIN_FULL", "COMPANY_ADMIN"] гэх мэт жагсаалт.
    """

    required_roles = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        if self.required_roles and not has_role(request.user, *self.required_roles):
            raise PermissionDenied("Энэ үйлдлийг гүйцэтгэх эрх алга.")
        return super().dispatch(request, *args, **kwargs)


class CompanyScopedQuerysetMixin:
    """ListView/DetailView-д queryset-ийг хэрэглэгчийн компанийн scope-оор шүүнэ.

    company_field = "company"  # FK нэр
    """

    company_field = "company"

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_authenticated:
            return qs.none()
        companies = user_companies(user)
        if companies is None:  # admin → бүх
            return qs
        if not companies:
            return qs.none()
        return qs.filter(**{f"{self.company_field}__in": companies})