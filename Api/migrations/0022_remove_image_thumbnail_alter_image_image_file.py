# Generated by Django 4.1.7 on 2023-03-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0021_alter_image_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
