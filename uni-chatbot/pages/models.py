import uuid
from django.db import models

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
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.CharField(max_length=250, blank=True)
    hero_image = models.CharField(max_length=200, blank=True,) # Relative path of image
    body = models.TextField(max_length=250, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Homepage Content"
    
#Navbar model
class Navbar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu_item = models.CharField(max_length=50, blank= True)
    url = models.CharField(max_length=100, blank=True)
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
