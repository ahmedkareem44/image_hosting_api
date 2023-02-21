from django.shortcuts import render

# Create your views here.

from rest_framework import generics
# from rest_framework import permissions
from image_app.serializers import ImageSerializer, ImageDetailsSerializer, ThumbnailSerializer
from image_app.models import Image, Thumbnail
from rest_framework import permissions
# from PIL import Image as PIL_Image


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to read it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ImageList(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

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
    serializer_class = ImageDetailsSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)


class ThumbnailDetail(generics.RetrieveAPIView):
    serializer_class = ThumbnailSerializer
    queryset = Thumbnail.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]

