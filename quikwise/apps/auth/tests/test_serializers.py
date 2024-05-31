from apps.auth.serializers import RegisterSerializer
from apps.users.factories import UserFactory
from rest_framework.test import APITestCase
from faker import Faker

fake = Faker()

class TestRegisterSerializer(APITestCase):

    def test_serializing_object_user(self):
        user = UserFactory()

        serializer = RegisterSerializer(user)

        actual = serializer.data

        expected = {
            'name': user.name,
            'username': user.username,
            'email': user.email,
        }

        self.assertEqual(expected, actual)

    def test_register_user_success(self):
        password = fake.password()

        data = {
            'name': fake.name(),
            'username': fake.user_name(),
            'email': fake.email(),
            'password': password,
            'confirm_password': password
        }

        serializer = RegisterSerializer(data=data)
        is_valid = serializer.is_valid()
        user = serializer.save()

        self.assertTrue(is_valid)
        self.assertEqual(data['username'], user.username)
        self.assertEquals(user.check_password(password), True)

    def test_register_user_with_existing_username_fail(self):
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

        serializer = RegisterSerializer(data=data)
        is_valid = serializer.is_valid()
        errors = serializer.errors

        self.assertFalse(is_valid)
        self.assertEqual(['username'], [*errors])
        self.assertIn('A user with that username already exists.', str(errors))

    def test_register_user_with_existing_email_fail(self):
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

        serializer = RegisterSerializer(data=data)
        is_valid = serializer.is_valid()
        errors = serializer.errors

        self.assertFalse(is_valid)
        self.assertEqual(['email'], [*errors])
        self.assertIn('A User With That Email Already Exists.', str(errors))

    def test_register_user_with_password_not_match_confirm_password_fail(self):
        password = fake.password()

        data = {
            'name': fake.name(),
            'username': fake.user_name(),
            'email': fake.email(),
            'password': password,
            'confirm_password': password + "extra"
        }

        serializer = RegisterSerializer(data=data)
        is_valid = serializer.is_valid()
        errors = serializer.errors

        self.assertFalse(is_valid)
        self.assertEqual(['confirm_password'], [*errors])
        self.assertIn("Those passwords don\'t match.", str(errors))