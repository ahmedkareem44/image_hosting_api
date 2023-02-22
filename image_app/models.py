from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
from django.dispatch import receiver
from image_app.util import image_resize


class ThumbnailType(models.Model):
    size = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.size}"


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to="static/")
    upload_data = models.DateTimeField('upload date', default=datetime.datetime.now)

    @property
    def original_image(self):
        if self.user.user_subscription.account_tier.originally_uploaded_file:
            return self.image
        else:
            return "N/A"

    @property
    def expiring_link(self):
        if self.user.user_subscription.account_tier.expiring_link:
            return "/expiring_link"
        else:
            return "N/A"


class Thumbnail(models.Model):
    original = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='thumbnails')
    image = models.ImageField(upload_to="static/")
    size = models.IntegerField()

    class Meta:
        unique_together = ('original', 'size',)

    @property
    def user(self):
        return self.original.user


class AccountTier(models.Model):
    plan_title = models.CharField(max_length=500, unique=True)
    thumbnail_type = models.ManyToManyField(ThumbnailType)
    originally_uploaded_file = models.BooleanField(default=False)
    expiring_link = models.BooleanField(default=False)

    def __str__(self):
        return self.plan_title


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_subscription")
    account_tier = models.ForeignKey(AccountTier, on_delete=models.PROTECT)


class CreateImageThumbnail:
    def __init__(self, image_object):
        self.image_object = image_object

    def create(self):
        user = self.image_object.user

        if hasattr(user, 'user_subscription'):
            for thumbnails_type in user.user_subscription.account_tier.thumbnail_type.all():
                self.make_thumbnail(thumbnails_type)

    def make_thumbnail(self, thumbnails_type):
        image_upload = image_resize(self.image_object.image, thumbnails_type.size)
        Thumbnail(original=self.image_object, image=image_upload, size=thumbnails_type.size).save()


@receiver(post_save, sender=Image)
def remove_from_inventory(sender, instance, **kwargs):
    if kwargs.get('created'):
        a = instance
        CreateImageThumbnail(a).create()