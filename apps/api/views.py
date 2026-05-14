from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q, F
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.core.models import (
    Company, Worker, Brigade, BrigadeMember,
    FamilyMember, GovernmentOrganization, NonGovernmentOrganization,
)
from apps.public.models import PublicPost, Banner, HeroBanner, SliderAd, SubBanner
from apps.messaging.models import MessageLog
from apps.accounts.permissions import user_companies

from .serializers import (
    CompanySerializer, WorkerSerializer, BrigadeSerializer, BrigadeMemberSerializer,
    FamilyMemberSerializer, GovernmentOrganizationSerializer, NonGovernmentOrganizationSerializer,
    PublicPostSerializer, BannerSerializer, HeroBannerSerializer, SliderAdSerializer,
    SubBannerSerializer, MessageLogSerializer,
)


class CompanyScopedMixin:
    """Queryset-ийг хэрэглэгчийн компанийн scope-оор шүүнэ."""

    company_field = "company"

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_authenticated:
            return qs.none()
        companies = user_companies(user)
        if companies is None:
            return qs
        if not companies:
            return qs.none()
        if self.company_field == "self":
            return qs.filter(id__in=companies)
        return qs.filter(**{f"{self.company_field}__in": companies})


class TrigramSearchMixin:
    """?q=... параметрээр trigram хайлт хийнэ (typo даадаг)."""

    trigram_fields = ["search_normalized"]
    trigram_threshold = 0.15

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        q = self.request.query_params.get("q", "").strip()
        if not q or not self.trigram_fields:
            return qs

        # Build similarity expression: max similarity across fields
        first_field = self.trigram_fields[0]
        similarity = TrigramSimilarity(first_field, q)
        for f in self.trigram_fields[1:]:
            similarity = similarity + TrigramSimilarity(f, q)

        return (
            qs.annotate(similarity=similarity)
              .filter(similarity__gte=self.trigram_threshold)
              .order_by("-similarity")
        )


class CompanyViewSet(TrigramSearchMixin, CompanyScopedMixin, viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "register_no", "search_normalized"]
    ordering_fields = ["name", "id"]
    company_field = "self"
    trigram_fields = ["name", "register_no", "search_normalized"]


class WorkerViewSet(TrigramSearchMixin, CompanyScopedMixin, viewsets.ModelViewSet):
    queryset = Worker.objects.select_related("company").all()
    serializer_class = WorkerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["first_name", "last_name", "parent_name", "register_no", "search_normalized"]
    ordering_fields = ["first_name", "last_name", "id"]
    trigram_fields = ["first_name", "last_name", "parent_name", "search_normalized"]


class BrigadeViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = Brigade.objects.select_related("leader_worker").prefetch_related("companies", "members").all()
    serializer_class = BrigadeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "search_normalized"]
    trigram_fields = ["name", "search_normalized"]


class BrigadeMemberViewSet(viewsets.ModelViewSet):
    queryset = BrigadeMember.objects.select_related("brigade", "worker").all()
    serializer_class = BrigadeMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class FamilyMemberViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = FamilyMember.objects.select_related("worker").all()
    serializer_class = FamilyMemberSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["first_name", "last_name", "register_no", "search_normalized"]
    trigram_fields = ["first_name", "last_name", "search_normalized"]


class GovernmentOrganizationViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = GovernmentOrganization.objects.all()
    serializer_class = GovernmentOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "register_no", "search_normalized"]
    trigram_fields = ["name", "search_normalized"]


class NonGovernmentOrganizationViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = NonGovernmentOrganization.objects.all()
    serializer_class = NonGovernmentOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "register_no", "search_normalized"]
    trigram_fields = ["name", "search_normalized"]


class PublicPostViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = PublicPost.objects.select_related("author").filter(is_published=True)
    serializer_class = PublicPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "body"]
    ordering = ["-created_at"]
    trigram_fields = ["title", "body"]


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HeroBannerViewSet(viewsets.ModelViewSet):
    queryset = HeroBanner.objects.all()
    serializer_class = HeroBannerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SliderAdViewSet(viewsets.ModelViewSet):
    queryset = SliderAd.objects.all()
    serializer_class = SliderAdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubBannerViewSet(viewsets.ModelViewSet):
    queryset = SubBanner.objects.all()
    serializer_class = SubBannerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MessageLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MessageLog.objects.select_related("sent_by").all()
    serializer_class = MessageLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering = ["-created_at"]