from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
from .service import send
from .models import Profile
from .forms import UserRegistrationForm, ProfileForm


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
        return redirect('homepage')
        



class ProfileView(TemplateView):
    template_name = "profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not Profile.objects.filter(user=request.user).exists():
            return redirect(reverse("edit_profile"))
        context = {
            'selected_user': request.user
        }
        return render(request, self.template_name, context)

    def user_profile(request, username):
        user = User.objects.get(username=username)
        context = {
        'selected_user': request.user
        }
        return render(request, 'profile.html', context)

class EditProfileView(TemplateView):
    template_name = "edit_profile.html"

    def dispatch(self, request, *args, **kwargs):
        form = ProfileForm(instance=self.get_profile(request.user))
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=self.get_profile(request.user))
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request, u"Профиль успешно обновлен!")
                return redirect(reverse("profile"))
        return render(request, self.template_name, {'form': form})

    def get_profile(self, user):
        try:
            return user.profile
        except:
            return None