from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, request
from django.contrib import messages
from django.conf import settings
from django.http.response import HttpResponse
from account.models import Verify_req
from django.shortcuts import render
from account.forms import Profile_form,User_register, User_authenticate, Change_password_old_form,Change_password_new_form
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.models import Group, User
from account.forms import Email_form
from account.models import Use_email
from account.models import Doctor_validate
import uuid
"""
    User will Log-out from this function
"""


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/health/user_login/')


'''
    User profile function view (It will redirect after login)
'''


def patient_home(request):
    if request.user.is_authenticated:
        return render(request, 'account/home.html')
    else:
        return HttpResponseRedirect('/')

# SESSION_EXPIRE_AT_BROWSER_CLOSE
'''
    User Login Function View 
'''
User = settings.AUTH_USER_MODEL
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            ua = User_authenticate(request=request, data=request.POST)
            if ua.is_valid():
                at = authenticate(username=ua.cleaned_data['username'],password=ua.cleaned_data['password'])
                print('#####################',at)
                if at is not None:
                    # login(request,at)
                    print('**********************')
                    vr = Verify_req.objects.get(user=at)
                    if vr.check:
                        login(request, at)
                        if request.user.is_superuser:
                            return HttpResponseRedirect('/admin_panel/main_admin')
                        else:
                            return HttpResponseRedirect('/') 
                            # if  at.who == 'Doctor':
                            #     if Doctor_validate.check:
                            #         return HttpResponseRedirect('/doctor_panel/doctor_homepage/')
                            #     else:
                            #         return HttpResponse('Your are on padding..!')
                            # else:
                            #     return HttpResponseRedirect('/')
                    else:
                        messages.warning(request,'Not verified by email id')
                else:
                    messages.info(request,'Username and password incorrect')
        else:
            ua = User_authenticate()
        return render(request, 'account/login.html', {'form': ua})
    else:
        return HttpResponseRedirect('/')


'''
    New user registration function view 
'''


def register_view(request):
    if request.method == 'POST':
        ur = User_register(request.POST)
        if ur.is_valid():
            new_user = ur.save()
            print('The New Username is this ',new_user)
            messages.success(request, 'Your Account Was Created')
            uid = uuid.uuid4()
            vr = Verify_req(user=new_user, token=uid)
            vr.save()
            email_success(new_user.email, uid)
            if new_user.who == 'Doctor':
                doc = Doctor_validate(doctor = new_user)
                dp = Group.objects.get(name='doctor')
                new_user.groups.add(dp)
                
            return HttpResponseRedirect('/health/notify/')
    else:
        ur = User_register()
    return render(request, 'account/register.html', {'form': ur})

###################################################################################


###################################################################################



'''
    get verify user who have click on this email link to vetify account
'''


def success(request, token):
    ch = Verify_req.objects.filter(token=token).first()
    ch.check = True
    ch.save()
    messages.info(request, 'Now,Your Profile Is Successfully created')
    return HttpResponseRedirect('/health/user_login/')


"""
    send email to user who have register account
"""


def email_success(email, token):
    subject = 'Vetify Account To Healthcare'
    message = f'Click on this link to vetify your account http://127.0.0.1:8000/health/success/{token}'
    from_email = settings.EMAIL_HOST_USER
    recipirnt_list = [email]

    send_mail(subject=subject, message=message,
              from_email=from_email, recipient_list=recipirnt_list)


'''
    User Notify For Verification Email
'''
def Notify(request):
    return render(request, 'account/notify.html')

"""
    Change Password With Their Old Passord(Without Email)
"""
def change_pass_with_new(request):
    if request.method == "POST":
        cp = Change_password_new_form(user = request.user,data = request.POST)
        if cp.is_valid():
            cp.save()
            # update_session_auth_hash(request,cp)
            messages.success(request,"Password Successfully Update")
    else:
        cp = Change_password_new_form(user=request.user)
    return render(request,'account/new_pass.html',{'form':cp})

"""
    Change Password With Their Old Passord(Without Email)
"""
def change_pass_with_old(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            cp = Change_password_old_form(user = request.user,data = request.POST)
            if cp.is_valid():
                cp.save()
                update_session_auth_hash(request,cp)
                messages.success(request,"Password Successfully Update")
        else:
            cp = Change_password_old_form(user=request.user)
        return render(request,'account/old_pass.html',{'form':cp})
    else:
        return HttpResponseRedirect('/health/user_login/')


'''
    Reset User Password With Send Email
'''
def get_email_x(email):
    subject = 'Reset Password To Healthcare'
    message = f'Reset password,click on this link http://127.0.0.1:8000/health/with_new/'
    from_email = settings.EMAIL_HOST_USER
    recipirnt_list = [email]

    send_mail(subject=subject, message=message,
              from_email=from_email, recipient_list=recipirnt_list)

def email_password(request):
    # if request.user.is_authenticated:
        if request.method == 'POST':
            em = Email_form(request.POST)
            if em.is_valid():
                em = em.cleaned_data['email']
                uid = uuid.uuid4()
                get_email_x(em)
                # emf = Use_email(user="baki che",email = em,token=uid)
                # emf.save()
                return HttpResponseRedirect('/health/info_email/')
                # messages.info(request,'')
        else:
            em = Email_form()
        return render(request,'account/email.html',{'form':em})
    # else:
    #     return HttpResponseRedirect('/health/user_login/')
'''
    it will render Email Info template while reset password
'''
def email_info(request):
    return render(request,'account/email_info.html')



'''
    Health care Privacy
'''
def privacy(request):
    return render(request,'account/privacy.html')


'''
User = settings.AUTH_USER_MODEL
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            ua = User_authenticate(request=request, data=request.POST)
            if ua.is_valid():
                at = authenticate(username=ua.cleaned_data['username'],password=ua.cleaned_data['password'])
                print(at)
                if at is not None:
                    login(request,at)
                    if not request.user.is_superuser:
                        vr = Verify_req.objects.get(user=at)
                        if vr.check:
                            login(request, at)
                            # messages.success(request,'Welcome ')
                            if  at.who == 'Doctor':
                                return HttpResponseRedirect('/doctor_panel/doctor_info/')
                            else:
                                return HttpResponseRedirect('/')
                        else:
                            messages.warning(request,'Not verified by email id')
                    else:
                        return HttpResponseRedirect('/admin_panel/main_admin')

        else:
            ua = User_authenticate()
        return render(request, 'account/login.html', {'form': ua})
    else:
        return HttpResponseRedirect('/')
'''