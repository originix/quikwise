from apps.users.viewsets import UserViewSet
from apps.commons.custom_jwt_simple.views import TokenObtainPairCustomView
from apps.commons.custom_jwt_simple.views import TokenRefreshCustomView
from apps.commons.custom_jwt_simple.views import TokenVerifyCustomView
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Open API', url='/')

app_name = 'api'
urlpatterns = [
    path('doc/', schema_view),
    path('token/', TokenObtainPairCustomView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshCustomView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyCustomView.as_view(), name='token_verify'),
]
router = DefaultRouter()

# user module
router.register(r'users', UserViewSet, basename="accounts")


urlpatterns += router.urls
