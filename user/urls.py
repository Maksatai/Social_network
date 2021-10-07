from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('success/',SuccessView.as_view(), name="success"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('edit/', EditProfileView.as_view(), name="edit_profile"),
    path('user/<username>', ViewUserView.as_view(), name="view_user"),
    path('friends/', friend_list, name="friend_list"),
    path('users/', users_list, name="users_list"),
    path('delete_friend/<int:id>/',delete_friend, name="delete_friend")
]
