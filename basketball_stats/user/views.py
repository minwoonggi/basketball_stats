from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .models import BsUser
from .forms import LoginForm, RegisterForm

# Create your views here.
class UserCreate(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/user/login'

    def form_valid(self, form):
        userid = form.cleaned_data.get('userid')
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        teamname = form.cleaned_data.get('teamname')
        backnumber = form.cleaned_data.get('backnumber')

        bsuser = BsUser(
            user_id=userid,
            password=make_password(password),
            user_name=username,
            team_name=teamname,
            back_number=backnumber
        )
        bsuser.save()

        return super().form_valid(form)

def home(request):
    if request.session.get('user'):
        id = request.session.get('user')

        bsuser = BsUser.objects.get(pk=id)
        return render(request, 'login.html')

    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form' : form })


# def register(request):
#     res_data = {}
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     elif request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#         #     userid = form.userid
#         #     password = form.password
#         #     repassword = form.re_password
#         #     username = form.username
#         #     teamname = form.teamname
#         #     backnumber = form.backnumber

        

#         # # 필수 입력 항목을 입력하지 않았을 경우
#         # if not (userid and password and repassword and username and teamname):
#         #     res_data['error'] = '등번호를 제외한 모든 항목을 입력해야합니다.'

#         # # 비밀번호 형식이 올바르지 않을 경우
#         # elif not passwordCheck(password):
#         #     res_data['error'] = '비밀번호 형식이 올바르지 않습니다.'

#         # # 비밀번호와 비밀번호 확인 입력이 다를 경우
#         # elif password != repassword:
#         #     res_data['error'] = '비밀번호가 일치하지 않습니다.'

#         # # 등록된 팀이 아닌 경우 (team table 생성 후)
        
        
#         # 회원가입 저장
#         # else:
#         #     bsuser = BsUser(
#         #         user_id = userid,
#         #         password = make_password(password),
#         #         user_name = username,
#         #         team_name = teamname,
#         #         back_number = backnumber
#         #     )
#         #     bsuser.save()
            
#         #     # 회원가입 후 home으로 이동
#             return redirect('/')

#         return render(request, 'register.html', res_data)