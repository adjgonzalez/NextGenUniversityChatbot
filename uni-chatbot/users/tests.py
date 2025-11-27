from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class UserRegistrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.registration_url = reverse("users:register")
        self.valid_data = {
            "username": "newstudent",
            "email": "student@email.com",
            "password1": "SecurePassword123!",
            "password2": "SecurePassword123!",
        }

    def test_successful_user_registration(self):
        response = self.client.post(self.registration_url, self.valid_data)
        self.assertEqual(response.status_code, 302)  # Should redirect on success
        user_exists = User.objects.filter(username=self.valid_data["username"]).exists()
        self.assertTrue(user_exists)
        user = User.objects.get(username=self.valid_data["username"])
        self.assertEqual(user.email, self.valid_data["email"])

    def test_registration_duplicate_username(self):
        # Create a user with the same username (and some email)
        User.objects.create_user(username="existinguser", email="existing@email.com", password="testpass123")
        data = {
            "username": "existinguser",  # Already taken
            "email": "different@email.com",
            "password1": "AnotherPassword123!",
            "password2": "AnotherPassword123!",
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFormError(form, "username", "A user with that username already exists.")

    def test_registration_password_mismatch(self):
        data = {
            "username": "testuser",
            "email": "testuser@email.com",
            "password1": "Password123!",
            "password2": "DifferentPassword123!",  # Mismatch
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFormError(form, "password2", "The two password fields didn’t match.")

    def test_registration_missing_required_fields(self):
        data = {
            "username": "",
            "email": "",  # Both fields missing
            "password1": "SecurePassword123!",
            "password2": "SecurePassword123!",
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFormError(form, "username", "This field is required.")
        self.assertFormError(form, "email", "This field is required.")