from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class UserProfile(models.Model):
    BASIC = 'B'
    PREMIUM = 'P'
    ENTERPRISE = 'E'

    USER_PLAN_CHOICES = [
        (BASIC, 'Basic'),
        (PREMIUM, 'Premium'),
        (ENTERPRISE, 'Enterprise'),
    ]
    user = models.ForeignKey(User, max_length=15, on_delete=models.CASCADE)
    plan = models.CharField(
        max_length=1, choices=USER_PLAN_CHOICES, default=BASIC)

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/', default=None, null=True)
    thumbnail_200 = ImageSpecField(source='image',
                                   processors=[ResizeToFill(200,200)],
                                   format='JPEG',
                                   options={'quality': 60})
    thumbnail_400 = ImageSpecField(source='image',
                                   processors=[ResizeToFill(400,400)],
                                   format='JPEG',
                                   options={'quality': 60})
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, max_length=15, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)
