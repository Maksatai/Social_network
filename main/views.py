from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Post, Comments
from .forms import NewPostForm, NewCommentForm
import json


class HomeView(TemplateView):
	template_name = 'home.html'


def post(request):
	post_objects = Post.objects.all()
	return render(request, 'post.html', {'post': post_objects})


def search(request):
    if 'search' in request.GET and request.GET['search']:
        q = request.GET['search']
    posts = Post.objects.filter(text__icontains=q)
    context = {'posts': posts}
    return render(request, 'post.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'post.html'
	context_object_name = 'posts'
	ordering = ['-created_at']
	paginate_by = 12
	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		return context


class UserPostListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'core/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 12

	def get_context_data(self, **kwargs):
		context = super(UserPostListView, self).get_context_data(**kwargs)
		user = get_object_or_404(User, user=self.kwargs.get('user'))
		liked = [i for i in Post.objects.filter(user=user) if Like.objects.filter(user = self.request.user, post=i)]
		context['liked_post'] = liked
		return context

	def get_queryset(self):
		user = get_object_or_404(User, user=self.kwargs.get('user'))
		return Post.objects.filter(user=user).order_by('-date_posted')


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


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	user = request.user

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
	return render(request, 'post_detail.html', {'post':post, 'form':form}) 


@login_required
def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


@login_required
def post_delete(request, pk):
	post = Post.objects.get(pk=pk)
	if request.user == post.user:
		Post.objects.get(pk=pk).delete()
	return redirect('homepage')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['text', 'tags']
	template_name = 'creating.html'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user:
			return True
		return False
