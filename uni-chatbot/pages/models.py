# Create your models here.
from django.db import models


class ProgramType(models.Model):
    name = models.CharField(
        max_length=50, unique=True
    )  # e.g., Undergraduate, Graduate, Online

    def __str__(self):
        return self.name


class Program(models.Model):
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
