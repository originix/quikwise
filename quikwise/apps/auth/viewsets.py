from .serializers import RegisterSerializer
from apps.base.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet


class RegisterViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = ([])
