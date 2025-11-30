from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Feedback, AnonymousFeedback
from django.contrib.messages import get_messages

class FeedbackModelTest(TestCase):
    def setUp(self):
        # Create a dummy user for testing
        self.user = User.objects.create_user(username='teststudent', password='password123')

    def test_feedback_creation(self):
        """Test that a logged-in user feedback is created correctly"""
        feedback = Feedback.objects.create(
            user=self.user,
            type='bug',
            message='The login button is broken'
        )
        self.assertEqual(feedback.message, 'The login button is broken')
        self.assertEqual(feedback.user.username, 'teststudent')
        # Check string representation
        self.assertEqual(str(feedback), 'The login button is broken')

    def test_anonymous_feedback_creation(self):
        """Test that anonymous feedback is created correctly"""
        feedback = AnonymousFeedback.objects.create(
            type='issue',
            message='The visuals are blurry'
        )
        self.assertEqual(feedback.message, 'The visuals are blurry')
        self.assertTrue(feedback.time) # Check that time was auto-added


class FeedbackViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teststudent', password='password123')
        
        self.url = reverse('feedback_form') 

    def test_feedback_page_loads(self):
        """Test that the page loads successfully (Status 200)"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/feedback_form.html')

    def test_anonymous_submission(self):
        """Test submitting the form properly as a guest"""
        data = {
            'type': 'bug',
            'message': 'I cannot find the admission page'
        }
        # Post the data to the URL
        response = self.client.post(self.url, data)
        
        # 1. Check status code 
        self.assertEqual(response.status_code, 200)

        # 2. Check if data was saved to the AnonymousFeedback table
        self.assertEqual(AnonymousFeedback.objects.count(), 1)
        self.assertEqual(Feedback.objects.count(), 0) 

        # 3. Check for success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Feedback sent successfully!")

    def test_authenticated_submission(self):
        """Test submitting the form as a logged-in student"""
        self.client.login(username='teststudent', password='password123')
        
        data = {
            'type': 'issue',
            'message': 'My grades are not showing'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 200)

        # Check if data was saved to the Feedback table (NOT Anonymous)
        self.assertEqual(Feedback.objects.count(), 1)
        self.assertEqual(AnonymousFeedback.objects.count(), 0)
        
        # Verify the feedback is linked to the correct user
        saved_feedback = Feedback.objects.first()
        self.assertEqual(saved_feedback.user, self.user)



