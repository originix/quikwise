from apps.memberships.abstracts import MembershipRole
from apps.memberships.abstracts import MembershipStatus
from apps.memberships.models import Membership
from apps.organizations.models import Organization
from apps.organizations.signals import organization_created
from apps.users.factories import UserFactory
from django.test import TestCase


class TestOrganizationCreatedSignal(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.organization = Organization.objects.create(name='quikwise')

    def test_handle_organization_created(self):
        organization_created.send(sender=Organization, organization=self.organization, user=self.user)

        membership = Membership.objects.get(user=self.user, organization=self.organization)

        self.assertEqual(MembershipRole.OWNER, membership.role)
        self.assertEqual(MembershipStatus.JOINED, membership.status)
        self.assertEqual(1, self.organization.members.count())