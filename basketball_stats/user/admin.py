from django.contrib import admin
from .models import BsUser

# Register your models here.

class BsUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'teamname', 'backnumber', 'password' )

admin.site.register(BsUser, BsUserAdmin)