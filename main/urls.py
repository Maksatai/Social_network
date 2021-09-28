from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import HomeView, PostListView, LikeView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name="homepage"),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/create/', views.create_post, name='create'),
    path('like/<int:pk>', LikeView, name='post-like'),
    path('delete/<int:pk>', views.post_delete, name='post-delete'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post-edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)