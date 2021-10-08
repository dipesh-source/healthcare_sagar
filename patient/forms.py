from django import forms
from django.db.models import fields
from django.forms import widgets
from patient.models import Pat_inqu,Feedback,Vis_inquiry,Book_app

'''
    Book an appointment
'''
class Book_form(forms.ModelForm):
    disease = forms.CharField(required=False,label='disease',label_suffix='',widget=forms.TextInput(attrs={"class":'form-control'}),error_messages={'required':'Must be your disease name'})
    # link = forms.URLField(required=False,label='Send link',label_suffix='',widget=forms.URLInput(attrs={'class':'form-control','autofocus':True}))
    # do_this = forms.CharField(label='Send image',label_suffix='',widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Book_app
        fields = ['when','disease','write']
        labels = {
            'when':'Select Date',
            # 'disease':'Enter Disease name',
            'write':'Say something',
            # 'link':'Send Link',
            # 'one':'write',
            # 'two':'write',
            # 'three':'write',
            # 'four':'write',
            # 'five':'write',
        }
        widgets = {
            'when':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            # 'link':forms.TextInput(attrs={'class':'form-control'}),
            # 'one':forms.TextInput(attrs={'class':'form-control'}),
            # 'two':forms.TextInput(attrs={'class':'form-control'}),
            # 'three':forms.TextInput(attrs={'class':'form-control'}),
            # 'four':forms.TextInput(attrs={'class':'form-control'}),
            # 'five':forms.Textarea(attrs={'class':'form-control'}),

            # 'disease':forms.TextInput(attrs={'class':'form-control'}),
            'write':forms.Textarea(attrs={'class':'form-control'}),
        }
        help_text={
            'write':'Excplain your illness here...!'
        }
        error_messages = {
            'when':{'required':'Please,select date'},
            # 'disease':{'required':'Enter your disease name'},
        }


'''
    patient inquiry form
'''
class Patient_inquiry_form(forms.ModelForm):
    class Meta:
        model = Pat_inqu
        fields = ['about','message']
        labels = {
            'about':'Subject',
            'message':'inquiry'
        }
        error_messages = {
            'about':{'required':'Entre Subject'},
            'message':{'required':'Write your inquiry here..!'}
        }
        widgets = {
            'about':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'message':forms.Textarea(attrs={'class':'md-textarea form-control mb-0','rows':"5",'style':"padding-bottom: 1.2rem"})
        }
# class="md-textarea form-control mb-0" rows="5" style="padding-bottom: 1.2rem;"
'''
    visitor
'''
class Visitor_inquiry_form(forms.ModelForm):
    class Meta:
        model = Vis_inquiry
        fields = ['name','phone','about','message']
        labels = {
            'name':'Enter Your Name',
            'phone':'Enter Phone Number',
            'message':'Write Inquiry',
        }
        error_message = {
            'name':{'required':'Enter Your Name'},
            'phone':{'required':'Enter Mobile Number'},
            'message':{'required':'Write For Knowing Something..!'}
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'about':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'})
        }
'''
    Feedback form
'''
DATA = (
    ('Very bad','Very bad'),
    ('Nither good nor bad','Nither good nor bad'),
    ('Somewhat good','Somewhat good'),
    ('Very good','Very good')
)
class Feedback_form(forms.ModelForm):
    select = forms.CharField(label_suffix='',error_messages={'required':'Select One Option'},widget=forms.RadioSelect(choices=DATA,attrs={'class':''}))
    class Meta:
        model = Feedback
        fields = ['select','text','excplain']
        labels = {
            'text':'Say something',
            'excplain':'Your Feedback',
        }
        error_messages = {
            'excplain':{'required':'Feedback is required'}
        }
        widgets = {
            'text':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'excplain':forms.Textarea(attrs={'class':'form-control'})
        }
 