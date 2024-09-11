from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from users.models import UserProfile


class BaseTestCase(APITestCase):
    """
    Base class to set up the user and client before each test.
    """

    def setUp(self):
        """
        Sets up an authenticated user before each test.
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            name='Test User',
            birth_date='1990-01-01',
            preferences='music, movies'
        )
        self.client.force_authenticate(user=self.user)
        self.conversation_url = reverse('conversation_ia')

    def authenticate_user(self):
        """
        Authenticates the test client with the created user.
        """
        self.client.force_authenticate(user=self.user)


class ConversationAPITestCase(BaseTestCase):
    """
    Tests the conversation API.
    """

    def test_conversation_invalid_method(self):
        """
        Given an authenticated user
        When sending a GET request to the conversation endpoint
        Then a 405 status code should be returned
        And the response should indicate that the GET method is not allowed
        """
        response = self.client.get(self.conversation_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response_data = response.json()
        self.assertIn('detail', response_data)
        self.assertEqual(response_data['detail'], 'Method "GET" not allowed.')