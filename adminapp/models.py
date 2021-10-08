from django.db import models
from django.conf import settings 
from django.db import models
from froala_editor.fields import FroalaField

class Gallery(models.Model):
  about = models.CharField(max_length=100)
  data = FroalaField(theme='dark')
  slug = models.SlugField(blank=True,null=True)
  content = FroalaField(options={
    'toolbarInline': True,
  },)
  fdate = models.DateTimeField(auto_now_add=True)

class Qualified(models.Model):
  doctor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
  img = models.ImageField(upload_to='quali_doc')
  name = models.CharField(max_length=100)
  mas = models.CharField(max_length=100)
  text = models.CharField(max_length=100,null=True,blank=True)
  fdate = models.DateTimeField(auto_now_add=True,auto_created=True)