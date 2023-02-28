from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
from django.dispatch import receiver
from image_app.util import image_resize
import uuid


class ThumbnailType(models.Model):
    size = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.size}"


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="static/")
    upload_date = models.DateTimeField('upload date', default=datetime.datetime.now)

    class Meta:
        unique_together = ('title', 'user',)

    @property
    def original_image(self):
        if self.user.user_subscription.account_tier.can_access_original_file:
            return self.image
        else:
            return "N/A"

    @property
    def expiring_link(self):
        if self.user.user_subscription.account_tier.can_generate_expiring_links:
            return "/expiring_link"
        else:
            return "N/A"

    def create_thumbnail(self):
        if hasattr(self.user, 'user_subscription'):
            for thumbnails_type in self.user.user_subscription.account_tier.thumbnail_type.all():
                image_upload = image_resize(self.image, thumbnails_type.size)
                Thumbnail(original=self, image=image_upload, size=thumbnails_type.size).save()


class Thumbnail(models.Model):
    original = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='thumbnails')
    image = models.ImageField(upload_to="static/")
    size = models.IntegerField("thumbnail height")

    class Meta:
        unique_together = ('original', 'size',)

    @property
    def user(self):
        return self.original.user


class AccountTier(models.Model):
    plan_title = models.CharField(max_length=500, unique=True)
    thumbnail_type = models.ManyToManyField(ThumbnailType)
    can_access_original_file = models.BooleanField(default=False)
    can_generate_expiring_links = models.BooleanField(default=False)

    def __str__(self):
        return self.plan_title


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_subscription")
    account_tier = models.ForeignKey(AccountTier, on_delete=models.PROTECT)


@receiver(post_save, sender=Image)
def create_image_thumbnail(sender, instance, **kwargs):
    if kwargs.get('created'):
        a = instance
        a.create_thumbnail()