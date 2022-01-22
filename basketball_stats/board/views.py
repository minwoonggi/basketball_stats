from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import BsBoard
from rest_framework import generics
from rest_framework import mixins
from .serializers import BsUserSerializer
from user.models import BsUser 
from .forms import BoardCreateForm

# Create your views here.

# class Board(ListView):
#     template_name = 'boards.html'
#     context_object_name = 'boards'
#     # model = BsBoard
#     queryset = BsBoard.objects.all()

def Board(request):
    return render(request, 'boards.html')

class BoardCreate(FormView):
    template_name = 'create_board.html'
    form_class = BoardCreateForm
    success_url = '/boards/'

    def form_valid(self,form):
        title = form.data.get('title')
        content = form.data.get('content')
        image = form.data.get('image')

        if self.request.session['user']:
            bsboard = BsBoard(
                bsuser_id= self.request.session['userid'],
                title=title,
                content=content,
                image=image,
            )
            bsboard.save()
        else:
            return redirect('/user/login')

# class BsUserListAPI(generics.GenericAPIView, mixins.ListModelMixin):
#     serializer_class = BsUserSerializer

#     def get_queryset(self):
#         return BsUser.objects.all().order_by('id')

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs) # mixins에 list라는 함수를 사용하면 model의 list를 json으로 return

