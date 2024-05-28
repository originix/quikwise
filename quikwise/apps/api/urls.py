from apps.auth.views import AuthLoginView
from apps.auth.views import TokenRefreshView
from apps.auth.views import TokenVerifyView
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

# user module
router.register(r'users', UserViewSet, basename="accounts")


urlpatterns += router.urls
