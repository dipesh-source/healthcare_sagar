from django.contrib import admin
from patient.models import Pat_inqu,Vis_inquiry,Feedback,Book_app
# Register your models here.

@admin.register(Book_app)
class book(admin.ModelAdmin):
    list_display  = ['id','doc','doctor','doc_name','ph','mast','add','when','in_day','out_day','start_time','end_time','patient','disease','write','pro','gender','fnm','lnm','phone','img','address','check','fdate']
    list_filter = ('when',)
@admin.register(Pat_inqu)
class one(admin.ModelAdmin):
    list_display = ['id','patient','about','message','fate']

@admin.register(Vis_inquiry)
class two(admin.ModelAdmin):
    list_display  = ['id','name','phone','about','message','fdata']

@admin.register(Feedback)
class three(admin.ModelAdmin):
    list_display = ['id','patint','select','excplain','fdate']