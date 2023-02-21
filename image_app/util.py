from PIL import Image
import io
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile


def image_resize(image, size):
    img_io = io.BytesIO()
    img = Image.open(image)
    img_format = img.format
    img.thumbnail((size, size))
    img.save(img_io, format=img_format)
    new_pic = InMemoryUploadedFile(img_io,
                                   'ImageField',
                                   f"{image}thumbnail{size}.{img_format}",
                                   f'image/{img_format}',
                                   sys.getsizeof(img_io), None)
    return new_pic


def main():
    pass


if __name__ == "__main__":
    main()