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
    # path('friend_request/<int:pk>/',friend_request, name = "friend_request"),
    # path('delete_request/<operation>/<int:pk>/',delete_request, name="delete_request"),
    # path('delete_friend/<int:pk>/',remove_friend, name="delete_friend"),
    # path('add_friend/<int:pk>/', add_friend, name = "add_friend"),
    path('all-profiles/', profiles_list_view, name = "all-profiles-view"),
    path('search_users/', search_users, name ="search_users")
]
