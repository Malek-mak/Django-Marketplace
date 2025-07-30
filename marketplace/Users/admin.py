from django.contrib import admin
from .models import User, CartModel, OrderModel
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(OrderModel)
admin.site.register(CartModel)
