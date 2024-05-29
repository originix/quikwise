from apps.base.errors import ErrorCode
from apps.base.response import Response
from apps.base.serializers import CRUDSerializer
from apps.users.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


class AUthLoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):

        token = super(TokenObtainPairSerializer, self).validate(attrs)
        refresh = self.get_token(self.user)
        token['refresh_token'] = str(refresh)
        token['access_token'] = str(refresh.access_token)

        return Response(data=token)

class TokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        refresh_token = RefreshToken(attrs['refresh_token'])
        token = {'access_token': str(refresh_token.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh_token.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh_token.set_jti()
            refresh_token.set_exp()

            token['refresh_token'] = str(refresh_token)

        return Response(data=token)


class TokenVerifySerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, attrs):
        UntypedToken(attrs['token'])

        return Response(data={})


class RegisterSerializer(CRUDSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'name',
            'username',
            'email',
            'password',
            'confirm_password',
        ]
        extra_kwargs = {
            'email': {'required': True},
        }

    def validate_email(self, data):
        user_model = get_user_model()
        existing = user_model.objects.filter(email=data).exists()

        if existing:
            raise serializers.ValidationError(_("A User With That Email Already Exists."), ErrorCode.UNIQUE)

        return data

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({'confirm_password': _("Those passwords don't match.")}, ErrorCode.INVALID)

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')

        return super().create(validated_data)

    def post_create(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()