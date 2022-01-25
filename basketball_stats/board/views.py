from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .models import BsBoard
from rest_framework import generics
from rest_framework import mixins
from .serializers import BsUserSerializer
from user.models import BsUser 
from .forms import BoardCreateForm

from django.utils.decorators import method_decorator
from user.decorators import login_required

# Create your views here.

class Board(ListView):
    template_name = 'boards.html'
    context_object_name = 'boards'
    model = BsBoard
    # queryset = BsBoard.objects.all()

# def Board(request):
#     return render(request, 'boards.html')

@method_decorator(login_required, name='dispatch')
class BoardCreate(FormView):
    template_name = 'create_board.html'
    form_class = BoardCreateForm
    success_url = '/boards'

    def form_valid(self,form):
        title = form.data.get('title')
        content = form.data.get('content')
        image = form.data.get('image')

        bsuser = BsUser.objects.filter(user_id=self.request.session['user'])

        if bsuser.exists():
            bsboard = BsBoard(
                user_id= bsuser[0],
                title=title,
                content=content,
                image=image,
            )
            bsboard.save()
        else:
            self.success_url = '/login'
        return super().form_valid(form)

# class BsUserListAPI(generics.GenericAPIView, mixins.ListModelMixin):
#     serializer_class = BsUserSerializer

#     def get_queryset(self):
#         return BsUser.objects.all().order_by('id')

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs) # mixins에 list라는 함수를 사용하면 model의 list를 json으로 return

