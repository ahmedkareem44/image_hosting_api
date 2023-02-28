from rest_framework import serializers
from image_app.models import Image, Thumbnail
from PIL import Image as PIL_Image


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.HyperlinkedIdentityField(view_name='image_view-detail', lookup_field="uuid_field")
    image = serializers.ImageField(write_only=True)
    upload_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Image
        fields = ['uuid_field', 'image_url', 'title', 'upload_date', 'image']

    def validate_image(self, obj):
        img = PIL_Image.open(obj)
        img_format = img.format # 'JPEG'
        if img_format.lower() not in ["jpg", "png", 'jpeg']:
            raise serializers.ValidationError(f"{img_format} files are not supported.")
        return obj

    def check_title_is_unique(self, user):
        if Image.objects.filter(title=self.initial_data["title"], user=user):
            raise serializers.ValidationError("title must be unique")


class ThumbnailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thumbnail
        fields = ['image', 'size']


class ImageDetailsSerializer(serializers.ModelSerializer):
    thumbnails = ThumbnailSerializer(many=True, read_only=True)
    original_image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['uuid_field', 'user', 'title', 'upload_date', 'thumbnails', 'original_image', 'expiring_link']

    def get_original_image(self, image):
        request = self.context.get('request')
        if isinstance(image.original_image, str):
            return image.original_image
        original_image = image.image.url
        return request.build_absolute_uri(original_image)
