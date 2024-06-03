import reversion

from apps.base.models import ControlModel
from apps.memberships.abstracts import MembershipStatus
from apps.memberships.abstracts import MembershipRole
from apps.organizations.models import Organization
from apps.users.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


@reversion.register()
class Membership(ControlModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name=_('organization'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    role = models.CharField(max_length=16, choices=MembershipRole.ROLE_CHOICES, default=MembershipRole.MEMBER, db_index=True,  verbose_name=_('role'))
    status = models.CharField(max_length=16, choices=MembershipStatus.STATUS_CHOICES, default=MembershipStatus.INVITED, db_index=True, verbose_name=_('status'))
    joined_at = models.DateTimeField(blank=True, null=True, verbose_name=_('joined at'))

    class Meta:
        db_table = 'membership'
        ordering = ['id']
        verbose_name = _('membership')
        verbose_name_plural = _('memberships')
        constraints = [
            models.UniqueConstraint(fields=['organization', 'user'], name='organization_user_unique')
        ]

    def __str__(self):
        return f"{self.organization.name} - {self.user.username} - {self.status}"