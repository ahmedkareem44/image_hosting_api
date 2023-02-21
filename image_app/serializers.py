from rest_framework import serializers
from image_app.models import Image, Thumbnail
from PIL import Image as PIL_Image


class ImageSerializer(serializers.ModelSerializer):
    image_view = serializers.HyperlinkedIdentityField(view_name='image_view')
    image = serializers.ImageField(write_only=True)
    upload_data = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'image_view', 'title', 'upload_data', 'image']

    def validate_image(self, obj):
        img = PIL_Image.open(obj)
        img_format = img.format # 'JPEG'
        if img_format.lower() not in ["jpg", "png", 'jpeg']:
            raise serializers.ValidationError(f"{img_format} files are not supported.")
        return obj


class ThumbnailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thumbnail
        fields = ['image', 'size']


class ImageDetailsSerializer(serializers.ModelSerializer):
    thumbnails = ThumbnailSerializer(many=True, read_only=True)
    original_image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'user', 'title', 'upload_data', 'thumbnails', 'original_image']

    def get_original_image(self, image):
        request = self.context.get('request')
        if isinstance(image.original_image, str):
            return image.original_image
        original_image = image.image.url
        return request.build_absolute_uri(original_image)
