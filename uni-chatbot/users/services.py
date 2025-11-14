from pages.models import Program

def enroll_user_in_program(user, program: dict):
    print("Hello from services.py", user.username, program["name"])
