from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, NewCommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def post(request):
    post_objects = Post.objects.all()
    return render(request, 'post.html', {'post': post_objects})

def create_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect(post)
    
    post_form = PostForm()
    return render(request, '', {'post_form': post_form})


