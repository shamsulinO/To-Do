from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "content"]

        widgets = {
            "title": forms.Textarea(attrs={'style':'margin: 10px;width: 49vw; background: #fff; border-radius: 5px; border: 2px solid #4827EC;', "rows": 1, 'placeholder': 'Title'}),
            "content": forms.Textarea(attrs={'style':'margin: 10px;width: 49vw; background: #fff; border-radius: 5px; border: 2px solid #4827EC;', "rows": 2, 'placeholder': 'Content', 'required':False}),
        }


class Edit(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "content"]

        widgets = {
            "title": forms.Textarea(attrs={'style':'margin: 10px;width: 49vw; background: #fff; border-radius: 5px; border: 2px solid #4827EC;', "rows": 1, 'placeholder': 'Title'}),
            "content": forms.Textarea(attrs={'style':'margin: 10px;width: 49vw; background: #fff; border-radius: 5px; border: 2px solid #4827EC;', "rows": 2, 'placeholder': 'Content', 'required':False}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'style': 'width: 100%; background-color: #fff; border-radius: 5px; border: 2px solid #4827EC; margin-bottom: 10px; padding-left: 5px;', 'placeholder': 'Login'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'style': 'width: 100%; background-color: #fff; border-radius: 5px; border: 2px solid #4827EC; margin-bottom: 10px; padding-left: 5px;', 'placeholder': 'Password'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'style': 'width: 100%; background-color: #fff; border-radius: 5px; border: 2px solid #4827EC; margin-bottom: 10px; padding-left: 5px;', 'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'style': 'width: 100%; background-color: #fff; border-radius: 5px; border: 2px solid #4827EC; margin-bottom: 10px; padding-left: 5px;', 'placeholder': 'Почта'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'style': 'width: 100%; background-color: #fff; border-radius: 5px; border: 2px solid #4827EC; margin-bottom: 10px; padding-left: 5px;', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'style': 'width: 100%; background-color: #fff; border-radius: 5px; border: 2px solid #4827EC; margin-bottom: 10px; padding-left: 5px;', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')