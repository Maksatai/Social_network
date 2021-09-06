from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

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