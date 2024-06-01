from apps.base.errors import ErrorCode
from apps.base.serializers import CRUDSerializer
from apps.organizations.models import Organization
from apps.organizations.services import is_name_available
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class OrganizationSerializer(CRUDSerializer):

    class Meta:
        model = Organization
        fields = [
            'name'
        ]

    def validate_name(self, data):

        if not is_name_available(data, self.instance):
            raise serializers.ValidationError(_("A organization with that name already exists."), ErrorCode.UNIQUE)

        return data