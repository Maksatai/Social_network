from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
# from v_profile.models import Profile
# from v_profile.forms import ProfileForm


class ProfileView(TemplateView):
    template_name = "profile.html"

    # def dispatch(self, request, *args, **kwargs):
    #     if not Profile.objects.filter(user=request.user).exists():
    #         return redirect(reverse("edit_profile"))
    #     context = {
    #         'selected_user': request.user
    #     }
    #     return render(request, self.template_name, context)


# class EditProfileView(TemplateView):
#     template_name = "edit_profile.html"

#     def dispatch(self, request, *args, **kwargs):
#         form = ProfileForm(instance=self.get_profile(request.user))
#         if request.method == 'POST':
#             form = ProfileForm(request.POST, request.FILES, instance=self.get_profile(request.user))
#             if form.is_valid():
#                 form.instance.user = request.user
#                 form.save()
#                 messages.success(request, u"Профиль успешно обновлен!")
#                 return redirect(reverse("profile"))
#         return render(request, self.template_name, {'form': form})

#     def get_profile(self, user):
#         try:
#             return user.profile
#         except:
#             return None
