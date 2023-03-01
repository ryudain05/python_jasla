from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('bicycle/', include('bicycle.urls')),
    path('admin/', include('super.urls')),
    path('sensor/', include('sensor.urls')),
]
