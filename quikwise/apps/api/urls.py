from apps.auth.views import AuthLoginView
from apps.auth.views import TokenRefreshView
from apps.auth.views import TokenVerifyView
from apps.auth.viewsets import RegisterViewSet
from apps.organizations.viewsets import OrganizationViewSet
from apps.users.viewsets import UserViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter


app_name = 'api'
urlpatterns = [
    path('auth/login', AuthLoginView.as_view(), name='auth_login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='auth_token_refresh'),
    path('auth/verify/', TokenVerifyView.as_view(), name='auth_token_verify'),
]
router = DefaultRouter()

router.register(r'auth/register', RegisterViewSet, basename='register')

router.register(r'organizations', OrganizationViewSet, basename='organization')

# user module
router.register(r'users', UserViewSet, basename="accounts")


urlpatterns += router.urls
