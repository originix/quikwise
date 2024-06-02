from apps.organizations.models import Organization
from rest_framework import permissions


class OrganizationPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj: Organization):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.is_owner(request.user)