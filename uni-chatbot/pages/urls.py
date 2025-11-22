from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.index, name="index"),
    path("admissions/", views.admissions_page, name="admissions"),
    path("admissions/<str:page_name>/", views.admissions_page, name="admissions_page"),
    path("", include("mychatbot.urls")),
    path(
        "admissions/load/<str:page_name>/",
        views.load_sidebar_content,
        name="load_sidebar_content",
    ),  # AJAX
    path("contact/", views.contact, name="contact"),
    path("faculty/", views.faculty, name="faculty"),
    path("programs/", views.programs, name="programs"),
    path("apply_now/", views.apply_now, name="apply_now"),
    path(
        "programs/<slug:program_slug>/", views.programs_detail, name="program_detail"
    ),  # ,path("programs_detail1/", views.programs_detail1, name="programs_detail1"),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)