from rest_framework import permissions


class IsObjectOwner(permissions.BasePermission):
    """
    Custom permission to only allow
    owners of an object to view and edit it.  Returns
    true if user is owner
    """
    def has_object_permission(self, request, view, obj):
        """Return Bool representing object permissions."""
        if request.method == "POST":
            return True
        return obj.user == request.user
