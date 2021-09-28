from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('success/',SuccessView.as_view(), name="success"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile/edit/', EditProfileView.as_view(), name="edit_profile"),
    path('friends/', friend_list, name="friend_list"),
    path('users/', users_list, name="users_list"),
]
