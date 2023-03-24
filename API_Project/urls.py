from django.contrib import admin
from django.views.static import serve
from django.urls import path, include, register_converter, re_path
from Api.views import ImageViewSet, serve_expiring_image
from rest_framework import routers
from Api.converters import FloatConverter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.DefaultRouter()
router.register('images', ImageViewSet, basename='images')
register_converter(FloatConverter, 'float')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('expiring-image/<int:image_id>/<float:expiration_timestamp>/',
         serve_expiring_image, name='serve_expiring_image'),
    re_path(r'^protected/(?P<path>.*)$', serve, {'document_root': settings.PROTECTED_MEDIA_ROOT}),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
