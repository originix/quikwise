import factory

from .models import User
from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda _: fake.name())
    username = factory.Sequence(lambda _: fake.user_name())
    email = factory.Sequence(lambda _: fake.email())