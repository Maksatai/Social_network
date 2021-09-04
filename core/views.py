from django.shortcuts import render
from django.views.generic import TemplateView
from sign_up.service import send

class HomeView(TemplateView):
    template_name = 'home.html'

class SuccessView(TemplateView):
    template_name = "success.html"

def password_reset(request):
    body = "Сброс пароля"
    subject = "Перейдите по ссылке для сброса пароля"
    send(body,subject,request.email)
    return render(request,"reset_succ.html")
