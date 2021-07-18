from django.contrib import admin
from django.urls import path, include       #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),       #new
    path('items/', include('items.urls')),        #new
]
