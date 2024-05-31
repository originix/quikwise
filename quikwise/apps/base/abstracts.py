from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractOrdering(models.Model):
    sequence = models.PositiveSmallIntegerField(null=True, blank=True, db_index=True, verbose_name=_('Sequence'))

    class Meta:
        abstract = True
