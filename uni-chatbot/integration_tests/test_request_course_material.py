import json

from django.core import mail
from django.test import TestCase
from django.urls import reverse

"Simulate a user requesting course material"


class ChatbotCourseMaterialTest(TestCase):
    def test_request_course_material_email(self):
        url = reverse("mychatbot:send_program_resources")
        payload = {
            "email": "student2@uni.edu",
            "program_slug": "mba",
            "program_name": "MBA",
        }
        response = self.client.post(
            url, data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get("success"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Your Requested Program Resources", mail.outbox[0].subject)
        self.assertIn("student2@uni.edu", mail.outbox[0].to)
        self.assertIn("MBA", mail.outbox[0].body)
