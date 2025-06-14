from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='index'),
    path("contact", views.contact, name='contact'),
    path("SignUp", views.signUp, name='signup'),
    path("Login", views.login_user, name='login'),
    path("Logout", views.logout_user, name='logout'),
]