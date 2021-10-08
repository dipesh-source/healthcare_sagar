from django.contrib import admin
from doctor.models import Doc_time, Post, Treatment


@admin.register(Treatment)
class treat(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'doc','doc_pic' ,'doc_name', 'phone', 'when', 'master',
                    'disease', 'img', 'link', 'one', 'two', 'three','four','pat_name','pat', 'patient', 'success','fdate']
    list_filter = ('doctor',)


@admin.register(Doc_time)
class two(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'day', 'date', 'start_time', 'end_time']


@admin.register(Post)
class three(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'title', 'dis', 'slug', 'info', 'fdate']
