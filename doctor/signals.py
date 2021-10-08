from patient.models import Book_app
from django.db.models.signals import post_delete,pre_delete,post_save,pre_save
from django.contrib.auth import get_user_model
from django.conf import settings
# from django.http import request
from .models import Doc_time , Post
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.text import slugify

# User = get_user_model()
User = settings.AUTH_USER_MODEL


@receiver(pre_save,sender = Book_app) 
def book_pr(sender, instance,  **kwarg):
    print('######### signals PRE_SAVE #######')
    print('sender', sender)
    print('instance', instance)
    


@receiver(post_save,sender = Book_app) 
def book_pr(sender, instance, created, **kwarg):
    print('######### signals POST_SAVE #######')
    print('sender', sender)
    print('instance', instance)
    print('created', created)

@receiver(pre_save,sender = Post)
def doc_post(sender, instance, **kwags):
    if not instance.slug:
        instance.slug = slugify(instance.title)