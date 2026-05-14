# registry/admin_messaging_view.py
from django.template.response import TemplateResponse
from django.contrib import messages as django_messages
from .models import (
    Company, Worker, FamilyMember, Brigade, BrigadeMember, MessageLog,
    CITY_CHOICES, COMPANY_ACTIVITY_DIRECTION_CHOICES, UB_DISTRICT_CHOICES
)
from .messaging import send_message, CHANNEL_LABELS

ACTIVITY_TYPE_CHOICES = [
    ("design",       "Зураг төсөл"),
    ("construction", "Барилга угсралт"),
    ("supply",       "Материал нийлүүлэлт"),
    ("consulting",   "Зөвлөх үйлчилгээ"),
    ("other",        "Бусад"),
]


def messaging_admin_view(request):
    def gp(key): return request.GET.get(key, "") or ""

    filter_city      = gp("filter_city")
    filter_district  = gp("filter_district")
    filter_direction = gp("filter_direction")
    filter_act_type  = gp("filter_act_type")
    filter_search    = gp("filter_search")
    filter_has_email = gp("filter_has_email")
    filter_has_phone = gp("filter_has_phone")

    # ── Компани ──
    cqs = Company.objects.all().order_by("name")
    if filter_city:       cqs = cqs.filter(city=filter_city)
    if filter_district:   cqs = cqs.filter(district=filter_district)
    if filter_direction:  cqs = cqs.filter(activity_direction=filter_direction)
    if filter_act_type:   cqs = cqs.filter(activity_type=filter_act_type)
    if filter_search:     cqs = cqs.filter(name__icontains=filter_search)
    if filter_has_email:  cqs = cqs.exclude(email="")
    if filter_has_phone:  cqs = cqs.exclude(phone="")
    all_companies = list(cqs)

    # ── Ажиллагсад ──
    wqs = Worker.objects.all().select_related("company").order_by("last_name", "first_name")
    if filter_city:       wqs = wqs.filter(company__city=filter_city)
    if filter_district:   wqs = wqs.filter(company__district=filter_district)
    if filter_direction:  wqs = wqs.filter(company__activity_direction=filter_direction)
    if filter_act_type:   wqs = wqs.filter(company__activity_type=filter_act_type)
    if filter_search:
        from django.db.models import Q
        wqs = wqs.filter(
            Q(company__name__icontains=filter_search) |
            Q(first_name__icontains=filter_search) |
            Q(last_name__icontains=filter_search)
        )
    if filter_has_email:  wqs = wqs.exclude(email="")
    if filter_has_phone:  wqs = wqs.exclude(phone="")
    all_workers = list(wqs.distinct())

    # ── Ажилтны хамаарал ──
    fqs = FamilyMember.objects.all().select_related("worker__company").order_by("last_name", "first_name")
    if filter_city:      fqs = fqs.filter(worker__company__city=filter_city)
    if filter_direction: fqs = fqs.filter(worker__company__activity_direction=filter_direction)
    if filter_search:
        from django.db.models import Q
        fqs = fqs.filter(
            Q(first_name__icontains=filter_search) |
            Q(last_name__icontains=filter_search) |
            Q(worker__company__name__icontains=filter_search)
        )
    if filter_has_email: fqs = fqs.exclude(email="")
    if filter_has_phone: fqs = fqs.exclude(phone="")
    all_family = list(fqs.distinct())

    # ── Бригадууд ──
    bqs = Brigade.objects.all().prefetch_related("companies").order_by("name")
    if filter_search:
        bqs = bqs.filter(name__icontains=filter_search)
    all_brigades = list(bqs)

    # ── Бригадын гишүүд ──
    bmqs = BrigadeMember.objects.all().select_related("worker", "brigade").order_by("worker__last_name")
    if filter_search:
        from django.db.models import Q
        bmqs = bmqs.filter(
            Q(worker__first_name__icontains=filter_search) |
            Q(worker__last_name__icontains=filter_search) |
            Q(brigade__name__icontains=filter_search)
        )
    if filter_has_phone: bmqs = bmqs.exclude(worker__phone="")
    all_brigade_members = list(bmqs.distinct())

    logs = MessageLog.objects.select_related("sent_by").order_by("-created_at")[:30]

    results = []
    success_count = 0
    fail_count = 0

    if request.method == "POST" and request.POST.get("action") == "send":
        channel        = request.POST.get("channel", "email")
        subject        = (request.POST.get("subject") or "").strip()
        body           = (request.POST.get("body") or "").strip()
        send_all       = request.POST.get("send_all") == "1"
        company_ids    = request.POST.getlist("company_ids")
        worker_ids     = request.POST.getlist("worker_ids")
        family_ids     = request.POST.getlist("family_ids")
        brigade_ids    = request.POST.getlist("brigade_ids")
        bm_ids         = request.POST.getlist("bm_ids")

        # Бүгдэд илгээх
        if send_all:
            company_ids  = list(Company.objects.values_list("id", flat=True))
            worker_ids   = list(Worker.objects.values_list("id", flat=True))
            family_ids   = list(FamilyMember.objects.values_list("id", flat=True))
            brigade_ids  = list(Brigade.objects.values_list("id", flat=True))
            bm_ids       = []

        if not body:
            django_messages.error(request, "Мессежийн агуулга хоосон байна.")
        elif not send_all and not any([company_ids, worker_ids, family_ids, brigade_ids, bm_ids]):
            django_messages.error(request, "Хүлээн авагч сонгоогүй байна.")
        else:
            recipients = _get_recipients(channel, company_ids, worker_ids, family_ids, brigade_ids, bm_ids)
            if not recipients:
                django_messages.warning(request, f"Сонгосон суваг ({CHANNEL_LABELS.get(channel)}) хаягтай хүлээн авагч олдсонгүй.")
            else:
                for r in recipients:
                    pb = body.replace("{name}", r["name"]).replace("{company}", r.get("company", r["name"]))
                    ps = subject.replace("{name}", r["name"]).replace("{company}", r.get("company", r["name"]))
                    result = send_message(channel, r["address"], ps, pb)
                    MessageLog.objects.create(
                        sent_by=request.user, channel=channel, target_type="selected",
                        recipient_name=r["name"], recipient_address=r["address"],
                        subject=ps, body=pb,
                        status="sent" if result["ok"] else "failed",
                        error_message=result.get("error", ""),
                    )
                    results.append({"ok": result["ok"], "name": r["name"], "address": r["address"], "error": result.get("error", "")})

                success_count = sum(1 for r in results if r["ok"])
                fail_count    = len(results) - success_count
                if success_count: django_messages.success(request, f"✅ {success_count} хүлээн авагчид амжилттай илгээлээ.")
                if fail_count:    django_messages.warning(request, f"⚠️ {fail_count} илгээлт амжилтгүй болсон.")

    district_choices = UB_DISTRICT_CHOICES if filter_city == "UB" else []

    from django.contrib import admin as _admin
    ctx = {
        **_admin.site.each_context(request),
        "title": "📨 Мессеж илгээх",
        "companies":          all_companies,
        "workers":            all_workers,
        "family_members":     all_family,
        "brigades":           all_brigades,
        "brigade_members":    all_brigade_members,
        "channels":           list(CHANNEL_LABELS.items()),
        "selected_channel":   request.POST.get("channel", "email"),
        "target":             request.POST.get("target_type", "companies"),
        "form_subject":       request.POST.get("subject", ""),
        "form_body":          request.POST.get("body", ""),
        "results":            results,
        "success_count":      success_count,
        "fail_count":         fail_count,
        "logs":               logs,
        "filter_city":        filter_city,
        "filter_district":    filter_district,
        "filter_direction":   filter_direction,
        "filter_act_type":    filter_act_type,
        "filter_search":      filter_search,
        "filter_has_email":   filter_has_email,
        "filter_has_phone":   filter_has_phone,
        "city_choices":       CITY_CHOICES,
        "district_choices":   district_choices,
        "direction_choices":  COMPANY_ACTIVITY_DIRECTION_CHOICES,
        "act_type_choices":   ACTIVITY_TYPE_CHOICES,
        "opts":               MessageLog._meta,
        # Нийт тоо
        "total_companies":    Company.objects.count(),
        "total_workers":      Worker.objects.count(),
        "total_family":       FamilyMember.objects.count(),
        "total_brigades":     Brigade.objects.count(),
        "total_bm":           BrigadeMember.objects.count(),
    }
    return TemplateResponse(request, "admin/registry/messaging.html", ctx)


