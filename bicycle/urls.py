from django.urls import path
from .views      import BicycleUp

urlpatterns = [
    path('register/', BicycleUp.as_view()),
]