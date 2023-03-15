from rest_framework.parsers import MultiPartParser, FormParser
from .models import UserProfile, UploadedImage
from .serializers import ImageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet




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



 

