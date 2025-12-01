from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from feedback.models import Feedback

"Integration test: User Login → Send Feedback"

User = get_user_model()


class FeedbackIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="feedtest@example.com", password="feedtest123"
        )

    def test_feedback_submission_and_confirmation(self):
        # Student logs in
        self.client.login(username="test", password="feedtest123")
        feedback_url = reverse("feedback_form")

        # Student submits feedback
        valid_type = settings.FEEDBACK_CHOICES[0][0]
        response = self.client.post(
            feedback_url,
            {"type": valid_type, "message": "Cannot see my grades"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

        # Check feedback is saved to DB and linked to user
        self.assertEqual(Feedback.objects.filter(user=self.user).count(), 1)

        # Check for confirmation message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Feedback sent successfully!" in str(m) for m in messages))
