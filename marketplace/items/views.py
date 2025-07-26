from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from items.models import category, item
from django.contrib.auth.decorators import login_required
from .forms import itemForm, EdititemForm
from django.contrib import messages
from django.db.models import Q
from Users.models import User, CartModel, OrderModel
from Users.forms import CartForm


def items(request):
    items = item.objects.filter(is_sold=False)
    query = request.GET.get('query', '')
    categori = request.GET.get('category', '')
    categories = category.objects.all()
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(discription__icontains=query))
        
    if categori:
        items = items.filter(categoty=categori)
        
        
    return render(request, 'items/items.html', {
        'items': items,
        'query': query,
        'categories': categories
    })


def detail(request, pk):
    i = get_object_or_404(item, pk=pk)
    
    related_items = item.objects.filter(categoty=i.categoty, is_sold=False).exclude(pk=pk)
    
    if request.method == 'POST':
        frm = CartForm(request.POST)
        if frm.is_valid():
            form = frm.save(commit=False)
            form.user = request.user
            form.product = i
            form.save()
            messages.success(request, 'Item added to cart successfully')
            return redirect('detail', pk=pk)
    else:
        frm = CartForm()
    
    return render(request, 'items/detail.html', {'item': i,
                                           'related_items': related_items,
                                             'form': frm,
                                           })

    
    
@login_required
def new(request):
    if request.method == 'POST':
        
        form = itemForm(request.POST)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, 'Item created succefully')
            return redirect('detail', pk = item.pk)
    else:
        form = itemForm()
        
    return render(request, 'items/new.html', {'form': form})

def delete_item(request, pk):
    i = get_object_or_404(item, pk=pk, created_by = request.user)
    i.delete()
    return redirect('dashboard')

def edit(request, pk):
    i = get_object_or_404(item, pk=pk, created_by = request.user)
    
    if request.method == 'POST':
        
        form = EdititemForm(request.POST)
        
        if form.is_valid():
            it = form.save(commit=False)
            it.created_by = request.user
            
            it.save()
            i.delete()
            messages.success(request, 'Item edited succefully')
            return redirect('detail', pk = it.pk)
    else:
        i = get_object_or_404(item, pk=pk, created_by = request.user)
        form = EdititemForm(instance = i)
    return render(request, 'items/edit.html', {'form': form})