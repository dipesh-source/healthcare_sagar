from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, User, UserManager
from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from datetime import datetime
from django.utils.functional import cached_property
'''
    Doctor verify
'''
class Doctor_validate(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    doctor = models.CharField(max_length=100)
    mas = models.CharField(max_length=100,null=True,blank=True)
    check = models.BooleanField(default=False)

'''
    User will use this Email for reset password(Forgot password)
''' 
class Use_email(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    token = models.CharField(max_length=100)

'''
    For email vetification class(Table)
'''

class Verify_req(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=120)
    check = models.BooleanField(default=False)

    def __str__(self):
        return self.token


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

DIS = (
    ('Neurology','Neurology'),
    ('Ophthalmology','Ophthalmology'),
    ('Dermatology','Dermatology'),
    ('Surgical','Surgical'),
    ('Cardiology','Cardiology'),
    ('Dental','Dental'),
    ('Traumatology','Traumatology'),
    ('General Surgeon','General Surgeon'),
    ('Medicine Specialists','Medicine Specialists'),
    ('Sports Medicine Specialists','Sports Medicine Specialists'),
    ('Pediatrics','Pediatrics'),
    ('Nutrition Counselling','Nutrition Counselling'),
)
DAYS = (
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
)
class CustomeUser(AbstractUser):
    username = None
    who = models.CharField(max_length=100)
    ###############
    master = models.CharField(choices=DIS,max_length=100) 
    clinic = models.CharField(max_length=100,null=True,blank=True)
    some  = models.CharField(max_length=100,null=True,blank=True)
    in_day = models.CharField(choices=DAYS,max_length=100)
    out_day = models.CharField(choices=DAYS,max_length=100)
    start_time = models.TimeField(default=datetime.now)
    end_time = models.TimeField(default=datetime.now)
    ###############
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100,unique=True)
    profile = models.ImageField(upload_to='profile')
    gender = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    mobile = models.PositiveBigIntegerField(null=True)
    address = models.CharField(max_length=200)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()