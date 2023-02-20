from rest_framework import serializers
from image_app.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['user', 'title', 'upload_data']


class ImageDetailsSerializer(serializers.ModelSerializer):
    thumbnails = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Image
        fields = ['user', 'title', 'image', 'upload_data']


