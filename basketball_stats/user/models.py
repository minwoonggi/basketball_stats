from django.db import models

# Create your models here.

class BsUser(models.Model):
    user_id = models.CharField(max_length=32, verbose_name='아이디')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    user_name = models.CharField(max_length=32, verbose_name='이름')
    team_name = models.CharField(max_length=32, verbose_name='팀명')
    back_number = models.CharField(max_length=3, blank=True, null=True, verbose_name='등번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='가입일시')
    updated_dttm = models.DateTimeField(auto_now=True, verbose_name='수정일시')

    class Meta:
        db_table = 'bs_user'
        verbose_name = 'bs user'
        verbose_name_plural = 'bs user'

class BsTeam(models.Model):
    team_name = models.CharField(max_length=32, verbose_name='팀명')
    team_yn = models.CharField(max_length=1, default='N')
    yn_dttm = models.DateTimeField(auto_now_add=True, verbose_name='승인일시')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='신청일시')
    updated_dttm = models.DateTimeField(auto_now=True, verbose_name='수정일시')
    
    class Meta:
        db_table = 'bs_team'
        verbose_name = 'bs team'
        verbose_name_plural = 'bs team'