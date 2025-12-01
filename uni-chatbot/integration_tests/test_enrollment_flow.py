import json

from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse

from pages.models import Program, ProgramType
from users.models import UserProfile

"Integration test: User Registration → Program Enrollment → Chatbot Resource Request"

User = get_user_model()


class UserEnrollmentResourceTest(TestCase):
    def setUp(self):
        # Create a program for enrollment and resource logic
        self.program_type = ProgramType.objects.create(name="Undergraduate")
        self.program = Program.objects.create(
            name="Test Program",
            slug="test-program",
            degree="BA",
            duration="4 years",
            description="A test program for integration.",
            program_type=self.program_type,
        )

    def test_registration_enrollment_and_chatbot_resource_request(self):
        # 1. Register a new user via the view
        reg_url = reverse("users:register")
        reg_data = {
            "username": "integrationuser",
            "email": "integrationuser@mail.com",
            "password1": "SecurePass123@",
            "password2": "SecurePass123@",
        }
        response = self.client.post(reg_url, reg_data)
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username="integrationuser")
        self.assertEqual(user.email, "integrationuser@mail.com")

        # 2. Ensure a welcome mail is sent (from signal or view)
        self.assertEqual(len(mail.outbox), 1)
        welcome_subjects = [m.subject for m in mail.outbox]
        self.assertTrue(any("Welcome" in subject for subject in welcome_subjects))

        # 3. Create their UserProfile and enroll them in the program
        profile = UserProfile.objects.create(user=user)
        profile.program = self.program
        profile.save()

        # 4. Simulate chatbot requesting resources for this user/program
        chatbot_resource_url = reverse("mychatbot:send_program_resources")
        chatbot_payload = {
            "email": user.email,
            "program_slug": self.program.slug,
            "program_name": self.program.name,
        }
        response = self.client.post(
            chatbot_resource_url,
            data=json.dumps(chatbot_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["success"])

        # 5. Mail outbox should have the second message (resource email)
        self.assertEqual(len(mail.outbox), 2)
        self.assertTrue("Your Requested Program Resources" in mail.outbox[1].subject)
        self.assertIn(user.email, mail.outbox[1].to)
