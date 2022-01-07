from django.contrib import admin
from .models import BsUser

# Register your models here.


class BsUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'password', 'user_name',
                    'team_name', 'back_number')


admin.site.register(BsUser, BsUserAdmin)
