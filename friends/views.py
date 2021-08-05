from django.shortcuts import render
from django.views.generic import TemplateView

class FriendsView(TemplateView):
    template_name = 'friends.html'

