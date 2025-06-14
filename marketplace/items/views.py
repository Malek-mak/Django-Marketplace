from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from items.models import category, item
from django.contrib.auth.decorators import login_required
from .forms import itemForm, EdititemForm
from django.contrib import messages
from django.db.models import Q


def items(request):
    items = item.objects.filter(is_sold=False)
    query = request.GET.get('query', '')
    categori = request.GET.get('category', '')
    categories = category.objects.all()
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(discription__icontains=query))
        
    if categori:
        items = items.filter(categoty=categori)
        
        
    return render(request, 'items.html', {
        'items': items,
        'query': query,
        'categories': categories
    })


def detail(request, pk):
    i = get_object_or_404(item, pk=pk)
    related_items = item.objects.filter(categoty=i.categoty, is_sold=False).exclude(pk=pk)
    
    return render(request, 'detail.html', {'item': i,
                                           'related_items': related_items
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
        
    return render(request, 'new.html', {'form': form})

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
    return render(request, 'edit.html', {'form': form})