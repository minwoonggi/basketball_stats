from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .models import BsUser, BsTeam
from .forms import LoginForm, RegisterForm, RegisterTeamForm
from .telegram import sendMsg
import datetime

# Create your views here.


class UserCreate(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/login'

    def form_valid(self, form):
        userid = form.data.get('userid')
        password = form.data.get('password')
        username = form.data.get('username')
        teamname = form.data.get('teamname')
        backnumber = form.data.get('backnumber')

        bsuser = BsUser(
            user_id=userid,
            password=make_password(password),
            user_name=username,
            team_name=teamname,
            back_number=backnumber
        )
        bsuser.save()

        return super().form_valid(form)

class UserLogin(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self,form):
        userid = form.data.get('userid')
        password = form.data.get('password')

        if userid and password:
            try:
                bsuser = BsUser.objects.get(userid=userid)
                if not check_password(password, bsuser.password):
                    return
                else:
                    self.request.session['user'] = userid
                    return super().form_valid(form)
            except:
                return

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             request.session['user'] = form.id
#             return redirect('/')
#     else:
#         form = LoginForm()

#     return render(request, 'login.html', {'form': form})

class TeamCreate(FormView):
    template_name = 'register_team.html'
    form_class = RegisterTeamForm
    success_url = '/'

    def form_valid(self, form):
        teamname = form.data.get('teamname')
        name = form.data.get('name')
        phone = form.data.get('phone')

        sendMsg('\'{0}\' 팀 등록이 요청되었습니다. \n이름: {1} \n전화번호: {2} \n승인하시겠습니까? \
            \n [Yes](http://127.0.0.1:8000/team_approve/?teamname={0}&yn=Y) \
            \t [No](http://127.0.0.1:8000/team_approve/?teamname={0}&yn=N)'.format(teamname, name, phone))

        return super().form_valid(form)

def teamApproval(request):
    teamname = request.GET.get('teamname')
    yn = request.GET.get('yn')
    
    if yn == 'Y':
        bsteam = BsTeam(
            team_name=teamname,
            team_yn=yn,
            yn_dttm=datetime.datetime.now(),
            registered_dttm=datetime.datetime.now(),
            updated_dttm=datetime.datetime.now(),
        )
        bsteam.save()
        sendMsg('\'%s\' 팀 등록이 완료되었습니다.' % teamname)
        return render(request, 'register_team_yn.html', {'approve': 'Y', 'teamname': teamname })
    else:
        sendMsg('\'%s\' 팀 등록이 반려되었습니다.' % teamname)
        return render(request, 'register_team_yn.html', {'approve': 'N', 'teamname': teamname })

def home(request):
    return render(request, 'home.html')

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
