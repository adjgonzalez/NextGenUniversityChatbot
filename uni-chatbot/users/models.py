# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from pages.models import Program


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    program = models.ForeignKey(
        Program, on_delete=models.SET_NULL, null=True, blank=True
    )
    enrolled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s profile"
