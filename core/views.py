from django.shortcuts import render
from post.models import Post, Like
from django.views.generic import ListView

# class HomeView(TemplateView):
#     template_name = 'base.html'

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