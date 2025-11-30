from django.contrib.auth import get_user_model
from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse

# Import Program and ProgramType from the correct location: pages.models
from pages.models import Program, ProgramType

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
        self.assertEqual(response.status_code, 302)  # Redirect on success
        user_exists = User.objects.filter(username=self.valid_data["username"]).exists()
        self.assertTrue(user_exists)
        user = User.objects.get(username=self.valid_data["username"])
        self.assertEqual(user.email, self.valid_data["email"])

    def test_registration_duplicate_username(self):
        User.objects.create_user(
            username="existinguser", email="existing@email.com", password="testpass123"
        )
        data = {
            "username": "existinguser",  # Already taken
            "email": "different@email.com",
            "password1": "AnotherPassword123!",
            "password2": "AnotherPassword123!",
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFormError(
            form, "username", "A user with that username already exists."
        )

    def test_registration_password_mismatch(self):
        data = {
            "username": "testuser",
            "email": "testuser@email.com",
            "password1": "Password123!",
            "password2": "DifferentPassword123!",
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFormError(form, "password2", "The two password fields didn’t match.")

    def test_registration_missing_required_fields(self):
        data = {
            "username": "",
            "email": "",
            "password1": "SecurePassword123!",
            "password2": "SecurePassword123!",
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFormError(form, "username", "This field is required.")
        self.assertFormError(form, "email", "This field is required.")


class UserAuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "existent"
        self.password = "topSecret123"
        self.email = "existent@email.com"
        User.objects.create_user(
            username=self.username, email=self.email, password=self.password
        )

    def test_successful_login(self):
        response = self.client.post(
            reverse("users:login"),
            {"username": self.username, "password": self.password},
        )
        self.assertEqual(response.status_code, 302)

    def test_failed_login_wrong_password(self):
        response = self.client.post(
            reverse("users:login"),
            {"username": self.username, "password": "wrongPassword"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password.")

    def test_failed_login_no_user(self):
        response = self.client.post(
            reverse("users:login"),
            {"username": "missinguser", "password": "irrelevant"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password.")

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("users:logout"))
        self.assertEqual(response.status_code, 302)
        # After logout, session should not contain user ID
        response = self.client.get(reverse("pages:index"))
        self.assertNotIn("_auth_user_id", self.client.session)


class UserPasswordResetTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.email = "resetme@abc.com"
        self.user = User.objects.create_user(
            username="userreset", email=self.email, password="passpass"
        )

    def test_password_reset_email_sent(self):
        response = self.client.post(reverse("password_reset"), {"email": self.email})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn(self.email, mail.outbox[0].to)


class UserEnrollmentTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "enrollme"
        self.password = "secure123"
        self.user = User.objects.create_user(
            username=self.username, email="enroll@abc.com", password=self.password
        )
        self.client.login(username=self.username, password=self.password)
        self.program_type = ProgramType.objects.create(name="Undergraduate")
        # Create Program instance
        self.program = Program.objects.create(
            name="Some Program",
            slug="some-program",
            degree="BA",
            duration="4 years",
            description="Sample Program for testing.",
            program_type=self.program_type,
        )

    def test_apply_now_sends_email(self):
        import json

        payload = json.dumps({"program": {"name": self.program.name}})
        response = self.client.post(
            reverse("pages:apply_now"), data=payload, content_type="application/json"
        )
        print(response.status_code, response.content)  # For debug
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Application successful", response.content)
        self.assertTrue(len(mail.outbox) > 0)
