from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm


def send_welcome_resources_email(user):
    """
    Helper function to send program- and resource-related information
    to newly registered users via email.
    """
    subject = "Welcome to NextGen University – Your Program Resources"

    lines = [
        f"Hi {user.username},",
        "",
        "Thank you for registering at NextGen University.",
        "Here are some useful resources to get you started:",
        "",
        "- Programs overview: https://example.com/programs",
        "- Admissions information: https://example.com/admissions",
        "- Contact an academic advisor: https://example.com/contact",
        "",
        "Best regards,",
        "NextGen University Team",
    ]

    message = "\n".join(lines)

    if not user.email:
        return

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
            return redirect("/")
    else:  # Not a POST
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        print("IN LOGIN")
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")

