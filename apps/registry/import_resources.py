from __future__ import annotations

from typing import Any, Dict, Iterable, Tuple

from django.core.exceptions import ValidationError
from import_export import resources, fields
from import_export.widgets import Widget, ForeignKeyWidget

from apps.core.models import (
    Company,
    Worker,
    CITY_CHOICES,
    UB_DISTRICT_CHOICES,
    COMPANY_ACTIVITY_DIRECTION_CHOICES,
    RESPONSIBLE_ROLE_CHOICES,
    ENGINEER_SPECIALTY_CHOICES,
)


# =========================
# Helpers
# =========================
def _norm(v: Any) -> str:
    """
    Excel-ээс утга орж ирэхэд:
    - None -> ""
    - int/float -> боломжтой бол бүхэл тоо шиг бол ".0"-г арилгаж текст болгоно
    - бусад -> strip()
    """
    if v is None:
        return ""
    if isinstance(v, int):
        return str(v).strip()
    if isinstance(v, float):
        if v.is_integer():
            return str(int(v)).strip()
        return str(v).strip()
    return str(v).strip()


def _norm_low(v: Any) -> str:
    return _norm(v).lower()


def _build_choice_maps(choices: Iterable[Tuple[str, str]]) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Return:
      - by_code:   normalized(code)  -> code
      - by_label:  normalized(label) -> code
    """
    by_code: Dict[str, str] = {}
    by_label: Dict[str, str] = {}
    for code, label in choices:
        c = _norm_low(code)
        l = _norm_low(label)
        if c:
            by_code[c] = code
        if l:
            by_label[l] = code
    return by_code, by_label


CITY_BY_CODE, CITY_BY_LABEL = _build_choice_maps(CITY_CHOICES)
DIST_BY_CODE, DIST_BY_LABEL = _build_choice_maps(UB_DISTRICT_CHOICES)
ACTDIR_BY_CODE, ACTDIR_BY_LABEL = _build_choice_maps(COMPANY_ACTIVITY_DIRECTION_CHOICES)
ROLE_BY_CODE, ROLE_BY_LABEL = _build_choice_maps(RESPONSIBLE_ROLE_CHOICES)
ENG_BY_CODE, ENG_BY_LABEL = _build_choice_maps(ENGINEER_SPECIALTY_CHOICES)

# Worker.Gender, Worker.Profession: TextChoices
GENDER_BY_CODE = {"male": "male", "female": "female"}
GENDER_BY_LABEL = {"эр": "male", "эм": "female"}

PROF_BY_CODE = {
    "engineer": "engineer",
    "architect": "architect",
    "foreman": "foreman",
    "accountant": "accountant",
    "hr": "hr",
    "manager": "manager",
    "worker": "worker",
    "other": "other",
}
PROF_BY_LABEL = {
    "инженер": "engineer",
    "архитектор": "architect",
    "даамал": "foreman",
    "нягтлан": "accountant",
    "хүний нөөц": "hr",
    "менежер": "manager",
    "ажилчин": "worker",
    "бусад": "other",
}


def _resolve_choice(value: Any, by_code: Dict[str, str], by_label: Dict[str, str], *, field_label: str) -> str:
    raw = _norm(value)
    if raw == "":
        return ""
    key = _norm_low(raw)
    if key in by_code:
        return by_code[key]
    if key in by_label:
        return by_label[key]
    raise ValidationError(f"{field_label}: буруу утга '{raw}'")


class ChoiceOrLabelWidget(Widget):
    def __init__(self, *, by_code: Dict[str, str], by_label: Dict[str, str], field_label: str):
        self.by_code = by_code
        self.by_label = by_label
        self.field_label = field_label

    def clean(self, value, row=None, *args, **kwargs):
        return _resolve_choice(value, self.by_code, self.by_label, field_label=self.field_label)

    # ✅ FIX: django-import-export 4.4+ render() рүү export_fields зэрэг kwargs дамжуулдаг болсон
    def render(self, value, obj=None, **kwargs):
        return str(value or "")


class BooleanMnWidget(Widget):
    TRUE_SET = {"1", "true", "t", "yes", "y", "тийм", "tiim"}
    FALSE_SET = {"0", "false", "f", "no", "n", "үгүй", "ugui", "uguĭ", "үгуй"}

    def clean(self, value, row=None, *args, **kwargs):
        raw = _norm(value)
        if raw == "":
            return False
        k = _norm_low(raw)
        if k in self.TRUE_SET:
            return True
        if k in self.FALSE_SET:
            return False
        raise ValidationError(f"Гэрлэсэн эсэх: буруу утга '{raw}' (Тийм/Үгүй гэж бичнэ)")

    # ✅ SAFE: мөн адил kwargs-ыг залгиж байхаар
    def render(self, value, obj=None, **kwargs):
        return "Тийм" if value else "Үгүй"


class CompanyByRegisterNoWidget(ForeignKeyWidget):
    """
    FK resolve:
      - Компани РД/Бүртгэлийн № (эхний сонголт) → Company.register_no
      - эсвэл компанийн нэрээр олж болно

    ✅ Компанигүй ажилтан:
      - хоосон / '-' / 'байхгүй' / 'компанигүй' гэх мэт -> None (алдаа биш)
    """
    EMPTY_SET = {
        "", "-", "—", "_", "0",
        "null", "none", "n/a",
        "үгүй", "ugui", "uguĭ", "үгуй",
        "байхгүй", "baihgui", "bhgui",
        "компанигүй", "компани байхгүй",
    }

    def __init__(self):
        super().__init__(Company, "register_no")

    def clean(self, value, row=None, *args, **kwargs):
        reg = _norm(value)
        if _norm_low(reg) in self.EMPTY_SET:
            return None

        if reg:
            obj = Company.objects.filter(register_no=reg).first()
            if not obj:
                raise ValidationError(f"Компани (РД/Бүртгэлийн №) олдсонгүй: '{reg}'")
            return obj

        if row is not None:
            name = _norm(row.get("Компани нэр") or "")
            if name:
                obj = Company.objects.filter(name=name).first()
                if not obj:
                    raise ValidationError(f"Компани (нэр) олдсонгүй: '{name}'")
                return obj

        return None


def _company_activity_type_from_direction(direction_code: str) -> str:
    main = (direction_code or "").strip()
    if main == "DESIGN":
        return Company.ActivityType.DESIGN
    if main in ("CONSTRUCTION", "ELECTRICAL_INTERNAL", "PLUMBING_INTERNAL", "HVAC", "COMM_SYSTEM", "ENGINEERING_NETWORK", "EXTERNAL_ROAD"):
        return Company.ActivityType.CONSTRUCTION
    if main in ("MATERIAL_PRODUCTION", "MATERIAL_TRADE"):
        return Company.ActivityType.SUPPLY
    if main == "SUPERVISION":
        return Company.ActivityType.CONSULTING
    return Company.ActivityType.OTHER


def _coerce_text_fields(instance, field_names):
    """
    Import үед Excel-ээс int/float орж ирээд ".join()" дээр унахаас хамгаална.
    - None -> ""
    - int/float/бусад -> str(value).strip()
    """
    for fn in field_names:
        val = getattr(instance, fn, None)
        if val is None:
            setattr(instance, fn, "")
        else:
            setattr(instance, fn, str(val).strip())


# =========================
# Resources (Монгол баганын нэртэй)
# =========================
class CompanyResource(resources.ModelResource):
    name = fields.Field(attribute="name", column_name="Компани нэр")
    register_no = fields.Field(attribute="register_no", column_name="РД/Бүртгэлийн №")

    activity_direction = fields.Field(
        attribute="activity_direction",
        column_name="Үйл ажиллагааны чиглэл",
        widget=ChoiceOrLabelWidget(by_code=ACTDIR_BY_CODE, by_label=ACTDIR_BY_LABEL, field_label="Үйл ажиллагааны чиглэл"),
    )

    activity_sub_direction = fields.Field(attribute="activity_sub_direction", column_name="Дэд сонголт")

    city = fields.Field(
        attribute="city",
        column_name="Хот/Аймаг",
        widget=ChoiceOrLabelWidget(by_code=CITY_BY_CODE, by_label=CITY_BY_LABEL, field_label="Хот/Аймаг"),
    )

    district = fields.Field(
        attribute="district",
        column_name="Дүүрэг (УБ үед)",
        widget=ChoiceOrLabelWidget(by_code=DIST_BY_CODE, by_label=DIST_BY_LABEL, field_label="Дүүрэг (УБ үед)"),
    )

    address = fields.Field(attribute="address", column_name="Дэлгэрэнгүй хаяг")
    phone = fields.Field(attribute="phone", column_name="Утас")
    email = fields.Field(attribute="email", column_name="Имэйл")
    website = fields.Field(attribute="website", column_name="Вэб")
    note = fields.Field(attribute="note", column_name="Тайлбар")

    class Meta:
        model = Company
        import_id_fields = ("register_no",)
        skip_unchanged = True
        report_skipped = True
        fields = (
            "name",
            "register_no",
            "activity_direction",
            "activity_sub_direction",
            "city",
            "district",
            "address",
            "phone",
            "email",
            "website",
            "note",
        )
        export_order = fields

    def before_save_instance(self, instance, row, **kwargs):
        instance.activity_type = _company_activity_type_from_direction(instance.activity_direction)
        if (instance.city or "").strip() != "UB":
            instance.district = ""

        # ✅ Company дээрх текст талбаруудыг string болгож хамгаална
        _coerce_text_fields(instance, [
            "name",
            "register_no",
            "activity_sub_direction",
            "address",
            "phone",
            "email",
            "website",
            "note",
        ])


class WorkerResource(resources.ModelResource):
    last_name = fields.Field(attribute="last_name", column_name="Ургийн овог")
    parent_name = fields.Field(attribute="parent_name", column_name="Эцэг/эхийн нэр")
    first_name = fields.Field(attribute="first_name", column_name="Нэр")

    gender = fields.Field(
        attribute="gender",
        column_name="Хүйс",
        widget=ChoiceOrLabelWidget(by_code=GENDER_BY_CODE, by_label=GENDER_BY_LABEL, field_label="Хүйс"),
    )

    register_no = fields.Field(attribute="register_no", column_name="Регистр")
    birth_date = fields.Field(attribute="birth_date", column_name="Төрсөн огноо")

    birth_place_city = fields.Field(
        attribute="birth_place_city",
        column_name="Төрсөн газар - Аймаг/Хот",
        widget=ChoiceOrLabelWidget(by_code=CITY_BY_CODE, by_label=CITY_BY_LABEL, field_label="Төрсөн газар - Аймаг/Хот"),
    )
    birth_place_sub = fields.Field(attribute="birth_place_sub", column_name="Төрсөн газар - Сум/Дүүрэг")

    married = fields.Field(attribute="married", column_name="Гэрлэсэн эсэх", widget=BooleanMnWidget())

    profession = fields.Field(
        attribute="profession",
        column_name="Мэргэжил",
        widget=ChoiceOrLabelWidget(by_code=PROF_BY_CODE, by_label=PROF_BY_LABEL, field_label="Мэргэжил"),
    )

    company = fields.Field(
        attribute="company",
        column_name="Компани РД/Бүртгэлийн №",
        widget=CompanyByRegisterNoWidget(),
    )

    responsible_role = fields.Field(
        attribute="responsible_role",
        column_name="Хариуцсан ажил",
        widget=ChoiceOrLabelWidget(by_code=ROLE_BY_CODE, by_label=ROLE_BY_LABEL, field_label="Хариуцсан ажил"),
    )

    engineer_specialty = fields.Field(
        attribute="engineer_specialty",
        column_name="Инженерийн төрөл",
        widget=ChoiceOrLabelWidget(by_code=ENG_BY_CODE, by_label=ENG_BY_LABEL, field_label="Инженерийн төрөл"),
    )

    phone = fields.Field(attribute="phone", column_name="Утас")
    email = fields.Field(attribute="email", column_name="Имэйл")
    facebook_url = fields.Field(attribute="facebook_url", column_name="Facebook хаяг")
    instagram_url = fields.Field(attribute="instagram_url", column_name="Instagram хаяг")
    viber = fields.Field(attribute="viber", column_name="Viber хаяг/дугаар")

    city = fields.Field(
        attribute="city",
        column_name="Хот/Аймаг",
        widget=ChoiceOrLabelWidget(by_code=CITY_BY_CODE, by_label=CITY_BY_LABEL, field_label="Хот/Аймаг"),
    )

    district = fields.Field(
        attribute="district",
        column_name="Дүүрэг (УБ үед)",
        widget=ChoiceOrLabelWidget(by_code=DIST_BY_CODE, by_label=DIST_BY_LABEL, field_label="Дүүрэг (УБ үед)"),
    )

    address = fields.Field(attribute="address", column_name="Оршин суугаа газрын хаяг")
    note = fields.Field(attribute="note", column_name="Тайлбар")

    class Meta:
        model = Worker
        import_id_fields = ("register_no",)
        skip_unchanged = True
        report_skipped = True
        fields = (
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
            "company",
            "responsible_role",
            "engineer_specialty",
            "phone",
            "email",
            "facebook_url",
            "instagram_url",
            "viber",
            "city",
            "district",
            "address",
            "note",
        )
        export_order = fields

    def before_import_row(self, row, **kwargs):
        # Engineer сонгосон бол engineer_specialty шаардлагатай
        role_raw = _norm(row.get("Хариуцсан ажил"))
        try:
            role_code = _resolve_choice(role_raw, ROLE_BY_CODE, ROLE_BY_LABEL, field_label="Хариуцсан ажил")
        except ValidationError:
            role_code = ""
        if role_code == "ENGINEER":
            spec = _norm(row.get("Инженерийн төрөл"))
            if not spec:
                raise ValidationError("Инженер сонгосон тул 'Инженерийн төрөл' заавал байна.")

    def before_save_instance(self, instance, row, **kwargs):
        if (instance.city or "").strip() != "UB":
            instance.district = ""

        # ✅ хамгийн гол fix:
        # Excel-ээс int/float орж ирж болох бүх текст талбаруудыг string болгож өгнө.
        _coerce_text_fields(instance, [
            "last_name",
            "parent_name",
            "first_name",
            "register_no",
            "birth_place_sub",
            "phone",
            "email",
            "facebook_url",
            "instagram_url",
            "viber",
            "address",
            "note",
        ])
