from django.contrib import admin
from .models import UserProfile, ExpirationTime, UploadedImage, Tier

admin.site.register(UserProfile)
admin.site.register(UploadedImage)
admin.site.register(ExpirationTime)
admin.site.register(Tier)