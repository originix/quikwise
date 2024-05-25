from apps.commons.custom_jwt_simple.serializers import TokenObtainPairCustomSerializer
from apps.commons.custom_jwt_simple.serializers import TokenRefreshCustomSerializer
from apps.commons.custom_jwt_simple.serializers import TokenVerifySerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class TokenCustomViewBase(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = None

    www_authenticate_realm = 'api'

    def get_authenticate_header(self, request):
        return '{0} realm="{1}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return serializer.validated_data


class TokenObtainPairCustomView(TokenCustomViewBase):
    serializer_class = TokenObtainPairCustomSerializer


class TokenRefreshCustomView(TokenCustomViewBase):
    serializer_class = TokenRefreshCustomSerializer


class TokenVerifyCustomView(TokenCustomViewBase):
    serializer_class = TokenVerifySerializer
