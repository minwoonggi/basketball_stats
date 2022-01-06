from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class BsUser(models.Model):
    username = models.CharField(max_length=32, verbose_name='이름')
    teamname = models.CharField(max_length=32, verbose_name='팀명')
    backnumber = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='등번호')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='가입일시')

    class Meta:
        managed = False
        db_table = 'bs_user'
        verbose_name = 'bs user'
        verbose_name_plural = 'bs user'