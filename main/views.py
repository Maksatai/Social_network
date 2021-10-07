from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Post, Comment
from .forms import NewPostForm, NewCommentForm
import json
from django.utils import timezone


def search(request):
    if 'search' in request.GET and request.GET['search']:
        q = request.GET['search']
    posts = Post.objects.filter(text__icontains=q)
    context = {'posts': posts}
    return render(request, 'post.html', context)


class PostListView(TemplateView):
	template_name = 'post.html'
	paginate_by = 12
	
	def dispatch(self, request, *args, **kwargs):
		User = get_user_model()
		form = NewPostForm(request.POST or None, request.FILES or None)
		if request.method == 'POST':
			form = NewPostForm(request.POST, request.FILES)
			if form.is_valid():
				form.instance.user = request.user
				form.save()
				return redirect(reverse("homepage"))
			else:
				form = NewPostForm()

		context = {
			'posts': Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at'),
			'form':form,

		}
		return render(request, self.template_name, context)



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
	fields = ['text', 'photo', 'tags']
	template_name = 'creating.html'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user:
			return True
		return False

class PostCommentView(View):
    def dispatch(self, request, *args, **kwargs):
        post_id = request.GET.get("post_id")
        comment = request.GET.get("comment")
        if comment and post_id:
            post = Post.objects.get(pk=post_id)
            comment = Comment(comment=comment, post=post, username=request.user)
            comment.save()
            return render(request, "comment.html", {'comment': comment})
        return HttpResponse(status=500, content="")