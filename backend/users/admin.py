from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import *

class MyUserAdmin(UserAdmin):
    ordering = ('id',)

admin.site.register(CustomUser, MyUserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user_full_name', 'user_emailid', 'user_phone')
