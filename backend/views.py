from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def email_view(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        subject = "Subject for your email"
        message = body.get("message")
        from_email = body.get("from_email")
        recipient_list = ["matthewklein345@gmail.com"]  # Replace with the recipient's email address
        if message and from_email:
            # send_mail(subject, message, from_email, recipient_list)
            return HttpResponse("Email sent successfully!", status=200)
        else:
            return HttpResponse("Please provide a message and sender's email address.", status=400)
    else:
        return HttpResponse("Invalid request method. Use POST.", status=405)
