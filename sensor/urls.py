from django.urls import path
from .views      import GpsTem

urlpatterns = [
    path('tem-gps/', GpsTem.as_view()),
]