import json

from django.core import mail
from django.test import TestCase
from django.urls import reverse

"Simulate a user requesting the chatbot transcripts"


class ChatbotTranscriptIntegrationTest(TestCase):
    def test_full_transcript_email_sent(self):
        url = reverse("mychatbot:send_transcript")
        conversation = [
            {"sender": "assistant", "message": "Welcome!"},
            {"sender": "user", "message": "Tell me about admissions."},
            {"sender": "assistant", "message": "Admissions are open now!"},
        ]
        response = self.client.post(
            url,
            data=json.dumps(
                {"email": "student@open.edu", "conversation": conversation}
            ),
            content_type="application/json",
        )

        # Check HTTP response
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get("success"))

        # Check that the email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Your Chatbot Conversation Transcript", mail.outbox[0].subject)
        self.assertIn("student@open.edu", mail.outbox[0].to)

        # Check that all conversation messages are present in email body
        for msg in conversation:
            self.assertIn(msg["message"], mail.outbox[0].body)
