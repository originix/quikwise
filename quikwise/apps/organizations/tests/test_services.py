from apps.organizations.models import Organization
from apps.organizations.services import is_name_available
from django.test import TestCase


class TestOrganizationService(TestCase):

    def setUp(self):
        self.organization = Organization.objects.create(name='quikwise')

    def test_is_name_available_name_exists_and_organization_is_none(self):

        available = is_name_available('quikwise')

        self.assertEqual(False, available)

    def test_is_name_available_name_not_exists_and_organization_is_none(self):

        available = is_name_available('quikwise-pro')

        self.assertEqual(True, available)

    def test_is_name_available_name_exists_and_self_organization(self):

        available = is_name_available('quikwise', self.organization)

        self.assertEqual(True, available)

    def test_is_name_available_name_exists_and_other_organization(self):
        other = Organization.objects.create(name='quikwise-pro')

        available = is_name_available('quikwise', other)

        self.assertEqual(False, available)