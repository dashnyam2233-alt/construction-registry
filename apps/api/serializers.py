from rest_framework import serializers

from apps.core.models import (
    Company, Worker, Brigade, BrigadeMember,
    FamilyMember, GovernmentOrganization, NonGovernmentOrganization,
)
from apps.public.models import PublicPost, Banner, HeroBanner, SliderAd, SubBanner
from apps.messaging.models import MessageLog


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class WorkerSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source="company.name", read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Worker
        fields = "__all__"

    def get_full_name(self, obj):
        return " ".join(f"{obj.last_name} {obj.parent_name} {obj.first_name}".split()).strip()


class BrigadeSerializer(serializers.ModelSerializer):
    leader_name = serializers.SerializerMethodField()

    class Meta:
        model = Brigade
        fields = "__all__"

    def get_leader_name(self, obj):
        return str(obj.leader_worker) if obj.leader_worker_id else ""


class BrigadeMemberSerializer(serializers.ModelSerializer):
    worker_name = serializers.SerializerMethodField()

    class Meta:
        model = BrigadeMember
        fields = "__all__"

    def get_worker_name(self, obj):
        return str(obj.worker) if obj.worker_id else ""


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = "__all__"


class GovernmentOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentOrganization
        fields = "__all__"


class NonGovernmentOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonGovernmentOrganization
        fields = "__all__"


class PublicPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = PublicPost
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class HeroBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroBanner
        fields = "__all__"


class SliderAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderAd
        fields = "__all__"


class SubBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubBanner
        fields = "__all__"


class MessageLogSerializer(serializers.ModelSerializer):
    sent_by_name = serializers.CharField(source="sent_by.username", read_only=True)

    class Meta:
        model = MessageLog
        fields = "__all__"