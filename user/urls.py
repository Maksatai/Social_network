from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile/edit/', EditProfileView.as_view(), name="edit_profile"),
]
