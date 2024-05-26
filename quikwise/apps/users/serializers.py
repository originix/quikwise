from .models import User
from apps.commons.serializers import CRUDSerializer
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class UserSerializerForm(CRUDSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'password',
            'confirm_password',
            'email',
        ]

    def validate_username(self, data):
        UserModle = get_user_model()
        existing = UserModle.objects.filter(username=data).exists()
        if existing:
            raise serializers.ValidationError(_('This username exists in a system.'))
        return data

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError(_('Please enter a password and confirm it.'))

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError(_('Those passwords don\'t match.'))

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return super().create(validated_data)

    def post_create(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()


class UserSerializerDetail(CRUDSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'password',
            'email',
        ]
