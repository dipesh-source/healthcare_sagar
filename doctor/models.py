from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from django.shortcuts import render
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User

from patient.models import Book_app
from django.conf import settings

User = settings.AUTH_USER_MODEL

'''
    Doctor Information
'''
DIS = (
    ('Neurology', 'Neurology'),
    ('Opthalmology', 'Opthalmology'),
    ('Nuclear Magnetic', 'Nuclear Magnetic'),
    ('Surgical', 'Surgical'),
    ('Cardiology', 'Cardiology'),
    ('Dental', 'Dental'),
    ('Traumatology', 'Traumatology'),
    ('General Surgeon', 'General Surgeon'),
    ('Medicine Specialists', 'Medicine Specialists'),
    ('Sports Medicine Specialists', 'Sports Medicine Specialists'),
    ('Other', 'Other'),
)

'''
    Doctor time table
'''
# are Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday,


class Doc_time(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    day = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    fdate = models.DateTimeField(auto_created=True, auto_now_add=True)


'''
    Upload Post
'''


class Post(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='doctor blog')
    dis = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    info = FroalaField(theme='dark')
    content = FroalaField(options={
        'toolbarInline': True,
    })
    fdate = models.DateTimeField(auto_now_add=True)


'''
    Doctor will give propper treatment to patient
'''


class Treatment(models.Model):
    doctor = models.ForeignKey(
        Book_app, on_delete=models.CASCADE, null=True, blank=True)
    doc = models.CharField(max_length=100, null=True, blank=True)
    doc_pic = models.ImageField(upload_to = 'doc_pic')
    phone = models.IntegerField(null=True,blank=True)
    doc_name = models.CharField(max_length=100, null=True, blank=True)
    when = models.CharField(max_length=100, null=True, blank=True)
    master = models.CharField(max_length=100, null=True, blank=True)
    disease = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to = 'treatment')
    link = models.URLField(max_length=500, null=True, blank=True)
    one = models.CharField(max_length=100, null=True, blank=True)
    two = models.CharField(max_length=100, null=True, blank=True)
    three = models.CharField(max_length=100, null=True, blank=True)
    four = models.TextField(max_length=3000,null=True,blank=True)
    pat_name = models.CharField(max_length=100,null=True,blank=True)
    pat = models.CharField(max_length=100, null=True, blank=True)
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    success = models.BooleanField(default=False)
    fdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.doctor)
