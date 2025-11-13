from django.urls import path

from . import views

app_name = "mychatbot"

urlpatterns = [
    path("send-transcript/", views.send_chatbot_transcript, name="send_transcript"),
]
