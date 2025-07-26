from django.urls import path
from . import views

urlpatterns = [
    path('seller/', views.SellerUser, name='seller'),
    path('buyer/', views.BuyerUser, name='buyer'),
    path('update/', views.Update, name='edit_profile'),
    path('change_password/', views.ChangePassword, name='change_password'),
    path('cart/', views.Cart, name='cart'),
    path('orders/', views.Orders, name='orders'),
    path('cancel_order/<int:id>/', views.cancel_order, name='cancel_order'),
    path('remove_from_cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('edit_cart/<int:id>/', views.edit_cart, name='edit_cart'),
]
