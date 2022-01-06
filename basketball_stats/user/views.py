from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import BsUser


# Create your views here.

def register(request):
    return render(request, 'register.html')