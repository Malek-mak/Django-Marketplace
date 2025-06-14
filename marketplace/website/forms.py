from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username' ,'class': 'rounded-xl px-6 py-4'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email' ,'class': 'rounded-xl px-6 py-4'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password' ,'class': 'rounded-xl px-6 py-4'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat' ,'class': 'rounded-xl px-6 py-4'}))


class LogInForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username' ,'class': 'rounded-xl px-6 py-4'}))

   
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password' ,'class': 'rounded-xl px-6 py-4'}))
