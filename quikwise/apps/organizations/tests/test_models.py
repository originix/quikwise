from apps.memberships.models import MembershipStatus
from apps.memberships.models import MembershipRole
from apps.memberships.models import Membership
from apps.organizations.models import Organization
from apps.users.factories import UserFactory
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

    def test_is_owner(self):
        organization = Organization.objects.get(name='quikwise')

        owner = UserFactory()
        member = UserFactory()

        Membership.objects.create(organization=organization, user=owner, status=MembershipStatus.JOINED, role=MembershipRole.OWNER)
        Membership.objects.create(organization=organization, user=member, status=MembershipStatus.JOINED, role=MembershipRole.MEMBER)

        self.assertEqual(True, organization.is_owner(owner))
        self.assertEqual(False, organization.is_owner(member))
