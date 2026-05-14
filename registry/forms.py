from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .models import Company, Worker, UserCompanyProfile


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Нууц үг", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Нууц үг (дахин)", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_password1(self):
        pw = self.cleaned_data.get("password1") or ""
        validate_password(pw)
        return pw

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            self.add_error("password2", "Нууц үг таарахгүй байна.")
        return cleaned


class CompanyRegisterForm(forms.ModelForm):
    class Meta:
        model = Company
        # ✅ админ дээр хамгийн түгээмэл талбарууд. Танайд байгаагаар нь тааруулсан.
        fields = [
            "name",
            "register_no",
            "activity_type",
            "activity_direction",
            "activity_sub_direction",
            "city",
            "district",
            "address",
            "phone",
            "email",
            "website",
            "note",
        ]


class WorkerRegisterForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            "company",
            "responsible_role",
            "engineer_specialty",
            "last_name",
            "parent_name",
            "first_name",
            "gender",
            "register_no",
            "birth_date",
            "birth_place_city",
            "birth_place_sub",
            "married",
            "profession",
            "phone",
            "email",
            "facebook_url",
            "instagram_url",
            "viber",
            "city",
            "district",
            "address",
            "note",
        ]


def ensure_user_company_profile(user, company):
    """
    ✅ Company бүртгүүлсэн хэрэглэгчийг компанитай нь холбож өгнө.
    """
    profile, _ = UserCompanyProfile.objects.get_or_create(user=user)
    profile.company = company
    profile.save()
    return profile
