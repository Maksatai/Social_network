from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import UserRegistrationForm
from django.core.mail import EmailMessage
from .service import send
# from django.contrib import messages

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator

class SignupView(TemplateView):
    template_name = "signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
            #Create a new user object but avoid saving it yet
                new_user = user_form.save(commit=False)
            # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])
            #Save the User object
                new_user.is_active=False
                new_user.save()
                user_new = new_user
                uidb64 = urlsafe_base64_encode(force_bytes(new_user.pk))

                domain = get_current_site(request).domain
                link = reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(new_user)})
                activate_url = "http://" + domain+ link

                subject="Регистрация"
                body="Уважаемый " + new_user.username + " Для активации аккаунта перейдите по ссылке\n"+ activate_url
                send(subject,body,new_user.email)
                return redirect("success")
        else:
            user_form = UserRegistrationForm()
        return render(request, self.template_name, {'user_form': user_form})

class VerificationView(TemplateView):
    def get(self, request, uidb64, token):

        # request.user.is_active=True
        # request.user.save()
        return redirect('home')
        
