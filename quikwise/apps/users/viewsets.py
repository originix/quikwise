from .models import User
from .permissions import UserPermission
from .serializers import UserSerializerForm
from .serializers import UserSerializerDetail
from apps.commons.viewsets import CRUDViewsetMixin


class UserViewSet(CRUDViewsetMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializerForm
    serializer_detail_class = UserSerializerDetail
    permission_classes = (UserPermission, )
