"""basketball_stats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import home, UserCreate, UserLogin, TeamCreate, teamApproval
from board.views import Board, BoardCreate

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # home
    path('', home),
    # user, team
    path('register/', UserCreate.as_view()),
    path('login/', UserLogin.as_view()),
    path('register_team/', TeamCreate.as_view()),
    path('team_approve/', teamApproval),
    # board 
    # path('boards/', Board),
    path('boards/', Board.as_view()), # class
    path('board/', BoardCreate.as_view()),
    # path('board/<int:pk>')

    # api
    # path('api/users/', BsUserListAPI.as_view())
]
