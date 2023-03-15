# Generated by Django 4.1.7 on 2023-03-13 20:55

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0017_image_avatar_thumbnail_alter_image_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
