# Generated by Django 4.1.7 on 2023-03-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_remove_image_thumbnails'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnails/'),
        ),
    ]
