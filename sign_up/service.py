from django.core.mail import send_mail

def send(user_email):
    send_mail(
    'Регистрация',
    'Для активации аккаунта перейдите по ссылке',
    'vfriendswels@gmail.com',
    [user_email],
    fail_silently=False,
)
