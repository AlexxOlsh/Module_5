from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.views import UserListAPI, UserDetailAPI


User = get_user_model()


class UserListAPITest(TestCase):
    """Тесты для UserListAPI"""

    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin', password='admin123', email='admin@example.com'
        )
        self.client.force_authenticate(user=self.admin_user)

    def test_get_user_list_success(self):
        """Тест на успешное получение списка пользователей (для администратора)"""
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_list_unauthenticated(self):
        """Тест на получение списка пользователей без аутентификации"""
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user_success(self):
        """Тест на успешное создание пользователя (для администратора)"""
        data = {'username': 'test_user', 'password': 'test123', 'email': 'test@example.com'}
        response = self.client.post(reverse('user-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_create_user_unauthenticated(self):
        """Тест на создание пользователя без аутентификации"""
        self.client.force_authenticate(user=None)
        data = {'username': 'test_user', 'password': 'test123', 'email': 'test@example.com'}
        response = self.client.post(reverse('user-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UserDetailAPITest(TestCase):
    """Тесты для UserDetailAPI"""

    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin', password='admin123', email='admin@example.com'
        )
        self.user = User.objects.create(username='test_user', password='test123', email='test@example.com')
        self.client.force_authenticate(user=self.admin_user)

    def test_get_user_detail_success(self):
        """Тест на успешное получение информации о пользователе (для администратора)"""
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail_unauthenticated(self):
        """Тест на получение информации о пользователе без аутентификации"""
        self.client.force_authenticate(user=None)
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user_success(self):
        """Тест на успешное обновление информации о пользователе (для администратора)"""
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        data = {'username': 'updated_user', 'email': 'updated@example.com'}
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updated_user')

    def test_update_user_unauthenticated(self):
        """Тест на обновление информации о пользователе неавторизованным пользователем"""
        self.client.force_authenticate(user=None)
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        data = {'username': 'updated_user', 'email': 'updated@example.com'}
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_user_success(self):
        """Тест на успешное удаление пользователя (для администратора)"""
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(User.objects.filter(id=self.user.id).exists())

    def test_delete_user_unauthenticated(self):
        """Тест на удаление пользователя неавторизованным пользователем"""
        self.client.force_authenticate(user=None)
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_user_by_regular_user(self):
        """Тест на удаление пользователя обычным пользователем"""
        self.client.force_authenticate(user=self.user)
        url = reverse('user-detail', kwargs={'pk': self.admin_user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)