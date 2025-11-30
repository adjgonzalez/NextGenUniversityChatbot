from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm


def send_welcome_resources_email(user):
    if not user.email:
        return

    subject = "Welcome to NextGen University – Your Program Resources"
    message = (
        f"Hi {user.username},\n\n"
        "Thank you for registering to NextGen University.\n"
        "Here are some useful resources to get you started:\n\n"
        "- Programs overview: https://example.com/programs\n"
        "- Admissions information: https://example.com/admissions\n"
        "- Contact an academic advisor: https://example.com/contact\n\n"
        "Best regards,\n"
        "NextGen University Team"
    )

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_welcome_resources_email(user)
            login(request, user)
            return redirect("pages:index")  # Use named URL for robustness
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        print("IN LOGIN")
        if form.is_valid():
            login(request, form.get_user())
            return redirect("pages:index")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("pages:index")
