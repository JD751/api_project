# Generated by Django 4.1.7 on 2023-03-14 08:31

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0018_alter_image_avatar_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='avatar_thumbnail',
        ),
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]