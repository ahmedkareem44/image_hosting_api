# Generated by Django 4.1.7 on 2023-02-27 23:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0011_rename_expiring_link_accounttier_can_access_original_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='uuid_field',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
