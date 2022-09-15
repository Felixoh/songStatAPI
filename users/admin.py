from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.forms import Textarea
from django.db import models
from users.models import NewUser,UserSettings,Membership,PayHistory,UserMembership,Subscription
from django.forms import *
from spotAPI.admin import musicApp


# Register your models here.
class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email','user_name','first_name')
    list_filter = ('email','user_name','first_name','is_active','is_staff')
    ordering = ('-start_date',)
    list_display = ('email','id','user_name','first_name','is_active','is_staff')
    fieldsets = (
        (None,{'fields':('email','user_name','first_name',)}),
        ('Permissions',{'fields':('is_staff','is_active')}),
        ('personal',{'fields':('about',)}),
    )
    
    add_fieldsets = (
        
        (
            None,{
                'classes':('wide',),
                'fields':('email','user_name','first_name','password1','password2','is_active')
            }
        )
    )

# musicApp.register(NewUser,UserAdminConfig)
# musicApp.register(UserSettings)
# musicApp.register(Membership)
# musicApp.register(PayHistory)
# musicApp.register(UserMembership)
# musicApp.register(Subscription)


admin.site.register(NewUser,UserAdminConfig)
admin.site.register(UserSettings)
admin.site.register(Membership)
admin.site.register(PayHistory)
admin.site.register(UserMembership)
admin.site.register(Subscription)