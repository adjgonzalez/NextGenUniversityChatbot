from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("", include("pages.urls")),
    path("", include("feedback.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("", include("mychatbot.urls")),

    # ------ Password Reset paths ------
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="users/password_reset.html",
        email_template_name="registration/password_reset_email.html"
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="users/password_reset_done.html"
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="users/password_reset_confirm.html"
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name="users/password_reset_complete.html"
    ), name='password_reset_complete'),
]