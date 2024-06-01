from apps.base import mixins
from rest_framework import viewsets
from rest_framework_extensions.mixins import DetailSerializerMixin



class ResponseModelViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    pass

class CRUDViewSetMixin(DetailSerializerMixin, ResponseModelViewSet):
    # serializer_class = UserSerializer
    # serializer_detail_class = UserDetailSerializer
    # queryset = User.objects.all()
    # queryset_detail = queryset.prefetch_related('groups__permissions')
    pass

