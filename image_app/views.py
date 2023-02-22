from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from image_app.serializers import ImageSerializer, ImageDetailsSerializer
from image_app.models import Image
from rest_framework import permissions


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


class ImageList(generics.ListCreateAPIView):
    """Returns a list of all images uploaded by the current user.
       user need to be:
       * Logged in
       * is staff
       * has subscription

       for post:
       accepted image format png, jpeg, jpg
       title must be unique

        """
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, HasSubscription]

    def get_queryset(self):
        """
        This view should return a list of all the images
        for the currently authenticated user.
        """
        user = self.request.user
        return Image.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ImageDetail(generics.RetrieveAPIView):
    """
        Returns an Image object
    """
    serializer_class = ImageDetailsSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, HasSubscription]

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)
