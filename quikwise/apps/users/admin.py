from apps.memberships.admin import MembershipInline
from apps.users.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (_('Personal info'), {'fields': ('username', 'name', 'email', 'password')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Activity'), {
            'fields': ('created_at', 'updated_at', 'last_login', 'date_joined'),
        })
    )

    list_display = [
        'username',
        'name',
        'email'
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
        'last_login',
        'date_joined'
    ]

    inlines = [
        MembershipInline
    ]

    def has_delete_permission(self, request, obj=None):
        return False
