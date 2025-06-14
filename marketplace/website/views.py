from django.shortcuts import render, redirect
from django.http import request
from items.models import *
from website.forms import SignUpForm, LogInForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def index(request):
    items = item.objects.filter(is_sold=False)
    categories = category.objects.all()
    return render(request, 'index.html', {'categories': categories, 'items':items})


def contact(request):
    return render(request, 'contact.html')

def signUp(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/login')
            
    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('index')
        else:
            messages.success(request, 'There was an error, try again.')
            return redirect('login')
    else:
        form = LogInForm()
        
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('index')