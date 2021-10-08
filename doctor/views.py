import doctor
import patient
from patient.forms import Book_form
from django.db.models.query_utils import Q
from patient.views import book_app
from django.contrib import messages
from django.shortcuts import render
from doctor.forms import Post_form, Doc_time_form, Treatment_form
from doctor.models import Doc_time, Post, Treatment
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, request
from django.utils.text import slugify
from doctor.forms import Profile_form
from patient.models import Book_app
from datetime import date, datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from patient.models import Book_app
from patient.forms import Book_form
from datetime import date
 
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from .decorator import group_required

User = get_user_model()

@login_required(login_url='/health/user_login/')
# @staff_member_required()
# @group_required('doctor')
# @permission_required()
def doctor_homepage(request):
    app1 = Book_app.objects.filter( Q(doctor = request.user) & Q(when  = date.today()), check = False).count()
    app2 = Book_app.objects.filter( Q(doctor = request.user) & Q(when__gt  = date.today())).count()
    app3 = Book_app.objects.filter( Q(doctor = request.user) & Q(when__lt = date.today())).count()
    app4 = Book_app.objects.filter( Q(doctor = request.user) & Q(check = True)).count()
    data = {'today_app':app1,'pand_app':app2,'miss_app':app3,'mypat':app4}
    return render(request, 'doctor/dochome.html',data)


'''
    All Doctor's todays appointment 
'''
def today_app(request):
    today_im = Book_app.objects.filter( Q(doc = request.user) & Q(when = date.today()), check = False )
    print('my all todays app ' ,today_im)
    print('my all todays app ' ,request.user.email)
    return render(request,'doctor/today_app.html',{'today_my':today_im,'date':datetime.today()})


'''
    Upload Post By Doctor
'''


@login_required(login_url='/health/user_login/')
def post_view(request):
    if request.method == 'POST':
        pf = Post_form(request.POST, request.FILES)
        if pf.is_valid():
            ti = pf.cleaned_data['title']
            im = pf.cleaned_data['img']
            di = pf.cleaned_data['dis']
            inf = pf.cleaned_data['info']
            po = Post(doctor=request.user, title=ti, img=im, dis=di, info=inf)
            po.save()
            pf = Post_form
            messages.success(request, 'Successfully Post')
    else:
        pf = Post_form()
    return render(request, 'doctor/postinfo.html', {'form': pf})


'''
    Doctor available time view
'''


def doc_time_view(request):
    if request.method == 'POST':
        dt = Doc_time_form(request.POST)
        if dt.is_valid():
            dy = dt.cleaned_data['day']
            dd = dt.cleaned_data['date']
            stm = dt.cleaned_data['start_time']
            etm = dt.cleaned_data['end_time']
            dot = Doc_time(doctor=request.user, day=dy, date=dd,
                           start_time=stm, end_time=etm)
            dot.save()
            # messages.success(request,'Success')
            dt = Doc_time_form()
    else:
        dt = Doc_time_form()
    dot = Doc_time.objects.filter(doctor=request.user)
    
    print(dot)
    return render(request, 'doctor/doc_time.html', {'form': dt, 'data': dot})


'''
    Doctor dashbord
'''

@group_required('doctor')

def doc_dash(request):
    today = date.today()
    app = Book_app.objects.filter(Q(doc=request.user) & Q(when__gt = date.today()))
    data = User.objects.filter( book_app__doctor=request.user )
    print(app)
    print('we are right track')
    return render(request, 'doctor/docdash.html', {'data': app, 'today': data})


'''
    Doctor will Delete their time
'''


def time_delete(request, id):
    if request.method == 'POST':
        dt = Doc_time.objects.get(pk=id)
        dt.delete()
        return HttpResponseRedirect('/doctor_panel/doctor_time/')


'''
    Update doctor time table
'''


def update_view(request, id):
    if request.method == 'POST':
        dot = Doc_time.objects.get(pk=id)
        dt = Doc_time_form(request.POST, instance=dot)
        if dt.is_valid():
            dt.save()
            messages.success(request, 'Sucessfully Update')
    else:
        dot = Doc_time.objects.get(pk=id)
        dt = Doc_time_form(instance=dot)
    return render(request, 'doctor/update.html', {'form': dt})


'''
    All doctoor Proifle details
'''
'''
    User All Profile Details
'''
# @login_required(login_url='/health/user_login/')


def profile_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            uc = Profile_form(request.POST, request.FILES,
                              instance=request.user)
            if uc.is_valid():
                uc.save()
                messages.info(request, 'Profile SUccessfully Update...')
        else:
            uc = Profile_form(instance=request.user)
        return render(request, 'doctor/doc_profile.html', {'profile': uc})
    else:
        return HttpResponseRedirect('/health/user_login/')


'''
    Delete your patient appointment
'''

def delete_appointment(request, uid):
    if request.method == 'POST':
        bk = Book_app.objects.get(pk=uid)
        bk.delete()
        return HttpResponseRedirect('/doctor_panel/doctor_dashbord/')



'''
    Delete your patient only today appointment
'''

