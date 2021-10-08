from django.contrib import admin
from .models import Gallery,Qualified
# Register your models here.

@admin.register(Gallery)
class One(admin.ModelAdmin):
    list_display = ['id','about','data','content','fdate']

@admin.register(Qualified)
class dipesh(admin.ModelAdmin):
    list_display = ['id','doctor','name','mas','text']