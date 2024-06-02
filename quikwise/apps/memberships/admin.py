from apps.memberships.models import Membership
from django.contrib import admin


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0
    exclude = [
        # 'deleted_at'
    ]

    autocomplete_fields = [
        'user',
    ]