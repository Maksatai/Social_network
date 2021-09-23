from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import HomeView, PostListView, like

urlpatterns = [
    path('', PostListView.as_view(), name="homepage"),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/create/', views.create_post, name='create'),
    path('like/', views.like, name='post-like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)