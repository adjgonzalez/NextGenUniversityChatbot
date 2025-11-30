from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from .models import AnonymousFeedback, Feedback


class FeedbackModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="teststudent", password="password123"
        )

    def test_feedback_creation(self):
        feedback = Feedback.objects.create(
            user=self.user,
            type=settings.FEEDBACK_CHOICES[0][0],
            message="The login button is broken",
        )
        self.assertEqual(feedback.message, "The login button is broken")
        self.assertEqual(feedback.user.username, "teststudent")
        self.assertEqual(str(feedback), "The login button is broken")

    def test_anonymous_feedback_creation(self):
        feedback = AnonymousFeedback.objects.create(
            type=settings.FEEDBACK_CHOICES[0][0], message="The visuals are blurry"
        )
        self.assertEqual(feedback.message, "The visuals are blurry")
        self.assertTrue(feedback.time)


class FeedbackViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="teststudent", password="password123"
        )
        self.url = reverse("feedback_form")
        # Use a valid type from your settings
        self.valid_type = settings.FEEDBACK_CHOICES[0][0]

    def test_feedback_page_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "feedback/feedback_form.html")

    def test_anonymous_submission(self):
        data = {"type": self.valid_type, "message": "Anonymous feedback test"}
        response = self.client.post(self.url, data, follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(AnonymousFeedback.objects.count(), 1)
        self.assertEqual(Feedback.objects.count(), 0)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Feedback sent successfully!" in str(m) for m in messages))

        feedback_obj = AnonymousFeedback.objects.first()
        self.assertIsNone(feedback_obj.user)

    def test_authenticated_submission(self):
        self.client.login(username="teststudent", password="password123")
        data = {"type": self.valid_type, "message": "Logged in feedback test"}
        response = self.client.post(self.url, data, follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Feedback.objects.count(), 1)
        self.assertEqual(AnonymousFeedback.objects.count(), 0)
        saved_feedback = Feedback.objects.first()
        self.assertEqual(saved_feedback.user, self.user)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Feedback sent successfully!" in str(m) for m in messages))
