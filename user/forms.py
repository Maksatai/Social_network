from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Почта'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Подтвердите пароль'}))

    class Meta:
        model = User
        fields =['username','email','password','password2']

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('Такой пользователь существует')
        return self.cleaned_data['username']

    

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        elif len(cd['password'])<6:
            raise forms.ValidationError('Слишком короткий пароль')
        return cd['password2']



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user']