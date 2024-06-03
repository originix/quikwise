from apps.memberships.abstracts import MembershipRole
from apps.memberships.abstracts import MembershipStatus
from apps.memberships.models import Membership
from django.dispatch import receiver
from django.dispatch import Signal
from django.utils import timezone

organization_created = Signal()

@receiver(organization_created)
def handle_organization_created(sender, organization, user, **kwargs):

    Membership.objects.create(
        user=user,
        organization=organization,
        role=MembershipRole.OWNER,
        status=MembershipStatus.JOINED,
        joined_at=timezone.now()
    )