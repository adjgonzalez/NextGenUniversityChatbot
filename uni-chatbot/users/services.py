from pages.models import Program
from users.models import UserProfile

def enroll_user_in_program(user, program: dict):
    prog: Program = Program.objects.get(name=program["name"])

    try:
        profile = UserProfile.objects.get(user=user)
        print("Program to enroll to:", prog)    
        print("Profile found", profile, profile.program)
        print("Hello from services.py", user.username, program["name"])
        profile.program = prog
        profile.save()

    except UserProfile.DoesNotExist:
        print("No profile found for user", user.username)
        return
