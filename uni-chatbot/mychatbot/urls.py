from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "mychatbot"

urlpatterns = [
    path("send-transcript/", views.send_chatbot_transcript, name="send_transcript"),
    path(
        "send-program-resources/",
        views.send_program_resources,
        name="send_program_resources",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
