from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class BsBoard(models.Model):
    bsuser = models.ForeignKey('user.BsUser', on_delete=models.CASCADE, verbose_name='유저 id(번호)')
    title = models.CharField(max_length=128, verbose_name='글제목')
    content = models.TextField(verbose_name='글내용')
    image = models.ImageField(null=True, upload_to='', blank=True, verbose_name='이미지')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성일시')
    updated_dttm = models.DateTimeField(auto_now=True, verbose_name='수정일시')
    
    class Meta:
        db_table = 'bs_board'
        verbose_name = 'bs board'
        verbose_name_plural = 'bs board'
    