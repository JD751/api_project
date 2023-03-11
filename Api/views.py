from rest_framework.parsers import MultiPartParser, FormParser
from .models import Image
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
        return Image.objects.filter(user=user)

    # def get_queryset(self, request):
    #     return Image.objects.filter(user=request.user.pk).all()
