from . import views
from django.urls import path
from user.views import UserCreate, UserLogin

urlpatterns = [
    path('register/', UserCreate.as_view()),
    path('login/', UserLogin.as_view()),
]
