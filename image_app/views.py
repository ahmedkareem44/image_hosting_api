from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework import permissions
from image_app.serializers import ImageSerializer
from image_app.models import Image
from PIL import Image as PIL_Image


class ImageList(generics.ListCreateAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Image.objects.filter(user=user)

    # def validate_image(self, value):
    #     img = PIL_Image.open(filename)
    #     print(img.format)
    #     if value < 18:
    #         raise serializers.ValidationError('The person has to be at least 18 years old.')
    #     return value


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Image.objects.filter(user=user)