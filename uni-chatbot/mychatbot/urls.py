from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "mychatbot"

urlpatterns = [
    path("send-transcript/", views.send_chatbot_transcript, name="send_transcript"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)