from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class SuccessView(TemplateView):
    template_name = "success.html"
# def password_reset(request):
#     send_mail('Сброс пароля', 'Перейдите по ссылке для сброса пароля', settings.EMAIL_HOST_USER, ['user.email'])
