# Generated by Django 4.1.7 on 2023-02-20 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image_app', '0004_alter_subscription_account_tier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]
