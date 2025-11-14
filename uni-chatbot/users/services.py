from pages.models import Program

def enroll_user_in_program(user, program: Program):
    print("Hello from services.py", user.username, program.name)
