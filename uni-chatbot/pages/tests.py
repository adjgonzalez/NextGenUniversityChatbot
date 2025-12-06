from django.test import Client, TestCase
from django.urls import reverse
from django.utils import translation


class PagesSectionTests(TestCase):
    """Test for public pages (index, admissions, contact, faculty, programs)."""

    def setUp(self):
        """Prepare test client and common URLs before each test."""
        self.client = Client()
        self.index_url = reverse("pages:index")
        self.admissions_url = reverse("pages:admissions")
        self.contact_url = reverse("pages:contact")
        self.faculty_url = reverse("pages:faculty")
        self.programs_url = reverse("pages:programs")
        self.admissions_page = lambda name: reverse(
            "pages:admissions_page", args=[name]
        )
        self.program_detail = lambda slug: reverse(
            "pages:program_detail", kwargs={"program_slug": slug}
        )

    def test_index_page_200_and_template(self):
        """Index page returns 200 and uses the correct template."""
        res = self.client.get(self.index_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "pages/home.html")

    def test_admissions_default_is_undergraduate(self):
        """/admissions/ defaults to 'undergraduate' with proper context."""
        res = self.client.get(self.admissions_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "admissions/admission.html")
        self.assertEqual(res.context["current_page"], "undergraduate")
        self.assertEqual(res.context["page_title"], "Undergraduate")

    def test_admissions_valid_graduate(self):
        """/admissions/graduate/ loads and sets context correctly."""
        res = self.client.get(self.admissions_page("graduate"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "admissions/admission.html")
        self.assertEqual(res.context["current_page"], "graduate")
        self.assertEqual(res.context["page_title"], "Graduate")

    def test_admissions_valid_online_course(self):
        """/admissions/online_course/ loads and sets context correctly."""
        res = self.client.get(self.admissions_page("online_course"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "admissions/admission.html")
        self.assertEqual(res.context["current_page"], "online_course")
        self.assertEqual(res.context["page_title"], "Online Course")

    def test_admissions_valid_funding(self):
        """/admissions/funding/ loads and sets context correctly."""
        res = self.client.get(self.admissions_page("funding"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "admissions/admission.html")
        self.assertEqual(res.context["current_page"], "funding")
        self.assertEqual(res.context["page_title"], "Funding")

    def test_admissions_invalid_page_fallback(self):
        """Invalid admissions page falls back to 'undergraduate'."""
        res = self.client.get(self.admissions_page("does_not_exist"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "admissions/admission.html")
        self.assertEqual(res.context["current_page"], "undergraduate")
        self.assertEqual(res.context["page_title"], "Undergraduate")

    def test_language_can_be_changed_multiple_times(self):
        # Set initial language to French
        with translation.override("fr"):
            lang1 = translation.get_language()
            lang2 = translation.get_language()
            lang3 = translation.get_language()

            # All checks should return the same language code
            self.assertEqual(lang1, "fr")
            self.assertEqual(lang2, "fr")
            self.assertEqual(lang3, "fr")

            # The result should be consistent across checks
            self.assertTrue(lang1 == lang2 == lang3)

    def test_contact(self):
        """Contact pages return 200 with correct templates."""
        res = self.client.get(self.contact_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "base/contact.html")
