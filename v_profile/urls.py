from django.urls import path
from v_profile.views import ProfileView
from v_profile.views import EditProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name="profile"),
   path('profile/edit/', EditProfileView.as_view(), name="edit_profile"),
]