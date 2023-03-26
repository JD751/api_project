# Generated by Django 4.1.7 on 2023-03-22 13:01

from django.db import migrations, models
import protected_media.models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0041_uploadedimage_expiration_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimage',
            name='image_url',
        ),
        migrations.AddField(
            model_name='uploadedimage',
            name='image_exp',
            field=protected_media.models.ProtectedImageField(default=None, null=True, storage=protected_media.models.ProtectedFileSystemStorage(), upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
    ]