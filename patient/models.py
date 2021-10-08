from django.db import models
from django.conf import settings
from django.utils.functional import cached_property
# from patient.models import Book_app
# Create your models here.
'''
    Patient Inquiry
'''
class Pat_inqu(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    about = models.CharField(max_length=100)
    message = models.CharField(max_length=10000)
    fate = models.DateTimeField(auto_now_add=True)
    
'''
    Vis inquiry
'''
class Vis_inquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    about = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    fdata = models.DateTimeField(auto_now_add=True)

'''
    Patient feedback Table
'''
WHAT = (
    ('Bad','Bad'),
    ('Average','Average'),
    ('Good','Good'),
)
class Feedback(models.Model):
    patint = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    select = models.CharField(max_length=100)
    text = models.CharField(max_length=100,null=True,blank=True)
    excplain = models.CharField(max_length=500)
    fdate = models.DateField(auto_now_add=True)

'''
    book an appointment
'''
# @cached_property
class Book_app(models.Model):
    doc = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    # pat = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    doctor = models.CharField(max_length=100)
    doc_name = models.CharField(max_length=100,default='') 
    ph = models.CharField(max_length=100,default='')
    mast = models.CharField(max_length=100,default='')
    add = models.CharField(max_length=100,default='')
    when = models.DateField()
    # link = models.CharField(max_length=100,null=True,blank=True)
    # do_this = models.ImageField(upload_to = 'do_this')
    # one = models.CharField(max_length=100,null=True,blank=True)
    # two = models.CharField(max_length=100,null=True,blank=True)
    # three = models.CharField(max_length=100,null=True,blank=True)
    # four = models.CharField(max_length=100,null=True,blank=True)
    # five = models.TextField(max_length=500,null=True,blank=True)
    in_day = models.CharField(max_length=100,null=True,blank=True)#####
    out_day = models.CharField(max_length=100,null=True,blank=True)#######
    start_time = models.CharField(max_length=100,null=True,blank=True)#######
    end_time  = models.CharField(max_length=100,null=True,blank=True)######
    patient = models.CharField(max_length=100) 
    disease = models.CharField(max_length=100,default='',null=True,blank=True)
    write = models.CharField(max_length=1000,default='',null=True,blank=True)
    pro = models.ImageField(upload_to = 'pat_img') ########
    gender = models.CharField(max_length=100)
    fnm = models.CharField(max_length=100)
    lnm = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'doc_img')
    address = models.CharField(max_length=100)
    check = models.BooleanField(default=False)
    fdate = models.DateTimeField(auto_now_add=True,auto_created=True)

    def count_similar_app(self):
        return Book_app.objects.filter(type=self.type).count()

    def __str__(self):
        return str(self.doc)
 