from django.contrib.auth.models import User
from django.http import request
from account import models
from django.conf import settings
# from django.forms import fields, forms
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms import fields, widgets
# from account.models import Use_email
from django import forms
from account.models import Use_email

'''
    User Authentication for new User while user login
'''


class User_authenticate(AuthenticationForm):
    username = None
    # email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email'}))
    username = forms.EmailField(label='Email Address', label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': ' ', 'autofocus': True}), error_messages={'required': 'Email Address Must Be Required'})
    password = forms.CharField(label="Password", label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg ', 'placeholder': ' '}), error_messages={'required': 'Password Must Be Required'})

    class Meta:
        model = get_user_model()
        # model = get_user_model()
        fields = ['username', 'password']

    # def clean_password(self):
    #     data = self.cleaned_data["password"]
    #     if data is not request.user.password:
    #         raise forms.ValidationError('wrong password')
    #     return data
    
'''
    User Creating form(Registration)
'''
DATA = (
    ('Patient', 'Patient'),
    ('Doctor', 'Doctor')
)


class User_register(UserCreationForm):
    who = forms.CharField(label='', label_suffix='', error_messages={'required': 'Select Your Role'}, widget=forms.RadioSelect(
        choices=DATA, attrs={'class':''}))
    password1 = forms.CharField(label='Enter Password', label_suffix='', error_messages={
                                'required': 'Password Must Be Required'}, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Confirm Password', label_suffix='', error_messages={
                                'required': 'Must Be Confirm Password'}, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = get_user_model()
        fields = ['who', 'username', 'email', 'first_name',
                  'last_name', 'password1', 'password2','is_active','is_staff','is_superuser']
        labels = {
            'username': 'Enter Username',
            'email': 'Enter Email Id',
            'first_name': 'Enter First Name',
            'last_name': 'Enter Last Name',
            # 'remind':'',
        }
        error_messages = {
            'username': {'required': 'Username is required'},
            'email': {'required': 'Email Address must be required'},
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            # 'remind':forms.BooleanField(required=True),

        }


"""
    User Change Password Form
"""


class Change_password_old_form(PasswordChangeForm):
    old_password = forms.CharField(label='Enter Old Password', label_suffix='', error_messages={
                                   'required': 'Must be Old Password'}, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholser': 'Enter Old Passworsd', 'autofocus': True}))
    new_password1 = forms.CharField(label='Enter New Password', label_suffix='', error_messages={
                                    'required': 'Required New Password'}, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholser': 'enter password'}))
    new_password2 = forms.CharField(label='Enter Confirm Password', label_suffix='', error_messages={
                                    'required': 'Must be Confirm Password'}, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholser': 'confirm password'}))

    class Meta:
        model = get_user_model()


"""
    User Reset Password Form
"""


class Change_password_new_form(SetPasswordForm):
    new_password1 = forms.CharField(label='Create Password', label_suffix='', error_messages={
                                    'required': 'Required New Password'}, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholser': 'Create Your Password', 'autofocus': True}))
    new_password2 = forms.CharField(label='Confirm Password', label_suffix='', error_messages={
                                    'required': 'Confirn New Password'}, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholser': 'Confirm Password'}))

    class Meta:
        model = get_user_model()


'''
    User Will Use This Form For Reset Password(Forget Password) 
'''


class Email_form(forms.ModelForm):
    # email = forms.CharField(label_suffix='Enter Email Address',error_messages={'required':'Enter Your Email Id'},widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = Use_email
        fields = ['email']
        labels = {
            'email': 'Enter Your Email Address'
        }
        error_messages = {
            'required': {'Email Address Is Required'}
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg', "aria-describedby": "inputGroup-sizing-lg", 'autofocus': True})
        }


'''
    User Profile Details
'''
DATA = [
    ('Male', 'Male'),
    ('Female', 'Female')
]
User = settings.AUTH_USER_MODEL

# 'gender', 'dob', 'mobile', 'address'
class Profile_form(UserChangeForm):
    password = None
    who = None
    gender = forms.ChoiceField(required=False,choices=DATA, label='Select Gender', label_suffix='', error_messages={'required': 'Select Your Gender'}, widget=forms.RadioSelect(
        attrs={"class":""}))
    # gender = forms.CharField(label='fwef')
# 'profile'
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'first_name', 'last_name','profile','mobile','dob','address']
        labels = {
            'email': 'Email address',
            'username': 'Your Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile': 'Select Profile Pic',
            # 'gender': 'Select Gender',
            'dob': 'Date Of Birth',
            'mobile': 'Enter Mobile Number',
            'address': 'Enter Address',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile': forms.FileInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }
        error_messages = {
            'profile':{'required':'Select image'},
        }
        # def clean(self):
        #     cleaned_data = super().clean()
        #     ph = self.cleaned_data['mobile']
        #     if len(ph) < 10:
        #         raise forms.ValidationError('Valid Number')
