from .models import User
from .permissions import UserPermission
from .serializers import UserSerializerForm
from .serializers import UserSerializerDetail
from apps.base.viewsets import CRUDViewSetMixin


class UserViewSet(CRUDViewSetMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializerForm
    serializer_detail_class = UserSerializerDetail
    permission_classes = (UserPermission, )
