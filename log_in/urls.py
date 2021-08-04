from django.urls import path
from log_in.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
]
