from django.urls import path
from .views      import SignUp, SignIn, NameCheck,MyInfo
from user        import views

urlpatterns = [
    path('sign-up/', SignUp.as_view()),
    path('log-in/', SignIn.as_view()),
    path('name-check/', NameCheck.as_view()),
    path('myinfo/', MyInfo.as_view()),
]