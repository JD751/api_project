from django.test import TestCase
from rest_framework.test import APITestCase
from Api.models import ExpirationTime, UploadedImage
from django.contrib.auth.models import User
from Api.models import UserProfile, Tier
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from django.utils import timezone
import tempfile
from django.conf import settings
import shutil
import unittest
from Api.models import Tier
import unittest
from django.core.exceptions import ValidationError



class ModelsAndImageGenerationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.tier = Tier.objects.create(name='Custom Tier', thumbnail_sizes='200')
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_model_creation(self):
        # Checks if UserProfile, Tier, and ExpirationTime objects are created correctly
        self.assertIsNotNone(self.user_profile)
        self.assertIsNotNone(self.tier)
        image_data = b"dummy_image_data"  # Binary data representing an image
        image_file = SimpleUploadedFile("test_image.png", image_data, content_type="image/png")
        expiration_time = ExpirationTime.objects.create(user=self.user, expiration_time=300)
        self.assertIsNotNone(expiration_time)

        # Uploading the image and check if the UploadedImage object is created correctly
        uploaded_image = UploadedImage.objects.create(image=image_file, user=self.user, user_profile=self.user_profile)


        self.assertIsNotNone(uploaded_image)
        self.assertEqual(uploaded_image.user, self.user)
        self.assertEqual(uploaded_image.user_profile, self.user_profile)


class AuthenticationTest(APITestCase):

        def setUp(self):
            self.user = User.objects.create_user(
                username="testuser",
                email="test@example.com",
                password="testpassword"
            )

            self.tier = Tier.objects.create(name='Custom Tier', thumbnail_sizes='200')
            self.user_profile = UserProfile.objects.create(user=self.user)

            # Obtaining JWT access token for the test user
            response = self.client.post(reverse('token_obtain_pair'), {'username': 'testuser', 'password': 'testpassword'})
            self.access_token = response.data['access']

        def test_authentication_required(self):
            url = reverse('images-list')
            response = self.client.get(url)

            # Checks if the response status code is 401 Unauthorized
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

            # Setting JWT token in the request headers and retrying the request
            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
            response = self.client.get(url)

            # Checks if the response status code is not 401 Unauthorized after setting the JWT token
            self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ImageExpirationTest(APITestCase):

        def setUp(self):
            self.user = User.objects.create_user(
                username="testuser",
                email="test@example.com",
                password="testpassword"
            )
            # Set up a temporary directory for media files during tests
            settings.MEDIA_ROOT = tempfile.mkdtemp()
            self.tier = Tier.objects.create(name='Custom Tier', thumbnail_sizes='200')
            self.user_profile = UserProfile.objects.create(user=self.user)

            # Obtaining JWT access token for the test user
            response = self.client.post(reverse('token_obtain_pair'), {'username': 'testuser', 'password': 'testpassword'})
            self.access_token = response.data['access']

            # Set up an UploadedImage with an expiration time
            image_data = b"dummy_image_data"
            image_exp_file = SimpleUploadedFile("test_image_exp.png", image_data, content_type="image/png")  # Creates an image for 'image_exp' attribute
            self.uploaded_image = UploadedImage(user=self.user, user_profile=self.user_profile)
            self.uploaded_image.image_exp.save("test_image_exp.png", image_exp_file)  # Saves the image_exp_file to the 'image_exp' attribute
            self.uploaded_image.save()  # Saves the updated UploadedImage instance
            self.expiration_time = 300
            ExpirationTime.objects.create(user=self.user, expiration_time=self.expiration_time)
        def test_image_expiration(self):
            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

            # Get the image link before the expiration time
            url = reverse('serve_expiring_image', kwargs={
                'image_id': self.uploaded_image.id,
                'expiration_timestamp': timezone.now().timestamp() + self.expiration_time - 10
            })
            response = self.client.get(url)
            self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)

            # Get the image link after the expiration time
            url = reverse('serve_expiring_image', kwargs={
                'image_id': self.uploaded_image.id,
                'expiration_timestamp': timezone.now().timestamp() - 10
            })
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        def tearDown(self):
            # Clean up the temporary directory for media files after tests
            shutil.rmtree(settings.MEDIA_ROOT)


class TestTierModelValidation(unittest.TestCase):
    def test_thumbnail_sizes_validation(self):
        # Test with valid values
        valid_sizes = ['200', '400']
        for size in valid_sizes:
            tier = Tier(name='test', thumbnail_sizes=size)
            try:
                tier.full_clean()
            except ValidationError:
                self.fail(f'{size} should be a valid value for thumbnail_sizes')
        
        # Test with invalid values
        invalid_sizes = ['100', '300', '500']
        for size in invalid_sizes:
            tier = Tier(name='test', thumbnail_sizes=size)
            with self.assertRaises(ValidationError):
                tier.full_clean()





