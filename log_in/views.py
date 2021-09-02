from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context['error'] = "Неправильный логин или пароль"
        return render(request, self.template_name, context)
