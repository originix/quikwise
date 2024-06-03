from apps.base.response import Response
from apps.base.viewsets import CRUDViewSetMixin
from apps.memberships.abstracts import MembershipStatus
from apps.organizations.models import Organization
from apps.organizations.permissions import OrganizationPermission
from apps.organizations.serializers import OrganizationSerializer
from apps.organizations.serializers import OrganizationCheckNameSerializer
from rest_framework.decorators import action


class OrganizationViewSet(CRUDViewSetMixin):
    serializer_class = OrganizationSerializer
    serializer_detail_class = OrganizationSerializer
    permission_classes = (OrganizationPermission, )
    pagination_class = None
    lookup_field = 'name'

    def get_queryset(self):
        queryset = Organization.objects.filter(members=self.request.user, membership__status=MembershipStatus.JOINED)

        return queryset

    @action(detail=False, url_path='actions/check-name', methods=['post'], serializer_class=OrganizationCheckNameSerializer)
    def check_name(self, request):
        serializer = OrganizationCheckNameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        return Response(data=validated_data)
