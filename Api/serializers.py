from rest_framework import serializers
from .models import UploadedImage, UserProfile

class ImageSerializer(serializers.ModelSerializer):
    thumbnail_url_200 = serializers.SerializerMethodField()
    thumbnail_url_400 = serializers.SerializerMethodField()
    
    class Meta:
        model = UploadedImage
        fields = ('user','image','thumbnail_url_200', 'thumbnail_url_400')

    def get_thumbnail_url_200(self, obj):
        if obj.user_profile.plan == UserProfile.BASIC or obj.user_profile.plan == UserProfile.PREMIUM or obj.user_profile.plan == UserProfile.ENTERPRISE:
            return obj.thumbnail_200.url
        return None

    def get_thumbnail_url_400(self, obj):
        if obj.user_profile.plan == UserProfile.PREMIUM or obj.user_profile.plan == UserProfile.ENTERPRISE:
            return obj.thumbnail_400.url
        return None
    

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.user_profile.plan == UserProfile.BASIC:
            rep.pop('image')
            rep.pop('thumbnail_url_400')
        return rep


       
        
        



