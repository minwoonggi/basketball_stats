from django.contrib import admin
from .models import BsBoard

# Register your models here.


class BsBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'title', 'content', 'image',
                    'registered_dttm', 'updated_dttm')


admin.site.register(BsBoard, BsBoardAdmin)
