from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'base.html'

def homepage(request):
    return render(request, 'base.html')
