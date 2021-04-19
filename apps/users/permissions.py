from rest_framework import permissions
from rest_framework.authtoken.models import Token

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print(obj.user, request.user)
        if request.method in permissions.SAFE_METHODS:
            print('**************************************')
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user