import os
import sys
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'syncflow.settings.development')

import django
django.setup()

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Brand

User = get_user_model()

class CoreTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass123', username='testuser')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create test brand
        self.brand_data = {
            'name': 'Test Brand',
            'description': 'A test brand description',
            'website': 'https://testbrand.com'
        }
        self.brand = Brand.objects.create(user=self.user, **self.brand_data)

    def test_brands_list(self):
        """Test listing brands for authenticated user"""
        url = '/api/brands/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Brand')

    def test_brands_list_empty(self):
        """Test listing brands when user has no brands"""
        Brand.objects.filter(user=self.user).delete()
        url = '/api/brands/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_brand(self):
        """Test creating a new brand"""
        url = '/api/brands/'
        new_brand_data = {
            'name': 'New Brand',
            'description': 'New brand description',
            'website': 'https://newbrand.com'
        }
        response = self.client.post(url, new_brand_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Brand')
        self.assertEqual(response.data['user'], self.user.id)

    def test_create_brand_duplicate_name(self):
        """Test creating brand with duplicate name for same user"""
        url = '/api/brands/'
        duplicate_data = {
            'name': 'Test Brand',  # Same name as existing brand
            'description': 'Duplicate brand'
        }
        response = self.client.post(url, duplicate_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_brand_detail(self):
        """Test retrieving brand details"""
        url = f'/api/brands/{self.brand.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Brand')
        self.assertEqual(response.data['description'], 'A test brand description')

    def test_brand_detail_not_found(self):
        """Test retrieving non-existent brand"""
        url = '/api/brands/999/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_brand(self):
        """Test updating brand details"""
        url = f'/api/brands/{self.brand.id}/'
        update_data = {
            'name': 'Updated Brand',
            'description': 'Updated description',
            'website': 'https://updatedbrand.com'
        }
        response = self.client.put(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Brand')
        self.assertEqual(response.data['description'], 'Updated description')

    def test_partial_update_brand(self):
        """Test partial update of brand"""
        url = f'/api/brands/{self.brand.id}/'
        update_data = {'description': 'Partially updated description'}
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Partially updated description')
        self.assertEqual(response.data['name'], 'Test Brand')  # Unchanged field

    def test_delete_brand(self):
        """Test deleting a brand"""
        url = f'/api/brands/{self.brand.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify brand is deleted
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthenticated_access(self):
        """Test that unauthenticated users cannot access brand endpoints"""
        self.client.force_authenticate(user=None)
        url = '/api/brands/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_can_only_access_own_brands(self):
        """Test that users can only access their own brands"""
        other_user = User.objects.create_user(email='other@example.com', password='testpass123')
        other_brand = Brand.objects.create(user=other_user, name='Other Brand')

        url = f'/api/brands/{other_brand.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
