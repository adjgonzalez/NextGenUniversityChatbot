from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class UserRegistrationTests(TestCase):
    """
    Test user registration functionality
    """

    def setUp(self):
        """Set up test data that runs before each test"""
        self.client = Client()
        self.registration_url = reverse("users:register")
        self.valid_data = {
            "username": "newstudent",
            "password1": "SecurePassword123!",
            "password2": "SecurePassword123!",
        }

    def test_registration_page_loads(self):
        """Test that registration page loads successfully"""
        response = self.client.get(self.registration_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")
        self.assertContains(response, "form")  # Check for form in content
        self.assertContains(response, "username")  # UserCreationForm has username field

    def test_successful_user_registration(self):
        """Test that a user can register with valid data"""
        response = self.client.post(self.registration_url, self.valid_data)

        # Should redirect after successful registration (to home page "/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

        # Check if user was created in database
        user_exists = User.objects.filter(username=self.valid_data["username"]).exists()
        self.assertTrue(user_exists)

        # Verify user details
        user = User.objects.get(username=self.valid_data["username"])
        self.assertTrue(user.check_password("SecurePassword123!"))

        # Check that user is logged in after registration
        response = self.client.get("/")
        self.assertTrue(response.context["user"].is_authenticated)

    def test_registration_duplicate_username(self):
        """Test that duplicate username registration fails"""
        # Create a user first
        User.objects.create_user(username="existinguser", password="testpass123")

        # Try to register with same username
        response = self.client.post(
            self.registration_url,
            {
                "username": "existinguser",  # Already exists
                "password1": "AnotherPassword123!",
                "password2": "AnotherPassword123!",
            },
        )

        # Should stay on registration page (200 status)
        self.assertEqual(response.status_code, 200)

        # Check that error message is displayed
        self.assertFormError(
            response, "form", "username", "A user with that username already exists."
        )

    def test_registration_password_mismatch(self):
        """Test registration fails when passwords don't match"""
        response = self.client.post(
            self.registration_url,
            {
                "username": "testuser",
                "password1": "Password123!",
                "password2": "DifferentPassword123!",  # Mismatch
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, "form", "password2", "The two password fields didn’t match."
        )

    def test_registration_weak_password(self):
        """Test registration fails with weak password"""
        response = self.client.post(
            self.registration_url,
            {
                "username": "testuser",
                "password1": "123",  # Too weak
                "password2": "123",
            },
        )

        self.assertEqual(response.status_code, 200)
        # Django should show password validation error
        self.assertIn("This password is too short.", response.content.decode())

    def test_registration_missing_required_fields(self):
        """Test registration fails when required fields are missing"""
        response = self.client.post(
            self.registration_url,
            {
                "username": "",  # Missing username
                "password1": "SecurePassword123!",
                "password2": "SecurePassword123!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "username", "This field is required.")

    def test_registration_form_instance(self):
        """Test that the correct form is used"""
        response = self.client.get(self.registration_url)
        self.assertIsInstance(response.context["form"], UserCreationForm)


class UserAuthenticationTests(TestCase):
    """Test login and logout functionality"""

    def setUp(self):
        self.client = Client()
        self.login_url = reverse("users:login")
        self.logout_url = reverse("users:logout")
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_login_page_loads(self):
        """Test that login page loads successfully"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")
        self.assertContains(response, "form")

    def test_successful_login(self):
        """Test user can login with correct credentials"""
        response = self.client.post(
            self.login_url,
            {
                "username": "testuser",
                "password": "testpass123",
            },
        )

        # Should redirect to home page after login
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

        # Check that user is logged in
        response = self.client.get("/")
        self.assertTrue(response.context["user"].is_authenticated)
        self.assertEqual(response.context["user"].username, "testuser")

    def test_login_invalid_credentials(self):
        """Test login fails with wrong credentials"""
        response = self.client.post(
            self.login_url,
            {
                "username": "testuser",
                "password": "wrongpassword",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password")

    def test_logout_functionality(self):
        """Test user can logout"""
        # Login first
        self.client.login(username="testuser", password="testpass123")

        # Verify logged in
        response = self.client.get("/")
        self.assertTrue(response.context["user"].is_authenticated)

        # Logout via POST
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

        # Verify logged out
        response = self.client.get("/")
        self.assertFalse(response.context["user"].is_authenticated)
