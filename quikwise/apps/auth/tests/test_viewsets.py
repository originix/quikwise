from apps.users.models import User
from apps.users.factories import UserFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker

fake = Faker()

class TestRegisterViewSet(APITestCase):

    def setUp(self):
        pass

    def test_register_user(self):
        url = reverse('api:register-list')
        password = fake.password()

        data = {
            'name': fake.name(),
            'username': fake.user_name(),
            'email': fake.email(),
            'password': password,
            'confirm_password': password
        }

        response = self.client.post(url, data=data, format='json')
        response_json = response.json()

        expected = {
            'name': data['name'],
            'username': data['username'],
            'email': data['email']
        }

        user = User.objects.get(username=data['username'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(expected, response_json['data'])
        self.assertEquals(user.check_password(password), True)

    def test_register_user_existing_user_should_fail(self):
        url = reverse('api:register-list')
        username = fake.user_name()
        password = fake.password()

        UserFactory.create(username=username)

        data = {
            'name': fake.name(),
            'username': username,
            'email': fake.email(),
            'password': password,
            'confirm_password': password
        }

        response = self.client.post(url, data=data, format='json')

        self.assertContains(response, "A user with that username already exists.", status_code=status.HTTP_400_BAD_REQUEST)

    def test_register_user_existing_email_should_fail(self):
        url = reverse('api:register-list')
        email = fake.email()
        password = fake.password()

        UserFactory.create(email=email)

        data = {
            'name': fake.name(),
            'username': fake.user_name(),
            'email': email,
            'password': password,
            'confirm_password': password
        }

        response = self.client.post(url, data=data, format='json')

        self.assertContains(response, "A user with that email already exists.", status_code=status.HTTP_400_BAD_REQUEST)

    def test_register_user_password_not_match_confirm_password_should_fail(self):
        url = reverse('api:register-list')
        password = fake.password()

        data = {
            'name': fake.name(),
            'username': fake.user_name(),
            'email': fake.email(),
            'password': password,
            'confirm_password': password + "extra"
        }

        response = self.client.post(url, data=data, format='json')

        self.assertContains(response, "Those passwords don't match.", status_code=status.HTTP_400_BAD_REQUEST)