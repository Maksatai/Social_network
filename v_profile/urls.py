from django.urls import path
from v_profile.views import ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name="profile"),
]