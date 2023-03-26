from rest_framework import serializers
from .models import UploadedImage, UserProfile, get_user_expiration_time
from datetime import datetime, timedelta
from django.urls import reverse



class ImageSerializer(serializers.ModelSerializer):
    thumbnail_url_200 = serializers.SerializerMethodField()
    thumbnail_url_400 = serializers.SerializerMethodField()
    thumbnail_url_custom = serializers.SerializerMethodField()
    expiring_url = serializers.SerializerMethodField()

    class Meta:
        model = UploadedImage
        fields = ('user','image','expiring_url',
                  'thumbnail_url_200', 'thumbnail_url_400','thumbnail_url_custom')
        
    

    def get_thumbnail_url_custom(self, obj):
        user_profile = obj.user_profile
        if user_profile.custom_tier:
            size = int(user_profile.custom_tier.thumbnail_sizes.split(',')[0])
            thumbnail_mapping = {
                200: obj.thumbnail_200.url,
                400: obj.thumbnail_400.url,
            }
            return thumbnail_mapping.get(size)
        return None

    

    

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
        user_profile = instance.user_profile

        tier = None
        if user_profile.custom_tier:
            tier = user_profile.custom_tier

        if not tier:
            if user_profile.plan == UserProfile.BASIC:
                rep.pop('image', None)
                rep.pop('thumbnail_url_400', None)
                rep.pop('expiring_url', None)
                rep.pop('thumbnail_url_custom', None)
            elif user_profile.plan == UserProfile.PREMIUM:
                rep.pop('expiring_url', None)
                rep.pop('thumbnail_url_custom', None)
            elif user_profile.plan == UserProfile.ENTERPRISE:
                rep.pop('thumbnail_url_custom', None)
        else:
            rep.pop('thumbnail_url_200', None)
            rep.pop('thumbnail_url_400', None)
            if not tier.access_original:
                rep.pop('image', None)

            if not tier.has_expiring_links:
                rep.pop('expiring_url', None)



        return rep

    
    def create(self, validated_data):
        user = self.context['request'].user
        expiration_time = get_user_expiration_time(user)
        validated_data['expiration_time'] = expiration_time
        return super().create(validated_data)


    def get_expiring_url(self, obj):
        user_expiration_time = get_user_expiration_time(obj.user)
        expiration_timestamp = (datetime.now() + timedelta(seconds=user_expiration_time.expiration_time)).timestamp()
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('serve_expiring_image', args=[obj.pk, expiration_timestamp]))
