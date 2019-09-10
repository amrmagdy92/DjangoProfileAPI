from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    # A class to restrict the access to updating profiles
    # A user can only update his own profile only
    def has_object_permission(self, request, view, obj):
        # checks if the user has permission to edit their own profile
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id == request.user.id
