# Generated by Django 4.1.7 on 2023-02-21 21:05

from django.db import migrations


def initial_values(apps, schema_editor):
    ThumbnailType = apps.get_model('image_app', 'ThumbnailType')
    thumbnail_type200 = ThumbnailType(size=200)
    thumbnail_type200.save()
    thumbnail_type400 = ThumbnailType(size=400)
    thumbnail_type400.save()

    AccountTier = apps.get_model('image_app', 'AccountTier')
    account_tier_basic = AccountTier(plan_title="Basic", originally_uploaded_file=False, expiring_link=False)
    account_tier_basic.save()
    account_tier_basic.thumbnail_type.add(thumbnail_type200)
    account_tier_basic.save()

    account_tier_basic = AccountTier(plan_title="Premium", originally_uploaded_file=True, expiring_link=False)
    account_tier_basic.save()
    account_tier_basic.thumbnail_type.add(thumbnail_type200)
    account_tier_basic.thumbnail_type.add(thumbnail_type400)
    account_tier_basic.save()

    account_tier_basic = AccountTier(plan_title="Enterprise", originally_uploaded_file=True, expiring_link=True)
    account_tier_basic.save()
    account_tier_basic.thumbnail_type.add(thumbnail_type200)
    account_tier_basic.thumbnail_type.add(thumbnail_type400)
    account_tier_basic.save()


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0007_alter_image_user_alter_subscription_user_and_more'),
    ]

    operations = [
        migrations.RunPython(initial_values),
    ]
