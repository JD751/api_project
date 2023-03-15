# Generated by Django 4.1.7 on 2023-03-14 08:39

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0019_remove_image_avatar_thumbnail_alter_image_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
