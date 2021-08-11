from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import TemplateView

class SignupView(TemplateView):
    template_name = "signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, first_name, last_name, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)