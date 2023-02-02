from rest_framework.permissions import BasePermission, SAFE_METHODS


class OnlyForAuthenticatedUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)
