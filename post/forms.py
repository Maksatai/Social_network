from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        photo = forms.ImageField(required=False)
        fields = [ 'text', 'photo', 'video', 'created_at']

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['text', 'photo', 'video', 'tags']