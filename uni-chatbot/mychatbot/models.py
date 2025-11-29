from django.db import models

class Student(models.Model):
    email = models.EmailField(unique=True)
    enrolled = models.BooleanField(default=True)
    name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.name or self.email} (Enrolled: {self.enrolled})"