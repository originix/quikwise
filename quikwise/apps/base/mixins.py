from apps.base.response import Response
from rest_framework.mixins import ListModelMixin as BaseListModelMixin
from rest_framework.mixins import CreateModelMixin as BaseCreateModelMixin
from rest_framework.mixins import RetrieveModelMixin as BaseRetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin as BaseUpdateModelMixin
from rest_framework.mixins import DestroyModelMixin as BaseDestroyModelMixin
from rest_framework import status


class ListModelMixin(BaseListModelMixin):

    def list(self, request, *args, **kwargs):
        response = super(ListModelMixin, self).list(request, *args, **kwargs)

        if self.pagination_class is not None:
            return response

        return Response(data=response.data, status=status.HTTP_200_OK)


class CreateModelMixin(BaseCreateModelMixin):

    def create(self, request, *args, **kwargs):
        response = super(CreateModelMixin, self).create(request, *args, **kwargs)

        return Response(data=response.data, status=status.HTTP_201_CREATED)


class RetrieveModelMixin(BaseRetrieveModelMixin):

    def retrieve(self, request, *args, **kwargs):
        response = super(RetrieveModelMixin, self).retrieve(request, *args, **kwargs)

        return Response(response.data)


class UpdateModelMixin(BaseUpdateModelMixin):

    def update(self, request, *args, **kwargs):
        response = super(UpdateModelMixin, self).update(request, *args, **kwargs)

        return Response(data=response.data, status=status.HTTP_200_OK)


class DestroyModelMixin(BaseDestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        response = super(DestroyModelMixin, self).destroy(request, *args, **kwargs)

        return Response(data=response.data, status=status.HTTP_204_NO_CONTENT)