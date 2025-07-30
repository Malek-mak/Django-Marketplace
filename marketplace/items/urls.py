from . import views
from django.urls import path


urlpatterns = [
    path("", views.items, name='items'),
    path("<int:pk>/detail", views.detail, name='detail'),
    path("New_Item", views.new, name='new'),
    path("<int:pk>/delete", views.delete_item, name='delete'),
    path("edit/<int:pk>", views.edit, name='edit'),
    path('review/<int:pk>', views.ReviewView, name='review'),
    path('order/<int:pid>/', views.Order, name='order'),
]