def _get_recipients(channel, company_ids, worker_ids, family_ids, brigade_ids, bm_ids):
    recipients = []
    seen = set()

    def addr_co(c):
        if channel == "email":    return (c.email or "").strip()
        if channel == "sms":      return (c.phone or "").strip().replace(" ", "")
        if channel == "facebook": return (getattr(c, "facebook_url", "") or "").strip()
        return ""

    def addr_wk(w):
        if channel == "email":    return (w.email or "").strip()
        if channel == "sms":      return (w.phone or "").strip().replace(" ", "")
        if channel == "telegram": return (getattr(w, "telegram", "") or "").strip()
        if channel == "viber":    return (w.viber or "").strip()
        if channel == "facebook": return (w.facebook_url or "").strip()
        return ""

    def addr_fm(f):
        if channel == "email": return (f.email or "").strip()
        if channel == "sms":   return (f.phone or "").strip().replace(" ", "")
        if channel == "viber": return (getattr(f, "viber", "") or "").strip()
        return ""

    def add(name, addr, company=""):
        if addr and addr.lower() not in seen:
            seen.add(addr.lower())
            recipients.append({"name": name, "address": addr, "company": company})

    if company_ids:
        for c in Company.objects.filter(id__in=company_ids):
            add(c.name, addr_co(c))

    if worker_ids:
        for w in Worker.objects.filter(id__in=worker_ids).select_related("company"):
            add(str(w), addr_wk(w), str(w.company) if w.company else "")

    if family_ids:
        for f in FamilyMember.objects.filter(id__in=family_ids).select_related("worker__company"):
            name = f"{f.last_name} {f.first_name}".strip() or str(f)
            add(name, addr_fm(f), str(f.worker.company) if f.worker and f.worker.company else "")

    if brigade_ids:
        for b in Brigade.objects.filter(id__in=brigade_ids).prefetch_related("members__worker").select_related("leader_worker"):
            if b.leader_worker:
                add(str(b.leader_worker), addr_wk(b.leader_worker))
            for m in b.members.all():
                add(str(m.worker), addr_wk(m.worker))

    if bm_ids:
        for bm in BrigadeMember.objects.filter(id__in=bm_ids).select_related("worker", "brigade"):
            add(str(bm.worker), addr_wk(bm.worker))

    return recipients
