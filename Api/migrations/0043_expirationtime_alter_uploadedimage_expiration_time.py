# Generated by Django 4.1.7 on 2023-03-23 10:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Api', '0042_remove_uploadedimage_image_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpirationTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_time', models.PositiveIntegerField(default=10, help_text='Expiration time in seconds', validators=[django.core.validators.MinValueValidator(300), django.core.validators.MaxValueValidator(30000)])),
                ('user', models.ForeignKey(max_length=15, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='expiration_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.expirationtime'),
        ),
    ]
