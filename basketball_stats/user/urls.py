from . import views
from django.urls import path
from user.views import UserCreate

urlpatterns = [
    path('register/', UserCreate.as_view()),
    path('login/', views.login),
]
