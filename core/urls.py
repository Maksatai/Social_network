from django.urls import path
from . import views
from .views import HomeView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name="homepage"),
]