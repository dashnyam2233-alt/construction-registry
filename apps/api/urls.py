from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CompanyViewSet, WorkerViewSet, BrigadeViewSet, BrigadeMemberViewSet,
    FamilyMemberViewSet, GovernmentOrganizationViewSet, NonGovernmentOrganizationViewSet,
    PublicPostViewSet, BannerViewSet, HeroBannerViewSet, SliderAdViewSet,
    SubBannerViewSet, MessageLogViewSet,
)

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="company")
router.register(r"workers", WorkerViewSet, basename="worker")
router.register(r"brigades", BrigadeViewSet, basename="brigade")
router.register(r"brigade-members", BrigadeMemberViewSet, basename="brigademember")
router.register(r"family-members", FamilyMemberViewSet, basename="familymember")
router.register(r"government-orgs", GovernmentOrganizationViewSet, basename="govorg")
router.register(r"non-government-orgs", NonGovernmentOrganizationViewSet, basename="nongovorg")
router.register(r"posts", PublicPostViewSet, basename="post")
router.register(r"banners", BannerViewSet, basename="banner")
router.register(r"hero-banners", HeroBannerViewSet, basename="herobanner")
router.register(r"slider-ads", SliderAdViewSet, basename="sliderad")
router.register(r"sub-banners", SubBannerViewSet, basename="subbanner")
router.register(r"messages", MessageLogViewSet, basename="message")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
]