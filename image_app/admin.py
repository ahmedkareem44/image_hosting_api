from django.contrib import admin
from image_app.models import Image, Subscription, AccountTier, ThumbnailType, Thumbnail
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.


@admin.register(Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'original', 'size')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'upload_data', 'image')
    list_filter = ["user", ]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'account_tier')


@admin.register(AccountTier)
class AccountTierAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan_title', 'originally_uploaded_file', 'expiring_link')
    filter_horizontal = ('thumbnail_type',)


@admin.register(ThumbnailType)
class ThumbnailTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size')


class SubscriptionInline(admin.TabularInline):
    model = Subscription
    can_delete = False


class UserExtensionAdmin(UserAdmin):
    inlines = [
        SubscriptionInline,
    ]


admin.site.unregister(User)
admin.site.register(User, UserExtensionAdmin)
