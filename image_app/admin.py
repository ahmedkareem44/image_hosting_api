from django.contrib import admin
from image_app.models import Image

# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'upload_data', 'image')
    #filter_horizontal = ('location','brand')
    list_filter = ["user",]
