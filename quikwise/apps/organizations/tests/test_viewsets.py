from apps.memberships.abstracts import MembershipStatus
from apps.memberships.abstracts import MembershipRole
from apps.memberships.models import Membership
from apps.organizations.factories import OrganizationFactory
from apps.organizations.models import Organization
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker

from apps.users.factories import UserFactory

fake = Faker()

class TestOrganizationViewSet(APITestCase):

    def setUp(self):
        self.organizations = OrganizationFactory.create_batch(4)
        self.user = UserFactory.create()
        self.client.force_login(self.user)

        for organization in self.organizations[:-1]:

            Membership.objects.create(organization=organization, user=self.user, status=MembershipStatus.JOINED)

    def test_list_organization(self):
        url = reverse('api:organization-list')

        response = self.client.get(url, format='json')
        response_json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(3, len(response_json['data']))

    def test_create_organization(self):
        url = reverse('api:organization-list')

        data = {
            'name': fake.user_name(),
        }

        response = self.client.post(url, data=data, format='json')
        response_json = response.json()

        organization = Organization.objects.get(name=data['name'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['name'], response_json['data']['name'])

        self.assertEqual(1, organization.members.count())
        self.assertEqual(MembershipRole.OWNER, organization.membership_set.first().role)
        self.assertEqual(MembershipStatus.JOINED, organization.membership_set.first().status)
        self.assertEqual(self.user, organization.membership_set.first().user)

    def test_get_organization(self):
        organization = OrganizationFactory.create(name='quikwise-organization')
        Membership.objects.create(organization=organization, user=self.user, status=MembershipStatus.JOINED)

        url = reverse('api:organization-detail', kwargs={'name': organization.name})

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_organization(self):
        organization = OrganizationFactory.create(name='quikwise-organization')
        Membership.objects.create(organization=organization, user=self.user, status=MembershipStatus.JOINED, role=MembershipRole.OWNER)

        url = reverse('api:organization-detail', kwargs={'name': organization.name})

        data = {
            'name': 'quikwise-new'
        }

        response = self.client.put(url, data=data, format='json')
        response_json = response.json()

        organization.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['name'], response_json['data']['name'])
        self.assertEqual('quikwise-new', organization.name)
    #
    def test_delete_organization(self):
        organization = OrganizationFactory.create(name='quikwise-organization')
        Membership.objects.create(organization=organization, user=self.user, status=MembershipStatus.JOINED, role=MembershipRole.OWNER)

        url = reverse('api:organization-detail', kwargs={'name': organization.name})

        response = self.client.delete(url, format='json')

        organization.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNotNone(organization.deleted_at)