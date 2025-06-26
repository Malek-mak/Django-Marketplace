from django.shortcuts import render, redirect
from django.http import request
from items.models import *
from .models import message
from website.forms import SignUpForm, LogInForm, ContactForm
from django.contrib.auth import login, logout, authenticate


def index(request):
    items = item.objects.filter(is_sold=False)
    categories = category.objects.all()
    return render(request, 'website/index.html', {'categories': categories, 'items':items})


def contact(request):
    return render(request, 'website/contact.html')

def signUp(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/login')
            
    else:
        form = SignUpForm()
        
    return render(request, 'website/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('index')
        else:
            
            return redirect('login')
    else:
        form = LogInForm()
        
    return render(request, 'website/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('index')


def contact(request, pk, by):
    
    
    
    if request.method == 'POST':
                
        #from the customer side
        
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sent_to = by
            msg.about = item.objects.get(pk=pk)
            msg.save()
            return redirect('detail', pk=pk)
            
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form,
                                            'by': by,
                                            'id': pk})
    
    
def messages(request):
    messages = message.objects.filter(sent_to=request.user)
    return render(request, 'website/messages.html', {
        'messages': messages
    })
        
    
    
        
    