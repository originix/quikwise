from apps.memberships.admin import MembershipInline
from apps.organizations.models import Organization
from apps.organizations.forms import OrganizationAdminForm
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from reversion.admin import VersionAdmin


@admin.register(Organization)
class OrganizationAdmin(VersionAdmin):
    form = OrganizationAdminForm

    fieldsets = (
        (_('Info'), {'fields': ('name', )}),
        (_('Activity'), {
            'fields': ('created_at', 'updated_at'),
        })
    )

    list_display = [
        'name',
        'created_at',
        'updated_at',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    inlines = [
        MembershipInline
    ]

