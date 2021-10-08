from django.db.models.base import Model
from django.forms import fields
from doctor import models
from doctor.models import Doc_time, Post ,Treatment
from django import forms
from django.forms import widgets
from django.forms.widgets import Widget
from django import forms
from froala_editor.widgets import FroalaEditor
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.forms import UserChangeForm


'''
    Doctor Post Form
'''


class Post_form(forms.ModelForm):
    info = forms.CharField(label='Enter Your Data', widget=FroalaEditor,
                           label_suffix='', error_messages={'required': 'Write your blog here.....!'})
    content = forms.CharField(required=False, widget=FroalaEditor(options={
        'toolbarInline': True,
    }))

    class Meta:
        model = Post
        fields = ['title', 'dis', 'img', 'info', 'content']
        labels = {
            'title': 'Title name',
            'img': 'select disease img',
            'dis': 'Enter Disease'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'autofocus': True}),
            'img': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'dis': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }
        error_messages = {
            'title': {'required': 'Please enter blog title'},
            'img': {'required': 'Please select disease image'},
            'dis': {'required': 'Must be disease name'},

        }


'''
    Doctor time table
'''
DAYS = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)


class Doc_time_form(forms.ModelForm):
    day = forms.ChoiceField(choices=DAYS, label_suffix="", label='Select Day', error_messages={
                            'required': 'Please select day'}, widget=forms.RadioSelect(attrs={'class': ' '}))
    # time = forms.TimeField(label='Enbtetr times',widget=forms.TextInput())

    class Meta:
        model = Doc_time
        fields = ['day', 'date', 'start_time', 'end_time']
        error_messages = {
            'date': {'required': 'Date is required'},
            'time': {'required': 'Must Be Time'}
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker', 'placehoder': 'Select Date'}),
            # 'time':forms.SelectDateWidget( empty_label=("Choose Year", "Choose Month", "Choose Day")),
            'start_time': forms.TimeInput(attrs={'id': 'timepicker', 'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'id': 'timepicker', 'class': 'form-control', 'type': 'time'}),

        }

#################################################################


'''
    In special case 'Doctor Profile'
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
User = settings.AUTH_USER_MODEL
DATA = [
    ('Male', 'Male'),
    ('Female', 'Female')
]
# 'gender', 'dob', 'mobile', 'address'


class Profile_form(UserChangeForm):

    password = None
    who = None
    gender = forms.CharField(required=False, label='Select Gender', label_suffix='', error_messages={'required': 'Select Your Gender'}, widget=forms.RadioSelect(
        choices=DATA, attrs={"class": ""}))
    # in_day = forms.Select(choices=DAYS, label='Starting Day',error_messages={'required':'Please select day'},widget=forms.RadioSelect(attrs={'class':' '}))
    # out_day = forms.Select(choices=DAYS, label='Ending Day',error_messages={'required':'Please select day'},widget=forms.RadioSelect(attrs={'class':' '}))
# 'profile'

    class Meta:
        model = get_user_model()
        fields = ['username', 'master', 'in_day', 'out_day', 'start_time', 'end_time',
                  'clinic', 'some', 'first_name', 'last_name', 'profile', 'mobile', 'dob', 'address']
        labels = {
            'email': 'Your Email',
            'start_time': 'Sletct in time',
            'end_time': 'Sletct out time',
            'username': 'Your Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile': 'Select Profile Pic',
            'master': 'Select Category',
            'dob': 'Date Of Birth',
            'mobile': 'Enter Mobile Number',
            'address': 'Enter Address',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'master': forms.Select(attrs={'class': 'form-control'}),
            'in_day': forms.Select(attrs={'class': 'form-control'}),
            'out_day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'id': 'timepicker', 'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'id': 'timepicker', 'class': 'form-control', 'type': 'time'}),
            'clinic': forms.TextInput(attrs={'class': 'form-control'}),
            'some': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile': forms.FileInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }
        error_messages = {
            'master': {'required': 'Category must be selected'},
            'start_time': {'required': 'Start time is required'},
            'end_time': {'required': 'End time is required'},
        }


'''
    DOctor will give treatment (This is form for that)
'''


class Treatment_form(forms.ModelForm):
    img = forms.CharField(label='Upload Image',label_suffix='',required=False,widget=forms.FileInput(attrs={'class':'form-control'}))
    link = forms.CharField(required=False,label='Send Link', label_suffix='',
                           widget=forms.URLInput(attrs={'class': 'form-control'}))
    one = forms.CharField(label='Treatment One', widget=forms.TextInput(
        attrs={'class': 'form-control'}),error_messages={'required':'Required Treatment'})
    two = forms.CharField(required=False,label='Treatment Two', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    three = forms.CharField(required=False,label='Treatment Three', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    four = forms.CharField(required=False,label='Treatment Three', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    class Meta:
        model = Treatment
        fields = ['link', 'one', 'two', 'three']
