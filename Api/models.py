from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from protected_media.models import ProtectedImageField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Tier(models.Model):
    name = models.CharField(max_length=255)
    access_original = models.BooleanField(default=False)
    has_expiring_links = models.BooleanField(default=False)

    def validate_thumbnail_size(value):
        if value not in ['200', '400']:
            raise ValidationError("Thumbnail size must either be 200 or 400")
        
    thumbnail_sizes = models.CharField(
        max_length=255, 
        help_text="Only 200 or 400 value allowed",
        validators=[validate_thumbnail_size]
    )

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    BASIC = 'B'
    PREMIUM = 'P'
    ENTERPRISE = 'E'

    USER_PLAN_CHOICES = [
        (BASIC, 'Basic'),
        (PREMIUM, 'Premium'),
        (ENTERPRISE, 'Enterprise'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)# each user will only have one user profile
    plan = models.CharField(
        max_length=1, choices=USER_PLAN_CHOICES, null=True, blank=True)
    custom_tier = models.ForeignKey(Tier, on_delete=models.CASCADE, default=None, null=True, blank=True)
    
class ExpirationTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expiration_time = models.PositiveIntegerField(default=300, 
                                                  validators=[MinValueValidator(300), MaxValueValidator(30000)],
                                                    help_text="Expiration time in seconds",
                                                    )

def get_user_expiration_time(user):
    try:
        expiration_time = ExpirationTime.objects.get(user=user)
    except ExpirationTime.DoesNotExist:
        expiration_time = ExpirationTime.objects.create(user=user, expiration_time=300)

    return expiration_time

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/', default=None, null=True)
    image_exp = ProtectedImageField(upload_to='images/', default=None, null=True)
    expiration_time = models.ForeignKey(ExpirationTime, on_delete=models.CASCADE, null=True)
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
        User, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.image)
