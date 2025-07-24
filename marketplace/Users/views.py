from django.shortcuts import render, redirect
from django.http import request
from Users.models import User
from .forms import UserUpdateForm, PasswordForm
from django.contrib import messages


def SellerUser(request):
    user = request.user
    data = User.objects.filter(id=user.id)
    return render(request, 'users/seller.html', {'user': data})


def BuyerUser(request):
    user = request.user
    data = User.objects.filter(id=user.id)
    return render(request, 'users/buyer.html', {'user': data})

def Update(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            if user.type == 'buyer':
                return redirect('buyer')
            else :
                return redirect('seller')  # Redirect to the seller page after update
    else:
        form = UserUpdateForm(instance=user)    
            
    return render(request, 'users/update.html', {'form': form})

def ChangePassword(request):
    user = request.user
    if request.method == 'POST':
        
        new_password = request.POST['new_password']
        new_password2 = request.POST['new_password2']
        
        if new_password == new_password2:
                user.set_password(new_password)
                user.save()
                return redirect('login')
        else:
                messages.error(request, 'New passwords do not match.')
                return redirect('change_password')
        
            
    else:
        form = PasswordForm()
    
    return render(request, 'users/change_password.html', {'form': form})

def Cart(request):
    return render(request, 'users/cart.html')

def Orders(request):
    return render(request, 'users/orders.html')

