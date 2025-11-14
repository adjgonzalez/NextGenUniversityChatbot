from django.test import Client, TestCase
from django.urls import reverse


class PagesSectionTests(TestCase):
    """Test for public pages (index, admissions, contact, faculty, programs)."""

    def setUp(self):
        """Prepare test client and common URLs before each test."""
        self.client = Client()
        self.index_url = reverse("mychatbot:index")
        self.admissions_url = reverse("mychatbot:admissions")
        self.contact_url = reverse("mychatbot:contact")
        self.faculty_url = reverse("mychatbot:faculty")
        self.programs_url = reverse("mychatbot:programs")
        self.admissions_page = lambda name: reverse(
            "mychatbot:admissions_page", args=[name]
        )
        self.program_detail = lambda slug: reverse(
            "mychatbot:program_detail", kwargs={"program_slug": slug}
        )

    def test_index_page_200_and_template(self):
        """Index page returns 200 and uses the correct template."""
        res = self.client.get(self.index_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "home.html")

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

    def test_contact_and_faculty_pages(self):
        """Contact and Faculty pages return 200 with correct templates."""
        res = self.client.get(self.contact_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "base/contact.html")

        res = self.client.get(self.faculty_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "base/faculty.html")
