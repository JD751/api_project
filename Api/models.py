from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    USER_PLAN_CHOICES = [
        ('B', 'Basic'),
        ('P', 'Premium'),
        ('E', 'Enterprise'),
    ]
    user = models.ForeignKey(User, max_length=15, on_delete=models.CASCADE)
    plan = models.CharField(max_length=1, choices=USER_PLAN_CHOICES, default='B')

class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, max_length=15, on_delete=models.CASCADE, null=True)
