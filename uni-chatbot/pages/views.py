import json

import django.conf
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from pages.models import Program
from users.models import UserProfile


# Home page
def index(request):
    print(django.conf.settings.DEBUG)
    return render(request, "pages/home.html")


# Admissions full page view (reload-safe, works with dynamic sidebar)
def admissions_page(request, page_name="undergraduate"):
    allowed_pages = ["undergraduate", "graduate", "online_course", "funding"]
    if page_name not in allowed_pages:
        page_name = "undergraduate"

    context = {
        "current_page": page_name,
        "page_title": page_name.replace("_", " ").title(),  # e.g., "Undergraduate"
    }
    return render(request, "admissions/admission.html", context)


# Load sidebar content dynamically via AJAX
def load_sidebar_content(request, page_name):
    template_map = {
        "undergraduate": "admissions/undergraduate.html",
        "graduate": "admissions/graduate.html",
        "online_course": "admissions/online_course.html",
        "funding": "admissions/funding.html",
    }

    template_name = template_map.get(page_name)
    if template_name:
        html = render_to_string(template_name, request=request)
        return JsonResponse({"html": html})
    return JsonResponse({"html": "<p>Page not found</p>"}, status=404)


# Contact page
def contact(request):
    return render(request, "base/contact.html")


# Faculty page
def faculty(request):
    return render(request, "base/faculty.html")


def programs(request):
    """Displays all programs with categories"""
    programs = Program.objects.all()
    categories = set(program.program_type.name for program in programs)

    return render(
        request, "base/programs.html", {"programs": programs, "categories": categories}
    )


def programs_detail(request, program_slug):
    """Loads program information based on slug

    Input:
        program_slug: slug to search program from
    """
    program = get_object_or_404(Program, slug=program_slug)
    category = program.program_type.name

    # Create dictionary of program to handle JSON serialization
    program_dict = {
        "id": str(program.id),
        "name": program.name,
        "slug": program.slug,
        "degree": program.degree,
        "duration": program.duration,
        "description": program.description,
        "routes": program.routes,
        "enrollment_status": program.enrollment_status,
        "campus": program.campus,
        "joint_programs": program.joint_programs,
    }
    # Create JSON object from dictionary
    program_json = json.dumps(program_dict, ensure_ascii=False)

    return render(
        request,
        "base/programs_detail1.html",
        {"program": program, "program_json": program_json, "category": category},
    )


def apply_now(request):
    """
    Handles user applications to programs

    Input:
        Request: POST request with program data
    """
    if not request.user.is_authenticated:
        return JsonResponse({"message": "You must be logged in"}, status=401)

    if request.method == "POST":
        try:
            # Get program that user wants to apply for
            data = json.loads(request.body)
            program = data.get("program")
            prog: Program = Program.objects.get(name=program["name"])

            # Have to update user to reflect chosen program
            profile = UserProfile.objects.get(user=request.user)
            profile.program = prog
            profile.save()

            # Contact admin about new application
            _contact_admin(profile, program)

            # Confirm application to user
            _contact_user(profile, program)

            return JsonResponse({"message": "Application successful"})

        except UserProfile.DoesNotExist:
            print("No profile found for user", request.user.username)
            return
        except Exception:
            return JsonResponse(
                {"message": "Something went wrong. Application Cancelled"}, status=500
            )
    return JsonResponse({"success": False, "error": "Invalid request method"})


def _contact_admin(profile: UserProfile, program: dict):
    """
    Contacts admin about new application
    """
    email = "admin@nextgenuniversity.com"
    transcript = f"Dear Application Commitee,\n\nNew incoming application has been received.\n\nData:\n\n\tName: {profile.user.username}\n\tProgram: {program['name']}\n"
    subject = program["name"] + " Application Confirmation - NextGen University"

    # Send email (will print to console in development)
    send_mail(
        subject,
        transcript,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
    return JsonResponse({"message": "Application successful"})


def _contact_user(profile: UserProfile, program: dict):
    """
    Contacts user to confirm application receipt
    """
    email = profile.user.email
    transcript = f"Dear {profile.user.username},\n\nYour application for {program['name']} has been received.\n\nWe will review your application and get back to you shortly.\n\nThank you for choosing NextGen University!\n"
    subject = program["name"] + " Application Received - NextGen University"

    # Send email (will print to console in development)
    send_mail(
        subject,
        transcript,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
    return JsonResponse({"message": "Application successful"})
