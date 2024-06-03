from apps.base import permissions
from apps.memberships.abstracts import MembershipRole
from apps.memberships.abstracts import MembershipStatus
from apps.memberships.models import Membership
from apps.organizations.models import Organization
from apps.organizations.permissions import OrganizationPermission
from apps.users.factories import UserFactory
from django.test import TestCase
from unittest.mock  import MagicMock


class TestOrganizationPermission(TestCase):

    def setUp(self):
        self.organization = Organization.objects.create(name='quikwise')
        self.user = UserFactory.create()
        self.permission = OrganizationPermission()

        self.request = MagicMock(user=self.user)
        self.view = MagicMock()

    def test_has_permissions_returns_true_when_auth(self):
        self.request.method = permissions.GET_METHOD

        self.assertTrue(self.permission.has_permission(self.request, self.view))

    def test_has_permissions_returns_false_when_not_auth(self):
        self.request.method = permissions.GET_METHOD
        self.request = MagicMock(user=MagicMock(is_authenticated=False))

        self.assertFalse(self.permission.has_permission(self.request, self.view))

    def test_has_object_permissions_returns_true_when_http_method_is_safe_method(self):
        self.request.method = permissions.GET_METHOD

        Membership.objects.create(organization=self.organization, user=self.user, status=MembershipStatus.JOINED, role=MembershipRole.MEMBER)

        self.assertTrue(self.permission.has_object_permission(self.request, self.view, self.organization))

    def test_has_object_permissions_returns_false_when_http_method_is_not_safe_method_and_membership_not_exists(self):
        self.request.method = permissions.PUT_METHOD

        self.assertFalse(self.permission.has_object_permission(self.request, self.view, self.organization))

    def test_has_object_permissions_returns_false_when_http_method_is_not_safe_method_and_membership_in_not_owner(self):
        self.request.method = permissions.PUT_METHOD

        Membership.objects.create(organization=self.organization, user=self.user, status=MembershipStatus.JOINED, role=MembershipRole.MEMBER)

        self.assertFalse(self.permission.has_object_permission(self.request, self.view, self.organization))

    def test_has_object_permissions_returns_true_when_http_method_is_not_safe_method_and_membership_in_owner(self):
        self.request.method = permissions.PUT_METHOD

        Membership.objects.create(organization=self.organization, user=self.user, status=MembershipStatus.JOINED, role=MembershipRole.OWNER)

        self.assertTrue(self.permission.has_object_permission(self.request, self.view, self.organization))