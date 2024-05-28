from apps.base.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework_extensions.mixins import DetailSerializerMixin


class ResponseModelViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        response = super(ResponseModelViewSet, self).create(request, *args, **kwargs)

        return Response(data=response.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        response = super(ResponseModelViewSet, self).retrieve(request, *args, **kwargs)

        return Response(response.data)

    def update(self, request, *args, **kwargs):
        response = super(ResponseModelViewSet, self).update(request, *args, **kwargs)

        return Response(data=response.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        response = super(ResponseModelViewSet, self).destroy(request, *args, **kwargs)

        return Response(data=response.data, status=status.HTTP_204_NO_CONTENT)


class CRUDViewSetMixin(DetailSerializerMixin, ResponseModelViewSet):
    # serializer_class = UserSerializer
    # serializer_detail_class = UserDetailSerializer
    # queryset = User.objects.all()
    # queryset_detail = queryset.prefetch_related('groups__permissions')
    pass

