from PIL import Image
import io
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile


def image_resize(image, size):
    img_io = io.BytesIO()
    img = Image.open(image)
    img.thumbnail((size, size))
    img.save(img_io, format="JPEG")
    new_pic = InMemoryUploadedFile(img_io,
                                   'ImageField',
                                   f"{image}thumbnail{size}.jpg",
                                   'image/jpeg',
                                   sys.getsizeof(img_io), None)
    return new_pic
