from django.contrib import admin
from django.urls import path
from Api.views import ImageUploadView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
     path('upload/', ImageUploadView.as_view(), name='image_upload'),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
