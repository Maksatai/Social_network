from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, NewCommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def post(request):
    post_objects = Post.objects.all()
    return render(request, 'post.html', {'post': post_objects})



