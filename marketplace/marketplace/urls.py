from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('items/', include('items.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('Users/', include('Users.urls')),
]
