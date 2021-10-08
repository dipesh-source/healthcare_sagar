from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from account.models import Verify_req,Use_email,Doctor_validate

@admin.register(Doctor_validate)
class Doc(admin.ModelAdmin):
    list_display = ['doctor','mas','check']
    list_filter = ('doctor',)

"""
class PatientInline(admin.TabularInline):
    model = Patient
    extra = 0

class DoctorAdmin(admin.ModelAdmin):
    inlines = [PatientInline]
"""

@admin.register(Use_email)
class Email_data(admin.ModelAdmin):
    list_display  = ['id','user','email','token']

@admin.register(Verify_req)
class Checking(admin.ModelAdmin):
    list_display = ['id','user','token','check']

# 'profile', 'who', 'gender', 'dob','address'
class CustomUserAdmin(UserAdmin):

    fieldsets = [
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name',
         'last_name','who','in_day','out_day','start_time','end_time','master','clinic','some','username','profile','dob','mobile','gender','address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        (_('Important date'), {'fields': ('date_joined', 'last_login')})
    ]

    add_fieldsets = [
        (None, {'fields': ('email', 'password1', 'password2'),
                'classes': ('wide')}),
    ]

    list_display = ['email', 'username', 'who', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)