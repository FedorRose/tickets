from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from main.models import Ticket


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'text', 'developer', 'priority', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control p-0 border-0"}),
            'text': forms.Textarea(attrs={'rows': "5", 'class': "form-control p-0 border-0"})
        }
