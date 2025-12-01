from django.test import TestCase

from pages.models import Program, ProgramType

"Simulate user being redirected to a program by the chatbot"


class ChatbotRedirectProgramTest(TestCase):
    def setUp(self):
        pt = ProgramType.objects.create(name="Graduate")
        Program.objects.create(
            name="MBA",
            slug="mba",
            program_type=pt,
            degree="MBA",
            duration="2 years",
            description="MBA program desc",
        )

    def test_redirect_to_program_info(self):
        program_info_url = "/programs/mba/"
        response = self.client.get(program_info_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"MBA", response.content)
        self.assertIn(b"description", response.content)
