from rest_framework.permissions import BasePermission


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        return request.user and request.user.is_authenticated and request.user.seller is not None


class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.buyer is not None
