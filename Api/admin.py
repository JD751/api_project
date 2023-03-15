from django.contrib import admin
from .models import UserProfile
from .models import UploadedImage

admin.site.register(UserProfile)
admin.site.register(UploadedImage)