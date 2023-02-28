from django.shortcuts import render

# Create your views here.

from rest_framework import mixins, viewsets, permissions
from image_app.serializers import ImageSerializer, ImageDetailsSerializer
from image_app.models import Image


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to read it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class HasSubscription(permissions.BasePermission):
    """
    Custom permission to only allow subscribed user.
    """
    message = 'User has no active subscription.'

    def has_permission(self, request, view):
        return bool(hasattr(request.user, "user_subscription"))


class ImageViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Returns a list of all images uploaded by the current user.
           user need to be:
           * Logged in
           * is staff
           * has subscription

           for post:
           accepted image format png, jpeg, jpg
           title must be unique

            """

    permission_classes = [permissions.IsAuthenticated, IsOwner, HasSubscription]
    lookup_field = "uuid_field"

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ImageDetailsSerializer
        return ImageSerializer

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.check_title_is_unique(self.request.user)
        serializer.save(user=self.request.user)

