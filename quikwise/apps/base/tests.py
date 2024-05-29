from apps.base.decorators import check_in_attributes


class TestSerializerMixin:
    """
        Add test serializer
    """
    expected_fields = None
    serializer_class = None

    @check_in_attributes(["expected_fields", "serializer_class", "instance"])
    def test_contains_expected_fields(self):
        serializer = self.serializer_class(instance=self.instance)
        data = serializer.data

        self.assertEqual(set(data.keys()), set(self.expected_fields))


class TestModelMixin:
    """
        Add default test model
    """
    model = None
    fields = None
    factory_class = None

    def _get_attributes(self):
        attributes = {}
        simple = self.factory_class.build()

        for field in self.fields:
            attributes.update({field: getattr(simple, field)})

        return attributes

    @check_in_attributes(["factory_class", "fields"])
    def test_create_model(self):
        attributes = self._get_attributes()
        instance = self.factory_class.create(**attributes)

        for k, v in attributes.items():
            self.assertEqual(getattr(instance, k), v)

    @check_in_attributes(["factory_class", "fields"])
    def test_update_model(self):
        attributes = self._get_attributes()
        instance = self.factory_class()

        for k, v in attributes.items():
            self.assertNotEqual(getattr(instance, k), v)

        for k, v in attributes.items():
            setattr(instance, k, v)

        for k, v in attributes.items():
            self.assertEqual(getattr(instance, k), v)

    @check_in_attributes(["factory_class", "model"])
    def test_delete_model(self):
        self.factory_class.create()
        queryset = self.model.objects.all()

        self.assertEqual(1, queryset.count())

        queryset.delete()
        count = self.model.objects.all().count()

        self.assertEqual(count, 0)
