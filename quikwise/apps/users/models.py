import reversion

from apps.base.models import ControlModel
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


@reversion.register()
class User(AbstractUser, ControlModel):
    name = models.CharField(blank=True, max_length=255, verbose_name=_('Name'))

    class Meta:
        db_table = 'user'
        ordering = ['-id']
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username
