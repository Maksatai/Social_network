from django.urls import path
from core.views import HomeView, PostListView

urlpatterns = [
    path('', HomeView.as_view(), name="homepage"),
    path('feed/', PostListView.as_view(), name='feed')
]