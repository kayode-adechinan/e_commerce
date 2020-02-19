from django.conf import settings
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


def send_mail(to, body): 
    subject = "Confirmation"
    from_email = settings.EMAIL_HOST_USER
    to = [to]
    text_content = body
    html_content = body
    msg = EmailMultiAlternatives(subject, strip_tags(text_content), from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
 