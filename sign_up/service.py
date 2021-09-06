from django.core.mail import send_mail

def send(email_subject,email_body,user_email):
    send_mail(
    email_subject,
    email_body,
    'vfriendswels@gmail.com',
    [user_email],
    fail_silently=False,
)