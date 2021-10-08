from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import Widget
from adminapp.models import Gallery,Qualified
from django import forms
from froala_editor.widgets import FroalaEditor

class GalleryForm(forms.ModelForm):
  # about = forms.TextInput()
  data = forms.CharField(widget=FroalaEditor,label_suffix='')
  # content = forms.CharField(widget=FroalaEditor(options={'toolbarInline': True,}))
  class Meta:
    model = Gallery
    fields = ['about','data'] 
    labels = {
      'about':'What About ?'
    }
    widgets = {
      'about':forms.TextInput(attrs={'class':'form-control form-control-lg','autofocus':True})
    }
    error_messages = {
      'about': {'required':'Please enter title'}
    }
    label_suffixs = {
      'about':'',
    }

class Quali_form(forms.ModelForm):
  # img = forms.CharField(label='Select Img',label_suffix='',error_messages={'required':'select Image'},widget=forms.FileInput(attrs={'class':'form-control'}))
  # name = forms.CharField(label='Enter name',label_suffix='',error_messages={'required':'Enter Doctor name'},widget=forms.TextInput(attrs={'class':'form-control'}))
  # mas = forms.CharField(label='Enter Category',label_suffix='',error_messages={'required':'Enter Doctor Mastery'},widget=forms.TextInput(attrs={'class':'form-control'}))
  # text = forms.CharField(label='about doctor',label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))
  class Meta:
    model = Qualified
    fields = ['img','name','mas','text']
    labels = {
      'img':'Select Img',
      'name':'Enter name',
      'mas':'Enter Category',
      'text':'about doctor',
    }
    error_messages = {
      'img':{'required':'select Image'},
      'name':{'required':'Enter Doctor name'},
      'mas':{'required':'Enter Doctor Mastery'},
    }
    widgets = {
      'img':forms.FileInput(attrs={'class':'form-control'}),
      'name':forms.TextInput(attrs={'class':'form-control'}),
      'mas':forms.TextInput(attrs={'class':'form-control'}),
      'text':forms.TextInput(attrs={'class':'form-control'}),
    }