import doctor
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from account.models import Use_email
from django.db.models.signals import post_delete,pre_delete,post_save,pre_save
 
'''
    Email for reset password
'''
@receiver(post_save,sender=Use_email)
def while_email(sender,instance,**kwargs):
    em = Use_email(user=instance)
    em.save()

User = get_user_model()
'''
    User Login Signal
'''
@receiver(user_logged_in, sender=User)
def while_register(sender, request, user, **kwargs):
    print('sender', sender)
    print('request', request)
    print('user', user)
    # doc = Doc_info(doctor = request.user)
    # doc.save()

'''
    User Logout Signals
'''
@receiver(user_logged_out,sender=User)
def while_logout(sender,request,user,**kwargs):
    print('sender', sender)
    print('request', request)
    print('user', user)


