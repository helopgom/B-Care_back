from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class BaseTestCase(APITestCase):
    """
    Base class for tests with common setup and utility methods.
    """

    def setUp(self):
        """
        Common setup for all tests.
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.client.force_authenticate(user=self.user)

        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

        self.registration_data = {
            'username': 'newuser',
            'password': 'newpassword123',
            'name': 'New User',
            'birth_date': '1990-01-01',
            'phone': '1234567890'
        }

        self.invalid_registration_data = {
            'username': '',
            'password': 'short',
            'name': '',
            'birth_date': '',
            'phone': ''
        }

    def authenticate_user(self):
        """
        Authenticate the test client with the created user.
        """
        self.client.force_authenticate(user=self.user)


class UserRegistrationTestCase(BaseTestCase):

    def test_register_user(self):
        """
        Given valid user data
        When registering a new user
        Then the user should be created
        And a 201 status code should be returned
        """
        response = self.client.post(self.register_url, self.registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # Se espera un nuevo usuario creado
        self.assertEqual(User.objects.get(username='newuser').username, 'newuser')

    def test_register_user_with_invalid_data(self):
        """
        Given invalid user data
        When registering a new user
        Then the user should not be created
        And a 400 status code should be returned
        """
        response = self.client.post(self.register_url, self.invalid_registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)  # No debe haberse creado ningún usuario adicional


class UserAuthTestCase(BaseTestCase):

    def test_login_user(self):
        """
        Given valid login credentials
        When logging in
        Then a token should be returned
        And a 200 status code should be returned
        """
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'password123'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_user_with_invalid_credentials(self):
        """
        Given invalid login credentials
        When logging in
        Then a token should not be returned
        And a 400 status code should be returned
        """
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'wrongpassword'},
                                    format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
class UserLogoutTestCase(BaseTestCase):

    def test_logout_user(self):
        """
        Given an authenticated user
        When logging out
        Then the token should be deleted
        And a 200 status code should be returned
        """
        # Crear un token para el usuario
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')  # Autenticar con el token
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Token deleted")

    def test_logout_user_with_invalid_token(self):
        """
        Given an invalid token
        When logging out
        Then a 404 status code should be returned
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token invalidtoken123')
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["message"], "Token not found")

class UserProfileTestCase(BaseTestCase):

    def test_get_user_profile(self):
        """
        Given an authenticated user
        When retrieving user profile
        Then the user's profile should be returned
        And a 200 status code should be returned
        """
        url = reverse('userprofile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_profile_without_authentication(self):
        """
        Given no authentication
        When retrieving user profile
        Then a 401 status code should be returned
        """
        self.client.logout()  # Desautentica al usuario
        url = reverse('userprofile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)