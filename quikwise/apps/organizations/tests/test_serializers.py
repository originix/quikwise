from apps.organizations.serializers import OrganizationSerializer
from apps.organizations.factories import OrganizationFactory
from apps.users.factories import UserFactory
from rest_framework.test import APITestCase
from unittest.mock import patch
from unittest.mock  import MagicMock
from faker import Faker

fake = Faker()

class TestOrganizationSerializer(APITestCase):

    def setUp(self):
        user = UserFactory.create()

        self.request = MagicMock(user=user)

    def test_serializing_object_user(self):

        organization = OrganizationFactory()

        serializer = OrganizationSerializer(organization, context={'request': self.request})

        actual = serializer.data

        expected = {
            'name': organization.name,
        }

        self.assertEqual(expected, actual)

    @patch('apps.organizations.signals.organization_created.send')
    def test_create_organization_success(self, mock_organization_created_send):

        data = {
            'name': fake.user_name()
        }

        serializer = OrganizationSerializer(data=data, context={'request': self.request})
        is_valid = serializer.is_valid()
        organization = serializer.save()

        self.assertTrue(is_valid)
        self.assertEqual(data['name'], organization.name)

        mock_organization_created_send.assert_called_once_with(sender=organization.__class__, organization=organization, user=self.request.user)

    def test_create_organization_name_invalid_fail(self):

        data = {
            'name': 'not a valid name',
        }

        serializer = OrganizationSerializer(data=data, context={'request': self.request})
        is_valid = serializer.is_valid()
        errors = serializer.errors

        # self.assertS

        self.assertFalse(is_valid)
        self.assertEqual(['name'], [*errors])
        self.assertIn('Enter a valid "slug" consisting of letters, numbers, underscores or hyphens.', str(errors))

    def test_create_organization_name_existing_fail(self):
        name = fake.user_name()

        OrganizationFactory.create(name=name)

        data = {
            'name': name
        }

        serializer = OrganizationSerializer(data=data, context={'request': self.request})
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

        serializer = OrganizationSerializer(organization, data=data, context={'request': self.request})
        serializer.is_valid()
        serializer.save()

        self.assertEqual('quikwise', organization.name)

    def test_update_organization_with_self_name_success(self):
        name = fake.user_name()

        organization = OrganizationFactory.create(name=name)

        data = {
            'name': name
        }

        serializer = OrganizationSerializer(organization, data=data, context={'request': self.request})
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

        serializer = OrganizationSerializer(organization, data=data, context={'request': self.request})
        is_valid = serializer.is_valid()
        errors = serializer.errors

        self.assertFalse(is_valid)
        self.assertEqual(['name'], [*errors])
        self.assertIn('organization with this name already exists.', str(errors))