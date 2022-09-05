from rest_framework.permissions import BasePermission


class BasicPermission(BasePermission):

    def has_permission(self, request, view):
        return True


class AuthPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return bool(request.user
                    and request.user.is_authenticated)

class OnlyAuthPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user
                    and request.user.is_authenticated)

class AdminPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ("POST"):
            return True
        elif request.method in ("GET", "PUT", "UPDATE"):
            return bool(request.user
                        and request.user.is_authenticated)
        elif request.method == "DELETE":
            return bool(request.user
                        and request.user.is_authenticated
                        and request.user.is_staff)
        return False
