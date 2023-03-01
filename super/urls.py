from django.urls import path
from .views      import UserList

urlpatterns = [
    path('user-list/', UserList.as_view()),

]