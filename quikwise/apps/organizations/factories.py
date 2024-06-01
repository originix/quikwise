import factory

from apps.organizations.models import Organization
from faker import Faker

fake = Faker()


class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization

    name = factory.Sequence(lambda _: fake.user_name())