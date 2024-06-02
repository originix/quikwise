import reversion

from apps.base.models import SoftControlModel
from apps.memberships.abstracts import MembershipStatus
from apps.memberships.abstracts import MembershipRole
from apps.users.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


@reversion.register()
class Organization(SoftControlModel):
    name = models.SlugField(max_length=64, db_index=True, unique=True, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    members = models.ManyToManyField(User, through='memberships.Membership', blank=True, verbose_name=_('members'))

    class Meta:
        db_table = 'organization'
        ordering = ['id']
        verbose_name = _('organization')
        verbose_name_plural = _('organizations')

    def __str__(self):
        return self.name

    def is_owner(self, user):
        return self.membership_set.filter(user=user, status=MembershipStatus.JOINED, role=MembershipRole.OWNER).exists()

