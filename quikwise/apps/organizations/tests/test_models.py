from apps.organizations.models import Organization
from django.test import TestCase


class TestOrganization(TestCase):

    def setUp(self):
        self.organization = Organization.objects.create(name='quikwise')

    def test_create_organization(self):
        organization = Organization.objects.create(name='quikwise-pro')
        self.assertEqual(organization.__str__(), 'quikwise-pro')

    def test_get_organization(self):
        organization = Organization.objects.get(name='quikwise')
        self.assertEqual(organization.__str__(), 'quikwise')
