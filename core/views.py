from django.shortcuts import render, get_object_or_404
from post.models import Post, Like
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home.html'

# def homepage(request):
#     return render(request, 'base.html')

class PostListView(ListView):
	model = Post
	template_name = 'base.html'
	context_object_name = 'posts'
	ordering = ['-created_at']
	paginate_by = 12
	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			liked = [i for i in Post.objects.all() if Like.objects.filter(user = self.request.user, post=i)]
			context['liked_post'] = liked
		return context


class UserPostListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'core/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 12

	def get_context_data(self, **kwargs):
		context = super(UserPostListView, self).get_context_data(**kwargs)
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		liked = [i for i in Post.objects.filter(user_name=user) if Like.objects.filter(user = self.request.user, post=i)]
		context['liked_post'] = liked
		return context

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(user_name=user).order_by('-date_posted')
    # template_name = 'home.html'

class SuccessView(TemplateView):
    template_name = "success.html"
