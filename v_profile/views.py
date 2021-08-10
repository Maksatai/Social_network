from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = "profile.html"
