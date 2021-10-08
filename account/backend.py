from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
 
class EmailAuthBackend():
    def authenticate(self,request,username,password):
        try:
            user = User.objects.get(email=username)
            success = user.check_password(password)
            if success:
                return user
        except User.DoesNotExist:
            pass
        return None
    
    def get_user(self, uid):
        try:
            return User.objects.get(pk=uid)
        except:
            return None
# class EmailBackend(object):
#     def authenticate(self,username=None,password=None,**kwargs):
#         try:
#             user = User.objects.get(email=username)
#         except User.MultipleObjectsReturned:
#             userv = User.objects.filter(email=username).order_by('id').first()
#         except User.DoesNotExist:
#             return None

#         if getattr(user, 'is_active') and user.check_password(password):
#             return user
#         return None
    
#     def get_user(self,user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
