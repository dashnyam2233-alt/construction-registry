from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Username талбарт:
    - email бичсэн бол email-ээр нь хэрэглэгч олж authenticate хийнэ
    - эсвэл username бичсэн бол username-ээр authenticate хийнэ

    Анхаарах:
    - DB дээр давхардсан (case-insensitive) username/email байж болох тул get() хэрэглэхгүй.
    - filter().first() ашиглаж 500 унагахгүй болгов.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        if not username or password is None:
            return None

        login_value = str(username).strip()
        if not login_value:
            return None

        is_email = "@" in login_value

        if is_email:
            qs = UserModel._default_manager.filter(email__iexact=login_value).order_by("id")
        else:
            qs = UserModel._default_manager.filter(username__iexact=login_value).order_by("id")

        # Давхардсан байж болно → эхнийхийг авна (crash хийхгүй)
        user = qs.first()
        if user is None:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None
