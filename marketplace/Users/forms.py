from django import forms
from .models import User, CartModel, OrderModel

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone' ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'rounded-xl px-6 py-4', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'rounded-xl px-6 py-4', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'rounded-xl px-6 py-4', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'rounded-xl px-6 py-4', 'placeholder': 'Phone'})  
        }
        
class PasswordForm(forms.Form):
    
        
        new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'rounded-xl px-6 py-4', 'placeholder': ' New Password'}))
        new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'rounded-xl px-6 py-4', 'placeholder': 'Confirm New Password'}))
        
        
class CartForm(forms.ModelForm):
    class Meta:
        model = CartModel
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'rounded-xl ', 'placeholder': '1'})
        }