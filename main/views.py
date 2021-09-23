from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Post, Like, Comments
from .forms import NewPostForm, NewCommentForm
import json


class HomeView(TemplateView):
	template_name = 'home.html'


def post(request):
	post_objects = Post.objects.all()
	return render(request, 'post.html', {'post': post_objects})


class PostListView(ListView):
	model = Post
	template_name = 'post.html'
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


@login_required
def create_post(request):
	user = request.user
	User = get_user_model()
	users = User.objects.all()
	if request.method == "POST":
		form = NewPostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			data = form.save(commit=False)
			data.user = user
			data.save()
			messages.success(request, f'Posted Successfully')
			return redirect('homepage')
	else:
		form = NewPostForm()
	return render(request, 'creating.html', {'form': form,'users':users})


@login_required
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	user = request.user
	is_liked =  Like.objects.filter(user=user, post=post)
	if request.method == 'POST':
		form = NewCommentForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.post = post
			data.username = user
			data.save()
			return redirect('post-detail', pk=pk)
	else:
		form = NewCommentForm()
	return render(request, 'post_detail.html', {'post':post, 'is_liked':is_liked, 'form':form})


@login_required
def like(request):
	post_id = request.GET.get("likeId")
	user = request.user
	post = Post.objects.get(pk=post_id)
	liked= False
	like = Like.objects.filter(user=user, post=post)
	if like:
		like.delete()
	else:
		liked = True
		Like.objects.create(user=user, post=post)
	resp = {'liked':liked}
	response = json.dumps(resp)
	return HttpResponse(response, content_type = "application/json")