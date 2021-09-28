from django import forms
from .models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        photo = forms.ImageField(required=False)
        fields = [ 'text', 'photo', 'created_at']

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['text', 'photo', 'tags']


class NewCommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['comment']