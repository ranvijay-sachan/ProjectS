from rest_framework import permissions


class MyCustomPermissions(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if obj.owner.id == request.user_id:
            return True

        if "manage_product" in request.user.Permissions:
            return True

        if request.method in permissions.SAFE_METHODS and "read_product" in request.user.Permissions:
            return True

        return False
