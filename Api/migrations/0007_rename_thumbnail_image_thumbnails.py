# Generated by Django 4.1.7 on 2023-03-13 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_alter_image_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='thumbnail',
            new_name='thumbnails',
        ),
    ]
