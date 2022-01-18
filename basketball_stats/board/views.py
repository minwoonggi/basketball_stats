from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BsBoard
from user.models import BsUser

# Create your views here.

class BsBoard(ListView):
    template_name = 'boards.html'
    context_object_name = 'boards'
    model = BsBoard

    def get_queryset(self):
        return