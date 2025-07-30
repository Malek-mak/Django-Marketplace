from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from Users.models import User, CartModel, OrderModel
from .forms import UserUpdateForm, PasswordForm, CartForm
from django.contrib import messages
from items.models import item


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
    cart = CartModel.objects.filter(user=request.user)
    return render(request, 'users/cart.html', {'cart': cart})

def Orders(request):
    orders = OrderModel.objects.filter(user=request.user)
    return render(request, 'users/orders.html', {'orders': orders})

def cancel_order(request, id):
    order = OrderModel.objects.get(id=id)
    order.status = 'cancelled'
    order.save()
    return redirect('orders')

def remove_from_cart(request, id):
    cart_item = CartModel.objects.get(id=id)
    cart_item.delete()
    return redirect('cart')

def edit_cart(request, id):
    cart = CartModel.objects.filter(user=request.user)
    cart_item = get_object_or_404(CartModel, id=id)
    if request.method == 'POST':
        form = CartForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cart item updated successfully')
            form = CartForm(instance=cart_item)
            return redirect('cart')
    else:
        form = CartForm(instance=cart_item)
    
    return render(request, 'users/cart.html', {'cart': cart, 'form': form})  
    
    
def Vendor(request, user):
    u = User.objects.get(username=user)
    items = u.items.all()
    return render(request, 'users/vendor.html', {'items': items})