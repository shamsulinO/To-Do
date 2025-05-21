from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "content"]

        widgets = {
            "title": forms.Textarea(attrs={'class':'AddTaskTitle', "rows": 1, 'placeholder': 'Заголовок'}),
            "content": forms.Textarea(attrs={'class':'AddTaskContent', "rows": 3, 'placeholder': 'Текст', 'required':False}),
        }


class Edit(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "content"]

        widgets = {
            "title": forms.Textarea(attrs={'class':'EditTitle', "rows": 1, 'placeholder': 'Заголовок'}),
            "content": forms.Textarea(attrs={'class':'EditContent', "rows": 3, 'placeholder': 'Текст', 'required':False}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'loglogin', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'logpass', 'placeholder': 'Пароль'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'reglog', 'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'regemail', 'placeholder': 'Почта'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'regpass', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'class': 'regpass', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')