from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.postgres.search import TrigramSimilarity

from apps.core.models import (
    Company, Worker, Brigade, BrigadeMember,
    FamilyMember, GovernmentOrganization, NonGovernmentOrganization,
)
from apps.public.models import Banner, HeroBanner, SliderAd, SubBanner, PublicPost
from apps.messaging.models import MessageLog
from apps.api import serializers as S


class TrigramSearchMixin:
    trigram_fields = []

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get("q")
        if q and self.trigram_fields:
            sim = None
            for f in self.trigram_fields:
                s = TrigramSimilarity(f, q)
                sim = s if sim is None else sim + s
            qs = qs.annotate(similarity=sim).filter(similarity__gt=0.15).order_by("-similarity")
        return qs


class CompanyViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = S.CompanySerializer
    permission_classes = [IsAuthenticated]
    trigram_fields = ["name", "register_no"]


class WorkerViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = Worker.objects.select_related("company", "brigade").all()
    serializer_class = S.WorkerSerializer
    permission_classes = [IsAuthenticated]
    trigram_fields = ["last_name", "first_name", "register_no"]


class BrigadeViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = Brigade.objects.select_related("company", "leader").prefetch_related("members").all()
    serializer_class = S.BrigadeSerializer
    permission_classes = [IsAuthenticated]
    trigram_fields = ["name"]


class BrigadeMemberViewSet(viewsets.ModelViewSet):
    queryset = BrigadeMember.objects.select_related("brigade", "worker").all()
    serializer_class = S.BrigadeMemberSerializer
    permission_classes = [IsAuthenticated]


class FamilyMemberViewSet(viewsets.ModelViewSet):
    queryset = FamilyMember.objects.select_related("worker").all()
    serializer_class = S.FamilyMemberSerializer
    permission_classes = [IsAuthenticated]


class GovernmentOrganizationViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = GovernmentOrganization.objects.all()
    serializer_class = S.GovernmentOrganizationSerializer
    permission_classes = [IsAuthenticated]
    trigram_fields = ["name"]


class NonGovernmentOrganizationViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = NonGovernmentOrganization.objects.all()
    serializer_class = S.NonGovernmentOrganizationSerializer
    permission_classes = [IsAuthenticated]
    trigram_fields = ["name"]


class PublicPostViewSet(TrigramSearchMixin, viewsets.ModelViewSet):
    queryset = PublicPost.objects.select_related("author").all()
    serializer_class = S.PublicPostSerializer
    permission_classes = [IsAuthenticated]
    trigram_fields = ["title", "body"]


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = S.BannerSerializer
    permission_classes = [IsAuthenticated]


class HeroBannerViewSet(viewsets.ModelViewSet):
    queryset = HeroBanner.objects.all()
    serializer_class = S.HeroBannerSerializer
    permission_classes = [IsAuthenticated]


class SliderAdViewSet(viewsets.ModelViewSet):
    queryset = SliderAd.objects.all()
    serializer_class = S.SliderAdSerializer
    permission_classes = [IsAuthenticated]


class SubBannerViewSet(viewsets.ModelViewSet):
    queryset = SubBanner.objects.all()
    serializer_class = S.SubBannerSerializer
    permission_classes = [IsAuthenticated]


class MessageLogViewSet(viewsets.ModelViewSet):
    queryset = MessageLog.objects.select_related("sender").all()
    serializer_class = S.MessageLogSerializer
    permission_classes = [IsAuthenticated]