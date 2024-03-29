from rest_framework.permissions import BasePermission, SAFE_METHODS
from . import models


class IsAdminOrReadOnly(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )