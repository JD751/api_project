# Generated by Django 4.1.7 on 2023-03-13 10:18

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0007_rename_thumbnail_image_thumbnails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='thumbnails',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='thumbnails'),
        ),
    ]
