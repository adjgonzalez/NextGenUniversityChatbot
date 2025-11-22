import json
from pages.models import Program
from users.models import UserProfile
from django.core.mail import send_mail
from django.conf import settings


def enroll_user_in_program(user, program: dict):
    prog: Program = Program.objects.get(name=program["name"])
    
    try:
        profile = UserProfile.objects.get(user=user)             
        profile.program = prog
        profile.save()

        email = "azometapania@mun.ca"
        transcript = f"Dear Application Commitee,\n\nNew incoming application has been received.\n\nData:\n\n\tName: {user.username}\n\tProgram: {program["name"]}\n"
        subject = program["name"] + " Application Confirmation - NextGen University"

        # Send email (will print to console in development)
        send_mail(
            subject,
            transcript,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

    except UserProfile.DoesNotExist:
        print("No profile found for user", user.username)
        return
    
    except Exception as e:
        print("Something went wrong for application")
        return e

