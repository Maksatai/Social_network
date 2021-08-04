from django.urls import path
from sign_up.views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
]