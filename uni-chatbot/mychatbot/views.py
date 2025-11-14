import json

from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def send_chatbot_transcript(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            conversation = data.get("conversation", [])

            if not email:
                return JsonResponse({"success": False, "error": "Email is required"})

            # Format the conversation transcript
            transcript = "Chatbot Conversation Transcript - NextGen University\n\n"
            transcript += "Here is your conversation with our university assistant:\n\n"

            for msg in conversation:
                sender = "You" if msg["sender"] == "user" else "University Assistant"
                transcript += f"{sender}: {msg['message']}\n"

            transcript += "\n\nThank you for contacting NextGen University!\n"

            # Send email (will print to console in development)
            send_mail(
                "Your Chatbot Conversation Transcript - NextGen University",
                transcript,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            return JsonResponse({"success": True})

        except Exception as e:
            print(f"Email error: {e}")
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request method"})
