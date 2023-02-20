from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime


class ThumbnailType(models.Model):
    size = models.IntegerField(unique=True)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to="static/")
    upload_data = models.DateTimeField('upload date', default=datetime.datetime.now)


class Thumbnail(models.Model):
    original = models.ForeignKey(Image, on_delete=models.PROTECT)
    image = models.ImageField()
    size = models.IntegerField()


class AccountTier(models.Model):
    thumbnail_type = models.ManyToManyField(ThumbnailType)
    plan_title = models.CharField(max_length=500)
    originally_uploaded_file = models.BooleanField()
    expiring_link = models.BooleanField()
