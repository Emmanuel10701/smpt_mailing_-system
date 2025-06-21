from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def send_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            subject = data.get("subject")
            message = data.get("message")
            from_email = data.get("from_email")
            recipient_list = data.get("to", ["youremail@example.com"])  # Change default

            if not subject or not message or not from_email:
                return JsonResponse({"error": "Missing fields"}, status=400)

            send_mail(subject, message, from_email, recipient_list)
            return JsonResponse({"success": True})

        except BadHeaderError:
            return JsonResponse({"error": "Invalid header found."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "POST method required"}, status=405)
