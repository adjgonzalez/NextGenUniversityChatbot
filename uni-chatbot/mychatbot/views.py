from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse

# Home page
def index(request):
    return render(request, "home.html")


# Admissions full page view (reload-safe, works with dynamic sidebar)
def admissions_page(request, page_name="undergraduate"):
    allowed_pages = ['undergraduate', 'graduate', 'online_course', 'funding']
    if page_name not in allowed_pages:
        page_name = 'undergraduate'

    context = {
        "current_page": page_name,
        "page_title": page_name.replace("_", " ").title()  # e.g., "Undergraduate"
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