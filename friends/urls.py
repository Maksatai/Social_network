from django.urls import path
from friends.views import FriendsView

urlpatterns = [
    path('friends/', FriendsView.as_view(), name="friends"),
]
