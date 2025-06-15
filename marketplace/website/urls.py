from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name='index'),
    path("contact/<int:pk>/<str:by>", views.contact, name='contact'),
    path("SignUp", views.signUp, name='signup'),
    path("Login", views.login_user, name='login'),
    path("Logout", views.logout_user, name='logout'),
    path("Messages", views.messages, name='messages'),
]