from apps.organizations.serializers import OrganizationSerializer
from apps.organizations.factories import OrganizationFactory
from rest_framework.test import APITestCase
from faker import Faker

fake = Faker()

class TestOrganizationSerializer(APITestCase):

    def test_serializing_object_user(self):
        organization = OrganizationFactory()

        serializer = OrganizationSerializer(organization)

        actual = serializer.data

        expected = {
            'name': organization.name,
        }

        self.assertEqual(expected, actual)

    def test_create_organization_success(self):

        data = {
            'name': fake.user_name()
        }

        serializer = OrganizationSerializer(data=data)
        is_valid = serializer.is_valid()
        organization = serializer.save()

        self.assertTrue(is_valid)
        self.assertEqual(data['name'], organization.name)

    def test_create_organization_name_invalid_fail(self):

        data = {
            'name': 'not a valid name',
        }

        serializer = OrganizationSerializer(data=data)
        is_valid = serializer.is_valid()
        errors = serializer.errors

        self.assertFalse(is_valid)
        self.assertEqual(['name'], [*errors])
        self.assertIn('Enter a valid "slug" consisting of letters, numbers, underscores or hyphens.', str(errors))

    def test_create_organization_name_existing_fail(self):
        name = fake.user_name()

        OrganizationFactory.create(name=name)

        data = {
            'name': name
        }

        serializer = OrganizationSerializer(data=data)
        is_valid = serializer.is_valid()
        errors = serializer.errors

        self.assertFalse(is_valid)
        self.assertEqual(['name'], [*errors])
        self.assertIn('organization with this name already exists.', str(errors))

    def test_update_organization_name_success(self):
        name = fake.user_name()

        organization = OrganizationFactory.create(name=name)

        data = {
            'name': 'quikwise'
        }

        serializer = OrganizationSerializer(organization, data=data)
        serializer.is_valid()
        serializer.save()

        self.assertEqual('quikwise', organization.name)

    def test_update_organization_with_self_name_success(self):
        name = fake.user_name()

        organization = OrganizationFactory.create(name=name)

        data = {
            'name': name
        }

        serializer = OrganizationSerializer(organization, data=data)
        serializer.is_valid()
        serializer.save()

        self.assertEqual(name, organization.name)

    def test_update_organization_other_name_existing_success(self):
        name = fake.user_name()
        other_name = fake.user_name()

        organization = OrganizationFactory.create(name=name)
        other_organization = OrganizationFactory.create(name=other_name)

        data = {
            'name': other_name
        }

        serializer = OrganizationSerializer(organization, data=data)
        is_valid = serializer.is_valid()
        errors = serializer.errors

        self.assertFalse(is_valid)
        self.assertEqual(['name'], [*errors])
        self.assertIn('organization with this name already exists.', str(errors))