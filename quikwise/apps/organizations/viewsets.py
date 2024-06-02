from apps.base.viewsets import CRUDViewSetMixin
from apps.memberships.abstracts import MembershipStatus
from apps.organizations.models import Organization
from apps.organizations.permissions import OrganizationPermission
from apps.organizations.serializers import OrganizationSerializer


class OrganizationViewSet(CRUDViewSetMixin):
    serializer_class = OrganizationSerializer
    serializer_detail_class = OrganizationSerializer
    permission_classes = (OrganizationPermission, )
    pagination_class = None
    lookup_field = 'name'

    def get_queryset(self):
        queryset = Organization.objects.filter(members=self.request.user, membership__status=MembershipStatus.JOINED)

        return queryset