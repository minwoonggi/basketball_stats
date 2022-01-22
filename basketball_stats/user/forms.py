from django import forms
from .models import BsTeam, BsUser
from django.contrib.auth.hashers import check_password, make_password
from .utils import idCheck, passwordCheck


class LoginForm(forms.Form):
    class Meta:
        model = BsUser
        fields = ('userid', 'password')

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


class RegisterForm(forms.ModelForm):

    class Meta:
        model = BsUser
        fields = ('userid', 'password', 're_password', 'username', 'teamname', 'backnumber')

    userid = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=32,
        label="아이디",
        required=True,
        help_text='영문으로 시작, 5~15자 길이'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput,
        label='비밀번호',
        help_text='8자 이상, 특수문자 포함'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        help_text='비밀번호를 한번 더 입력해주세요.',
        widget=forms.PasswordInput,
        label="비밀번호 확인"
    )
    username = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요.'
        },
        max_length=32,
        label="이름",
        help_text='이름을 입력해주세요.'
    )
    teamname = forms.CharField(
        error_messages={
            'required': '팀명을 입력해주세요.'
        },
        max_length=32,
        label='팀명',
        help_text='팀명을 입력해주세요.'
    )
    backnumber = forms.CharField(
        max_length=32,
        label='등번호',
        help_text='없을 경우 입력하지 않으셔도 됩니다.',
        required=False
    )

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
            if not idCheck(userid):
                self.add_error('userid', '아이디 형식이 올바르지 않습니다.')
                return

            # 비밀번호 검사
            if not passwordCheck(password):
                self.add_error('password', '비밀번호 형식이 올바르지 않습니다.')
                return

            if password != re_password:
                self.add_error('re_password', '비밀번호가 일치하지 않습니다.')
                return

class RegisterTeamForm(forms.ModelForm):

    class Meta:
        model = BsTeam
        fields = ('teamname', 'name', 'phone')

    teamname = forms.CharField(
        error_messages={
            'required': '팀명을 입력해주세요.'
        },
        max_length=32,
        label="팀명",
        required=True,
        help_text='팀명을 입력해주세요.'
    )
    name = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요.'
        },
        max_length=32,
        label="이름",
        required=True,
        help_text='이름을 입력해주세요.'
    )
    phone = forms.CharField(
        error_messages={
            'required': '전화번호를 입력해주세요.'
        },
        max_length=32,
        label="전화번호",
        required=True,
        help_text='\'-\'을 제외하고 입력해주세요.'
    )

    def clean(self):
        cleaned_data = super().clean()
        teamname = cleaned_data.get('teamname')
        phone = cleaned_data.get('phone')

        if teamname and phone:
            pass
        else:
            self.add_error('teamname', '비밀번호가 일치하지 않습니다.')
