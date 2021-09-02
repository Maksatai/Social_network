from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = "profile.html"

    def user_profile(request, username):
        user = User.objects.get(username=username)
        context = {
        'selected_user': request.user
        }

        return render(request, 'profile.html', context)

# class EditProfileView(TemplateView):
#     template_name = "edit_profile.html"

    # def dispatch(self, request, *args, **kwargs):
    #     form = ProfileForm(instance=self.get_profile(request.user))
    #     if request.method == 'POST':
    #         form = ProfileForm(request.POST, request.FILES, instance=self.get_profile(request.user))
    #         if form.is_valid():
    #             form.instance.user = request.user
    #             form.save()
    #             messages.success(request, u"Профиль успешно обновлен!")
    #             return redirect(reverse("profile"))
    #     return render(request, self.template_name, {'form': form})

    # def get_profile(self, user):
    #     try:
    #         return user.profile
    #     except:
    #         return None