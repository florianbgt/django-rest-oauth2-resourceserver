from django.contrib import admin
from django.urls import path, include       #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('users/', include('users.urls'))
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),       #new
]
