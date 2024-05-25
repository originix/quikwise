from .responses import ResponseModelViewSet
from rest_framework_extensions.mixins import DetailSerializerMixin


class CRUDViewsetMixin(DetailSerializerMixin, ResponseModelViewSet):
    # serializer_class = UserSerializer
    # serializer_detail_class = UserDetailSerializer
    # queryset = User.objects.all()
    # queryset_detail = queryset.prefetch_related('groups__permissions')
    pass
