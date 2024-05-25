from rest_framework import serializers
from collections import OrderedDict


class ChoicesField(serializers.Field):
    """Custom ChoiceField serializer field."""

    def __init__(self, choices, **kwargs):
        """init."""
        self._choices = OrderedDict(choices)
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        """Used while retrieving value for the field."""
        return self._choices[obj]

    def to_internal_value(self, data):
        """Used while storing value for the field."""
        for i in self._choices:
            if self._choices[i] == data:
                return i
        raise serializers.ValidationError("Acceptable values are {0}.".format(list(self._choices.values())))


class AutomaticFieldMixin(object):
    def automatic_fields(self, request, instance, validated_data):
        # control model
        # CASE CREATE: update set created_user
        # CASE UPDATE: update set updated_user and updated_at

        if instance is None:
            if request.user.is_authenticated:
                validated_data['created_user'] = request.user
            else:
                validated_data['created_user'] = validated_data['created_user']

        if request.user.is_authenticated:
            validated_data['updated_user'] = request.user
        else:
            validated_data['updated_user'] = validated_data['updated_user']


class CRUDSerializer(serializers.ModelSerializer):
    """
        CRUD(Create-Read-Update-Delete)

        CASE Create:
            step:
                - set field with validate data
                - pre-create
                - setup automatic fields
                - save instance
                - post-create
                - return instance

        CASE Update:
        step:
            - pre-update
            - update field with validate data
            - setup automatic fields
            - save instance
            - post-update
            - return instance

        Create and Update are override default function
        Delete and Read aren't override default function
    """

    def automatic_fields(self, request, instance, validated_data):
        pass

    def pre_create(self, validated_data):
        pass

    def post_create(self, instance, validated_data):
        pass

    def pre_update(self, instance, validated_data):
        pass

    def post_update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        # pre-create instance
        self.pre_create(validated_data)

        # Automatic assign data fields
        if self.context.get('request', None):
            self.automatic_fields(self.context['request'], None, validated_data)

        # Save
        instance = super().create(validated_data)

        # post-create instance
        self.post_create(instance, validated_data)

        return instance

    def update(self, instance, validated_data):
        # pre-update instance
        self.pre_update(instance, validated_data)

        # Automatic assing data fields
        if self.context.get('request', None):
            self.automatic_fields(self.context['request'], instance, validated_data)

        # Save
        instance = super().update(instance, validated_data)

        # post-update instance
        self.post_update(instance, validated_data)

        return instance


class CRUDSerializerMixin(AutomaticFieldMixin, CRUDSerializer):
    pass


class WriteRestrictedModelSerializer(serializers.ModelSerializer):
    """
        A ModelSerializer that takes an additional `writable_fields` argument that controls which fields can be written to.
    """

    def __init__(self, *args, **kwargs):
        super(WriteRestrictedModelSerializer, self).__init__(*args, **kwargs)

        # Any fields set to read_only.
        for field_name in self.fields.keys():
            self.fields[field_name].read_only = True


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
        A ModelSerializer that takes an additional `fields` argument that controls which fields should be displayed.
        http://www.tomchristie.com/rest-framework-2-docs/api-guide/serializers#modelserializer
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
