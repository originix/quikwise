import django.db.models.options as options

from .managers import SoftDeletionManager
from django.conf import settings
from django.db import models
from django.db.models import signals
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_model_changes import ChangesMixin as ModelChangesMixin
from uuid import uuid4

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('exclude_field_changes',)


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name=_('Deleted at'))

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
        signals.post_delete.send(sender=self.__class__, instance=self)

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


class ControlModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="%(class)s_created_user", verbose_name=_('Created User'))
    updated_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="%(class)s_updated_user", verbose_name=_('Updated User'))

    class Meta:
        abstract = True


class SoftControlModel(ControlModel, SoftDeletionModel):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

    # custom error message that remove 'live' key
    def unique_error_message(self, model_class, unique_check):
        unique_check_list = list(unique_check)
        unique_check = tuple(field for field in unique_check_list if field != 'live')
        return super(SoftControlModel, self).unique_error_message(model_class, unique_check)


class HardControlModel(ControlModel):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class UserControlModel(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True


class ChangesMixin(ModelChangesMixin):

    default_exclude_field_changes = [
        'created_user',
        'updated_user'
    ]

    def current_state(self):
        """
        Returns a ``field -> value`` dict of the current state of the instance.
        """
        exclude_field_changes = []

        if hasattr(self._meta, 'exclude_field_changes'):
            exclude_field_changes = self._meta.exclude_field_changes

        exclude_field_changes = exclude_field_changes + self.default_exclude_field_changes

        field_names = set()
        [field_names.add(f.name) for f in self._meta.local_fields if f.name not in exclude_field_changes]
        [field_names.add(f.attname) for f in self._meta.local_fields]

        return dict([(field_name, getattr(self, field_name)) for field_name in field_names])
