from django.test import Client, TestCase
from django.contrib.auth.models import User

class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_login_view_uses_correct_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_redirects_to_home_view_for_authenticated_users(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get('/login/')
        self.assertRedirects(response, '/home/')

    def test_login_view_success(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'password'})
        self.assertRedirects(response, '/home/')
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_failure(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertTemplateUsed(response, 'login.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)
