from django.utils.translation import gettext_lazy as _


class MembershipStatus:
    INVITED = 'invited'
    JOINED = 'joined'

    STATUS_CHOICES = (
        (INVITED, _('Invited')),
        (JOINED, _('Joined')),
    )


class MembershipRole:
    OWNER = 'owner'
    ADMIN = 'admin'
    MEMBER = 'member'
    GUEST = 'guest'

    ROLE_CHOICES = [
        (OWNER, 'Owner'),
        (ADMIN, 'Admin'),
        (MEMBER, 'Member'),
        (GUEST, 'Guest'),
    ]