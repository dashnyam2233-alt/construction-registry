from import_export import resources

from .models import (
    GovernmentOrganization,
    NonGovernmentOrganization,
    Company,
    Worker,
    FamilyMember,
    AdminGroup,
    Brigade,
    BrigadeMember,
)


class GovernmentOrganizationResource(resources.ModelResource):
    class Meta:
        model = GovernmentOrganization


class NonGovernmentOrganizationResource(resources.ModelResource):
    class Meta:
        model = NonGovernmentOrganization


class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company


class WorkerResource(resources.ModelResource):
    class Meta:
        model = Worker


class FamilyMemberResource(resources.ModelResource):
    class Meta:
        model = FamilyMember


class AdminGroupResource(resources.ModelResource):
    class Meta:
        model = AdminGroup


class BrigadeResource(resources.ModelResource):
    class Meta:
        model = Brigade


class BrigadeMemberResource(resources.ModelResource):
    class Meta:
        model = BrigadeMember
