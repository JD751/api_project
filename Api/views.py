from rest_framework.parsers import MultiPartParser, FormParser
from .models import UserProfile, UploadedImage
from .serializers import ImageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse, FileResponse
import os

class ImageViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def get_queryset(self):
        user = self.request.user
        return UploadedImage.objects.filter(user=user)
    
    def perform_create(self, serializer):
        user=self.request.user
        user_profile = UserProfile.objects.get(user=user)
        serializer.save(user_profile=user_profile)
        serializer.save(user=user)
        serializer.save(image_exp=self.request.FILES.get('image'))



# def serve_expiring_image(request, image_id, expiration_timestamp):
#     if float(expiration_timestamp) > datetime.now().timestamp():
#         image = get_object_or_404(UploadedImage, pk=image_id)
#         return HttpResponseRedirect(image.image_exp.url)
#     else:
#         raise Http404("Image expired")

from django.http import FileResponse

def serve_expiring_image(request, image_id, expiration_timestamp):
    if float(expiration_timestamp) > datetime.now().timestamp():
        image = get_object_or_404(UploadedImage, pk=image_id)
        user = request.user
        user_profile = UserProfile.objects.get(user=user)

        if user_profile.custom_tier:
            size = int(user_profile.custom_tier.thumbnail_sizes.split(',')[0])
            response_file = image.get_thumbnail_url(size)
        else:
            response_file = image.image.path

        content_type = 'image/jpeg'
        response = FileResponse(open(response_file, 'rb'), content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename={os.path.basename(response_file)}'
        return response
    else:
        raise Http404("Image expired")



 

