from django import forms
from .models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        photo = forms.ImageField(required=False)
        fields = [ 'text', 'photo', 'created_at']

class NewPostForm(forms.ModelForm):
	# text = forms.TextInput(widget = forms.TextInput(attrs={'placeholder':'text'}))
	# tags = forms.TextInput(widget = forms.TextInput(attrs={'placeholder':'hashtag'}))
	# photo = forms.ImageField(widget = forms.ImageField)
	class Meta:
		model = Post
		fields = ['text', 'photo', 'tags']


class NewCommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['comment']