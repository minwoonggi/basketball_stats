from django import forms
from .models import BsUser
from django.contrib.auth.hashers import check_password, make_password


class LoginForm(forms.Form):
    userid = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=32, label="아이디")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label="비밀번호")
    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')

        if userid and password:
            try:
                bsuser = BsUser.objects.get(user_id=userid)
            except BsUser.DoesNotExist:
                self.add_error('userid', '아이디가 없습니다.')
                return

            if not check_password(password, bsuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
            else:
                self.id = bsuser.id


class RegisterForm(forms.Form):
    userid = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=32, label="아이디")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label="비밀번호")
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label="비밀번호 확인")
    username = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요.'
        },
        max_length=32, label="이름")
    teamname = forms.CharField(
        error_messages={
            'required': '팀명을 입력해주세요.'
        },
        max_length=32, label="팀명")
    backnumber = forms.CharField(
        max_length=32, label="팀명")

    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        username = cleaned_data.get('username')
        teamname = cleaned_data.get('teamname')
        backnumber = cleaned_data.get('backnumber')

        if userid and password and re_password and username and teamname:
            # 아이디 검사
            if idCheck(userid):
                self.add_error('userid', '아이디 형식이 올바르지 않습니다.')
                return

            # 비밀번호 검사
            if passwordCheck(password):
                self.add_error('password', '비밀번호 형식이 올바르지 않습니다.')
                return

            bsuser = BsUser(
                user_id = userid,
                password = make_password(password),
                user_name = username,
                team_name = teamname,
                back_number = backnumber
            )
            bsuser.save()
        
        else:
            self.add_error('등번호를 제외한 모든 항목을 입력해야합니다.')



import re

def idCheck(id):
    ID_regex = re.compile("([A-za-z]{5,15})")
    ID_validation = ID_regex.search(id.replace(" ",""))
    
    if ID_validation:
        return True
    else:
        return False

def passwordCheck(password):
    
    if len(password) < 8 or len(password) > 21 and not re.findall('[0-9]+', password) and not \
    re.findall('[a-z]', password) or not re.findall('[A-Z]', password):
        print('비밀번호 기준(숫자, 영문 대소문자 구성)에 맞지 않습니다.')
        return False

    elif not re.findall('[`~!@#$%^&*(),<.>/?]+', password):
        print('비밀번호는 최소 1개 이상의 특수문자가 포함되어야 함')  
        return False

    print('비밀번호의 길이, 숫자, 영문자 등 유효함!!')
    return True
