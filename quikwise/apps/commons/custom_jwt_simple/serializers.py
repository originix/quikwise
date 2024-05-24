from apps.commons.custom_responses import CustomResponse
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class TokenObtainPairCustomSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = CustomResponse()

        token = super(TokenObtainPairSerializer, self).validate(attrs)
        refresh = self.get_token(self.user)
        token['refresh'] = str(refresh)
        token['access'] = str(refresh.access_token)

        return data.response_jwt_custom_success(token)


class TokenRefreshCustomSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        data = CustomResponse()
        refresh = RefreshToken(attrs['refresh'])
        token = {'access': str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()

            token['refresh'] = str(refresh)

        return data.response_jwt_custom_success(token)


class TokenVerifySerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, attrs):
        data = CustomResponse()
        UntypedToken(attrs['token'])

        return data.response_jwt_custom_success({})
