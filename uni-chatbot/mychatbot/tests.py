import json

from django.core import mail
from django.test import TestCase
from django.urls import reverse


class ChatbotTests(TestCase):
    def test_send_chatbot_transcript_success(self):
        url = reverse("mychatbot:send_transcript")
        data = {
            "email": "student@example.com",
            "conversation": [
                {"sender": "assistant", "message": "Welcome!"},
                {"sender": "user", "message": "Tell me about undergraduate programs."},
                {
                    "sender": "assistant",
                    "message": "We offer several undergraduate programs.",
                },
            ],
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        resp_json = response.json()
        self.assertTrue(resp_json.get("success"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Chatbot Conversation Transcript", mail.outbox[0].subject)
        self.assertIn("student@example.com", mail.outbox[0].to)

    def test_send_chatbot_transcript_missing_email(self):
        url = reverse("mychatbot:send_transcript")
        data = {
            "conversation": [
                {"sender": "assistant", "message": "Welcome!"},
            ]
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json().get("success"))
        self.assertIn("Email is required", response.json().get("error", ""))

    def test_send_chatbot_transcript_invalid_method(self):
        url = reverse("mychatbot:send_transcript")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json().get("success"))
        self.assertIn("Invalid request method", response.json().get("error", ""))

    def test_send_program_resources_success(self):
        url = reverse("mychatbot:send_program_resources")
        data = {
            "email": "resourceuser@example.com",
            "program_slug": "bsc-computer-science",
            "program_name": "BSc Computer Science",
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        resp_json = response.json()
        self.assertTrue(resp_json.get("success"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Your Requested Program Resources", mail.outbox[0].subject)
        self.assertIn("resourceuser@example.com", mail.outbox[0].to)

    def test_send_program_resources_missing_email(self):
        url = reverse("mychatbot:send_program_resources")
        data = {"program_slug": "mba", "program_name": "MBA"}
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        resp_json = response.json()
        self.assertFalse(resp_json.get("success"))
        self.assertIn("Email is required", resp_json.get("error", ""))

    def test_send_program_resources_invalid_method(self):
        url = reverse("mychatbot:send_program_resources")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json().get("success"))
        self.assertIn("Invalid request method", response.json().get("error", ""))