def delete_today_appointment(request, uid):
    if request.method == 'POST':
        bk = Book_app.objects.get(pk=uid)
        bk.delete()
        return HttpResponseRedirect('/doctor_panel/today_app/')

'''
    Doctor will update patient appointment date 
'''
def update_app_date(request,pid):
    if request.method == 'POST':
        bp = Book_app.objects.get(pk = pid)
        bof = Book_form(request.POST,instance=bp)
        if bof.is_valid():
            wh = bof.cleaned_data['when']
            book = Book_app.objects.filter(pk = bp.id).update(when = wh)
            messages.success(request,'Date successfully updated')
            return HttpResponseRedirect('/doctor_panel/doctor_homepage/')
    else:
        bp = Book_app.objects.get(pk = pid)
        bof = Book_form(instance=bp)
    return render(request,'doctor/update_date.html',{'form':bof})
'''
    Doctor will update patient appointment date 
'''
# def update_app_date(request,pid):
#     if request.method == 'POST':
#         bp = Book_app.objects.get(pk = pid)
#         print('after post first data @@@@@',bp)
#         bof = Book_form(request.POST,instance=bp)
#         if bof.is_valid():
#             wh = bof.cleaned_data['when']
#             bk = Book_app(when = wh)
#             bk.save()
#             # Book_app.objects.filter(pk = bp.id).update(when = wh)
#             # book.save()
#             messages.success(request,'Date successfully updated')
#     else:
#         bp = Book_app.objects.get(pk = pid)
#         print('first @@@@@@@@@@@@@@',bp)
#         bof = Book_form(instance=bp)
#         print('second @@@@@@@@@@@@',bof)
#     return render(request,'doctor/update_date.html',{'form':bof})


'''
    this function will return all missing appointment
'''
def missing_app(request):
    data = Book_app.objects.filter( Q(doctor = request.user) & Q(when__lt = date.today())) 
    return render(request,'doctor/missing_app.html',{'data':data })

'''
    Delete messing appointment
'''
def delete_missing(request,mid):
    if request.method == 'POST':
        bk = Book_app.objects.get(pk = mid)
        bk.delete()
        return HttpResponseRedirect('/doctor_panel/missing_app/')

'''
    Doctor will give treatment to his/her patient's via 
    this function
'''
def doc_treatment(request,tid):        
    if request.method == 'POST':
        bp = Book_app.objects.get(pk = tid)
        print('###### dipesh parmar  ######',bp.gender)
        # us = User.objects.get()
        # print('@@@@@@@@ dipesh parmar @@@@@@@',us)
        tf = Treatment_form(request.POST,request.FILES)
        if tf.is_valid():
            im = tf.cleaned_data['img']
            lk = tf.cleaned_data['link']
            on = tf.cleaned_data['one']
            tw = tf.cleaned_data['two']
            th = tf.cleaned_data['three']
            fo = tf.cleaned_data['four']
            tre = Treatment(doctor = bp,doc=bp,doc_name=bp.doc_name,doc_pic = bp.pro,phone = bp.ph,when=bp.when,master=bp.mast,disease=bp.disease,img = im,link = lk,one = on, two = tw, three = th,four = fo,pat_name = bp.patient,pat = bp.gender,success = True)
            print(tre)
            print('###### dipesh parmar  ######',bp.id)
            # print('################',bp.doctor)
            tre.save()
            fatch = Book_app.objects.filter( Q(doc = request.user) & Q(patient = bp.patient) ).update(check = True)
            print('ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')
            # datch = Book_app.objects.filter(  )
            messages.success(request,'Treatment Successfully')
            tf = Treatment_form()
    else:
        tf = Treatment_form()
    bk = Book_app.objects.filter(pk = tid)
    ghanu = {'data':bk,'form':tf}
    return render(request,'doctor/treatment.html',ghanu)
    
'''
    Doctor will recover missing appointment
'''
def missing_cover(request,mid):
    if request.method == 'POST':
        bp = Book_app.objects.get(pk = mid)
        bf = Book_form(request.POST,instance=bp)
        if bf.is_valid():
            wh = bf.cleaned_data['when']
            book = Book_app.objects.filter(pk = bp.id).update(when = wh)
            messages.success(request,'Date successfully updated')
            return HttpResponseRedirect('/doctor_panel/doctor_homepage/')
    else:
        bp = Book_app.objects.get(pk = mid)
        bf = Book_form(instance=bp)
    return render(request,'doctor/miss_cover.html',{'form':bf})


"""
    Doctor's private patient's
"""
def my_patient(request):
    private = Book_app.objects.filter( Q(doctor = request.user) & Q(check = True) )
    # succ = Treatment.objects.filter( Q(doc = request.user) & Q(success = True) )
    return render(request,'doctor/my_patient.html',{'datax':private})

'''
    Doctor will generate his/her patient record
'''
@permission_required('doctor.add_treatment',login_url='/admin_panel/get_error/')
def generate_record(request,rid):
    tre = Treatment.objects.filter( Q(doc = request.user) & Q(pat_name = rid) )
    print('################################',rid)
    return render(request,'doctor/record.html',{'data':tre})