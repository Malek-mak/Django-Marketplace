from django.shortcuts import render, redirect
from django.http import request
from items.models import item



def index(request):
    user = request.user
    items = item.objects.filter(created_by=user)
    return render(request, 'dashboard/dashboard.html', {'items':items})
    
