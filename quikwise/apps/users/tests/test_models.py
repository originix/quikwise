from apps.users.models import User
from django.test import TestCase


class TestAccount(TestCase):

    def setUp(self):
        self.account = User.objects.create(username='demo')

    def test_create_account(self):
        account = User.objects.create(username='demo1')
        self.assertEqual(account.__str__(), 'demo1')

    def test_read_account(self):
        account = User.objects.get(username='demo')
        self.assertEqual(account.__str__(), 'demo')
