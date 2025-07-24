from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from Users.models import User
from .models import message

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'type', 'phone')
        
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name' ,'class': 'rounded-xl px-6 py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name' ,'class': 'rounded-xl px-6 py-4'}))
    type = forms.ChoiceField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')], widget=forms.Select(attrs={'class': 'rounded-xl px-6 py-4'}))
        
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username' ,'class': 'rounded-xl px-6 py-4'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email' ,'class': 'rounded-xl px-6 py-4'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password' ,'class': 'rounded-xl px-6 py-4'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat' ,'class': 'rounded-xl px-6 py-4'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number' ,'class': 'rounded-xl px-6 py-4'}))


class LogInForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username' ,'class': 'rounded-xl px-6 py-4'}))

   
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password' ,'class': 'rounded-xl px-6 py-4'}))

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = message
        fields = ('message', 'sent_by')
        
    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Message',
        'class': 'rounded-xl px-6 py-12'
    }))
    sent_by = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'class': 'rounded-xl px-12 py-4'
    }))