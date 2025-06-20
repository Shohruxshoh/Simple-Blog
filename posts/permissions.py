from django.contrib.auth.middleware import LoginRequiredMiddleware
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or request.user.is_superuser
