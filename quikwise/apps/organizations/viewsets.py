from apps.base.viewsets import CRUDViewSetMixin
from apps.organizations.models import Organization
from apps.organizations.permissions import OrganizationPermission
from apps.organizations.serializers import OrganizationSerializer


class OrganizationViewSet(CRUDViewSetMixin):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    serializer_detail_class = OrganizationSerializer
    permission_classes = (OrganizationPermission, )
    lookup_field = 'name'