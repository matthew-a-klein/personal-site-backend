from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json
from .import settings

@csrf_exempt
def email_view(request):
    if request.method == 'POST':
        # Get the info we need from the POST request
        body = json.loads(request.body.decode('utf-8'))
        from_name=body.get("from_name")
        message = body.get("message")
        reply_email = body.get("from_email")

        if message  and from_name and reply_email:
            email_message(from_name, reply_email, message)
            return HttpResponse("Email sent successfully!", status=200)
        else:
            return HttpResponse("Please provide a message and sender's email address.", status=400)
    else:
        return HttpResponse("Invalid request method. Use POST.", status=405)
    
def email_message(from_name, reply_email, message):
    html_message = generate_html(from_name, reply_email, message)
    send_mail(
    subject=f"message from {from_name} via {settings.WEBSITE_NAME}",
    message="",
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=[settings.EMAIL_RECIPIENT],
    fail_silently=False,
    html_message=html_message, 
   
    )
    
def generate_html(from_name, reply_email, message):

    html_content = f"<h3>You recieved an email from {from_name} at {reply_email}</h3>"
    html_content += f"<p>{message}</p>"
    return html_content
