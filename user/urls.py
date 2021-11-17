from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('success/',SuccessView.as_view(), name="success"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('edit/', EditProfileView.as_view(), name="edit_profile"),
    path('user/<username>', ViewUserView.as_view(), name="view_user"),
    path('friends/', FriendList.as_view(), name="friend_list"),
    path('all-profiles/', UserList.as_view(), name = "all-profiles-view"),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('send-invite/', send_invatation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('my-invites/accept/', accept_invatation, name='accept-invite'),
    path('my-invites/reject/', reject_invatation, name='reject-invite'),
    path('search_users/', SearchUsers.as_view(), name ="search_users")
]
