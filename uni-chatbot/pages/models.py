import uuid
from django.utils.text import slugify

# Create your models here.
from django.db import models


class ProgramType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=50, unique=True
    )  # e.g., Undergraduate, Graduate, Online

    def __str__(self):
        return self.name


class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    degree = models.CharField(max_length=50)  # e.g., BSc, BA, MBA, MDSc
    duration = models.CharField(max_length=50)  # e.g., '4 years', '6 months'
    description = models.TextField()
    program_type = models.ForeignKey(
        ProgramType, on_delete=models.CASCADE, related_name="programs"
    )

    # Optional fields
    routes = models.CharField(
        max_length=100, blank=True, null=True
    )  # e.g., Course-based
    enrollment_status = models.CharField(
        max_length=100, blank=True, null=True
    )  # e.g., Full-time
    campus = models.CharField(max_length=100, blank=True, null=True)

    joint_programs = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name


# Homepage model
class HomePage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page_title = models.CharField(max_length=100, default="Home")
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.CharField(max_length=250)
    hero_image = models.CharField(max_length=200) # Relative path of image
    body = models.TextField(max_length=250)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Homepage Content"
    
#Navbar model
class Navbar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu_item = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_item

#Logo model   
class Logo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_path = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_path
    
#Admissions Page Sidebar model
class AdmissionSidebarItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)  # e.g., 'undergraduate', 'graduate'
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

#Admissions Undergraduate Page model
class UndergraduateAddmissionReqPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page_title = models.CharField(max_length=100, default="Undergraduate")
    page_heading = models.CharField(max_length=255)
    admission_req_heading = models.CharField(max_length=255)
    admission_req_description = models.TextField()
    english_req_heading = models.CharField(max_length=255)
    english_req_description = models.TextField()
    language_req_exemtion_heading = models.CharField(max_length=255)
    language_req_exemtion_desc = models.TextField(
        blank=True, null=True,
        help_text="Optional text after the bullet list"
    )
    application_heading = models.CharField(max_length=255)
    application_deadlines = models.TextField()

    def __str__(self):
        return self.page_heading


class LanguageReqExemptionBullet(models.Model):
    page = models.ForeignKey(
        UndergraduateAddmissionReqPage,
        on_delete=models.CASCADE,
        related_name="exemption_bullets"
    )
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
    
#Admissions Graduate Page model
class GraduateAdmissionPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page_title = models.CharField(max_length=100, default="Graduate")
    page_heading = models.CharField(max_length=255)
    admission_req_heading = models.CharField(max_length=255)
    admission_req_desc = models.TextField()
    find_supervisor_heading = models.CharField(max_length=255)
    find_supervisor_descr = models.TextField()
    application_deadline_heading = models.CharField(max_length=255)
    application_deadline_description = models.TextField()
    fast_track_heading = models.CharField(max_length=255)
    fast_track_description = models.TextField()

    def __str__(self):
        return self.page_heading
    
class AdmissionReqBullet(models.Model):
    page = models.ForeignKey(
        GraduateAdmissionPage,
        on_delete=models.CASCADE,
        related_name="requirement_bullets"
    )
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
    
# Admissions Online Course Page model
class OnlineCoursesPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page_title = models.CharField(max_length=100, default="Online Courses")
    page_heading = models.CharField(max_length=255)
    highschool_heading = models.CharField(max_length=255)
    highschool_description = models.TextField()
    undergrad_heading = models.CharField(max_length=255)
    undergrad_description = models.TextField()
    grad_heading = models.CharField(max_length=255)
    grad_description = models.TextField()
    other_req_heading = models.CharField(max_length=255)

    def __str__(self):
        return self.page_heading


class OnlineCoursesBullet(models.Model):
    page = models.ForeignKey(
        OnlineCoursesPage,
        on_delete=models.CASCADE,
        related_name="online_bullets"
    )
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
    
# Admissions Funding Page model
class FundingPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page_title = models.CharField(max_length=100, default="Funding & Scholarships")
    financial_heading = models.CharField(max_length=255)
    financial_description = models.TextField()
    entrance_scholarship_heading = models.CharField(max_length=255)
    entrance_scholarship_description = models.TextField()
    in_program_scholarship_heading = models.CharField(max_length=255)
    in_program_scholarship_description = models.TextField()

    def __str__(self):
        return self.page_title

# Contact Page model
class ContactPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page_title = models.CharField(max_length=100, default="Contact Us")
    office_name = models.CharField(max_length=255, default="Admission Office")
    office_room = models.CharField(max_length=100, default="Room 3118")
    office_location = models.CharField(max_length=255, default="NextGen University, St. John's, Canada")
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.page_title
    
# Faculty and Department Page model
class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0, help_text="Controls accordion order")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    faculty = models.ForeignKey(
        Faculty,
        related_name="departments",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=500, unique=True, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.name)  # automatically slugify
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.faculty.name})"
    
# Department Pages model
class DepartmentPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.ForeignKey(
        'Department',
        related_name="pages",
        on_delete=models.CASCADE
    )
    page_title = models.CharField(max_length=255)
    main_heading = models.CharField(max_length=255)
    description = models.TextField()
    achievements = models.TextField(blank=True)
    advisor_name = models.CharField(max_length=255, blank=True)
    advisor_title = models.CharField(max_length=255, blank=True)
    advisor_email = models.EmailField(blank=True)
    advisor_office = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.department.name} - {self.page_title}"
