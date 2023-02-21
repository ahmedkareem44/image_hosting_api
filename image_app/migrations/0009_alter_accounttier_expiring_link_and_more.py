# Generated by Django 4.1.7 on 2023-02-21 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0008_auto_20230221_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttier',
            name='expiring_link',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accounttier',
            name='originally_uploaded_file',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accounttier',
            name='plan_title',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]