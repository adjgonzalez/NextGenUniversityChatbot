import json

from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse

"Simulate a user requesting to contact the admin via the chatbot"

User = get_user_model()


class ChatbotAdminContactTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="student1", email="student1@uni.edu", password="test123"
        )

    def test_student_contacts_admin_via_chatbot(self):
        self.client.login(username="student1", password="test123")
        contact_url = reverse("mychatbot:send_transcript")
        chat_history = [
            {"sender": "user", "message": "I need help with my account."},
            {
                "sender": "assistant",
                "message": "I'll forward this to an administrator.",
            },
        ]
        # Assume transcript sent to admin means an admin gets an email
        response = self.client.post(
            contact_url,
            data=json.dumps(
                {
                    "email": "nextgen@uni.edu",
                    "conversation": chat_history,
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get("success"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Chatbot Conversation Transcript", mail.outbox[0].subject)
        self.assertIn("nextgen@uni.edu", mail.outbox[0].to)
        self.assertIn("I need help with my account.", mail.outbox[0].body)
