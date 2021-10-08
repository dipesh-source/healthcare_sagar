from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from adminapp.models import Gallery, Qualified
from adminapp.forms import GalleryForm, Quali_form
from django.shortcuts import render
from patient .models import Book_app
from patient.models import Feedback

"""
    Admin Panel Site(Page)
"""
User = get_user_model()


@user_passes_test(lambda u: u.is_superuser, login_url='/admin_panel/get_error/')
def admin_home(request):
    if request.user.is_superuser:
        count1 = User.objects.filter(who="Patient").count()
        count2 = User.objects.filter(who="Doctor").count()
        count3 = Book_app.objects.all().count()
        count4 = User.objects.count()
        print('#####################')
        return render(request, 'secure/admin_home.html', {'data1': count1, 'data2': count2, 'data3': count3, 'data4': count4})
    else:
        return HttpResponseRedirect('/admin_panel/get_error/')


'''
    it will genret error when user will try to user admin panel
'''


def error_data(request):
    return render(request, 'secure/error.html')


'''
    The Main Admin Panel Page / Admin Panel Site(Page)
'''


@user_passes_test(lambda u: u.is_superuser, login_url='/admin_panel/get_error/')
def home_admin(request):
    if request.user.is_superuser:
        return HttpResponseRedirect('/adminapp/main_admin/')
    else:
        return HttpResponseRedirect('/adminapp/get_error/')


'''
    Admin will managre their Gallery 
'''
# @login_required(login_url='/adminapp/get_error/')


@user_passes_test(lambda u: u.is_superuser, login_url='/admin_panel/get_error/')
def gallery_view(request):
    if request.method == 'POST':
        gf = GalleryForm(request.POST, request.FILES)
        if gf.is_valid():
            ab = gf.cleaned_data['about']
            dt = gf.cleaned_data['data']
            # so = gf.cleaned_data['content']
            ga = Gallery(about=ab, data=dt)
            ga.save()
    else:
        gf = GalleryForm()
    return render(request, 'secure/gallery.html', {'form': gf})

# Create your views here.


@user_passes_test(lambda u: u.is_superuser, login_url='/admin_panel/get_error/')
def final(request):
    if request.user.is_superuser:
        count1 = User.objects.filter(who="Patient").count()
        count2 = User.objects.filter(who="Doctor").count()
        count3 = User.objects.count()
        print('#####################')
        return render(request, 'secure/mastad.html', {'data1': count1, 'data2': count2, 'data3': count3})
    else:
        return HttpResponseRedirect('/admin_panel/get_error/')


@user_passes_test(lambda u: u.is_superuser, login_url='/admin_panel/get_error/')
def qualified_doc(request):
    if request.method == 'POST':
        qd = Quali_form(request.POST, request.FILES)
        if qd.is_valid():
            img = qd.cleaned_data['img']
            nm = qd.cleaned_data['name']
            ms = qd.cleaned_data['mas']
            tx = qd.cleaned_data['text']
            doc = Qualified(img=img, name=nm, mas=ms, text=tx)
            doc.save()
            qd = Quali_form()
            messages.success(request, 'Doctor successfully upload')
    else:
        qd = Quali_form()
    return render(request, 'secure/quali.html', {'form': qd})


'''
    admin will show all the appointment
'''

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_panel/get_error/')

def view_all_appointment(request):
    bk = Book_app.objects.all()
    return render(request, 'secure/view_appointment.html', {'data': bk})


'''
    Admin can show all the available doctor and delete any doctor
'''
@user_passes_test(lambda u: u.is_superuser, login_url='/admin_panel/get_error/')

def all_doctors(request):
    doc1 = User.objects.filter( who="Doctor" ) 
    doc2 = User.objects.filter(who = 'Doctor') and User.objects.values('username')
    doc3 = User.objects.filter(who = 'Doctor') and User.objects.values('master')
    print('################### my data ',doc2)
    # doc2 = User.objects.filter(who = 'Doctor')
    # doc3 = User.objects.values('master')
    # doc4 = User.objects.values('profile')
    # print('############',doc3)
    my_data = {'data1':doc1,'data2':doc2,'data3':doc3}
    return render(request,'secure/view_doctor.html',my_data)
'''
    Doctor can view all the patient
'''
@user_passes_test(lambda u: u.is_superuser, login_url='/admin_panel/get_error/')

def view_all_patient(request):
    pat = User.objects.filter(who = 'Patient')
    return render(request,'secure/view_patient.html',{'data':pat})


'''
    All doctors data with filter by specialist
'''
@user_passes_test(lambda u: u.is_superuser, login_url='/admin_panel/get_error/')

def filter_view_all_doctors(request):
    app1 = User.objects.filter(
        Q(who='Doctor') and Q(master='Neurology')).count()
    app2 = User.objects.filter(
        Q(who='Doctor') and Q(master='Opthalmology')).count()
    app3 = User.objects.filter(Q(who='Doctor') and Q(
        master='Nuclear Magnetic')).count()
    app4 = User.objects.filter(
        Q(who='Doctor') and Q(master='Surgical')).count()
    app5 = User.objects.filter(
        Q(who='Doctor') and Q(master='Cardiology')).count()
    app6 = User.objects.filter(Q(who='Doctor') and Q(master='Dental')).count()
    app7 = User.objects.filter(
        Q(who='Doctor') and Q(master='Traumatology')).count()
    app8 = User.objects.filter(Q(who='Doctor') and Q(
        master='General Surgeon')).count()
    app9 = User.objects.filter(Q(who='Doctor') and Q(
        master='Medicine Specialists')).count()
    app10 = User.objects.filter(Q(who='Doctor') and Q(
        master='Sports Medicine Specialists')).count()
    app11 = User.objects.filter(Q(who='Doctor') and Q(master='Other')).count()
    ######################################################################
    doc1 = User.objects.filter(Q(who='Doctor') and Q(master='Neurology'))
    doc2 = User.objects.filter(Q(who='Doctor') and Q(master='Opthalmology'))
    doc3 = User.objects.filter(
        Q(who='Doctor') and Q(master='Nuclear Magnetic'))
    doc4 = User.objects.filter(Q(who='Doctor') and Q(master='Surgical'))
    doc5 = User.objects.filter(Q(who='Doctor') and Q(master='Cardiology'))
    doc6 = User.objects.filter(Q(who='Doctor') and Q(master='Dental'))
    doc7 = User.objects.filter(Q(who='Doctor') and Q(master='Traumatology'))
    doc8 = User.objects.filter(Q(who='Doctor') and Q(master='General Surgeon'))
    doc9 = User.objects.filter(
        Q(who='Doctor') and Q(master='Medicine Specialists'))
    doc10 = User.objects.filter(Q(who='Doctor') and Q(
        master='Sports Medicine Specialists'))
    doc11 = User.objects.filter(Q(who='Doctor') and Q(master='Other'))

    # print('all doctors ')
    # print('Master doctors ',app1)
    # print('Master doctors ',app2)
    # print('Master doctors ',app3)
    # print('Master doctors ',app4)
    # print('Master doctors ',app5)
    # print('Master doctors ',app6)
    # print('Master doctors ',app7)
    # print('Master doctors ',app8)
    # print('Master doctors ',app9)
    # print('Master doctors ',app10)
    # print('Master doctors ',app11)
    all_data = {'mas1': app1, 'mas2': app2, 'mas3': app3, 'mas4': app4, 'mas5': app5, 'mas6': app6, 'mas7': app7, 'mas8': app8, 'mas9': app9, 'mas10': app10, 'mas11': app11,
                '11': doc1, 'd2': doc2, 'd3': doc3, 'd4': doc4, 'd5': doc5, 'd6': doc6, 'd7': doc7, 'd8': doc8, 'd9': doc9, 'd10': doc10, 'd11': doc11}
    return render(request, 'secure/filter_specialist.html', all_data)

'''
    Admin will delete doctors
'''
@user_passes_test(lambda u: u.is_superuser,login_url='/admin_panel/get_error/')
def delete_doctor(request,uid):
    if request.method == 'POST':
        us = User.objects.get(pk = uid)
        us.delete()
        return HttpResponseRedirect('/admin_panel/view_doctors/')

'''
    Admin will delete patient
'''
@user_passes_test(lambda u:u.is_superuser,login_url='/admin_panel/get_error/')
def delete_patient(request,uid):
    if request.method == 'POST':
        us = User.objects.get(pk = uid)
        us.delete()
        return HttpResponseRedirect('/admin_panel/view_patients/')

'''
    Admin will read all the patient feedback
'''
@user_passes_test(lambda u:u.is_superuser,login_url='/admin_panel/get_error/')
def all_feedback(request):
    fb = Feedback.objects.all()
    fb_count = Feedback.objects.count()
    return render(request,'secure/read_feedback.html',{'data':fb,'count_data':fb_count})

'''
    Delete patient feedback
'''
@user_passes_test(lambda u:u.is_superuser,login_url='/admin_panel/get_error/')
def delete_feedback(request,uid):
    if request.method == 'POST':
        fb = Feedback.objects.get(pk = uid)
        fb.delete()
        return HttpResponseRedirect('/admin_panel/read_feedack/')

'''
    This function will count all category of doctors 
'''
@user_passes_test(lambda u: u.is_superuser,login_url='/admin_panel/get_error/')
def count_specialist(reqeust):
    c1 = User.objects.filter(master = 'Neurology').count()
    c2 = User.objects.filter(master = 'Ophthalmology').count()
    c3 = User.objects.filter(master = 'Dermatology').count()
    c4 = User.objects.filter(master = 'Surgical').count()
    c5 = User.objects.filter(master = 'Cardiology').count()
    c6 = User.objects.filter(master = 'Dental').count()
    c7 = User.objects.filter(master = 'Traumatology').count()
    c8 = User.objects.filter(master = 'General Surgeon').count()
    c9 = User.objects.filter(master = 'Medicine Specialists').count()
    c10 = User.objects.filter(master = 'Sports Medicine Specialists').count()
    c11 = User.objects.filter(master = 'Pediatrics').count()
    c12 = User.objects.filter(master = 'Nutrition Counselling').count()
    all_count = {'sp1':c1,'sp2':c2,'sp3':c3,'sp4':c4,'sp5':c5,'sp6':c6,'sp7':c7,'sp8':c8,'sp9':c9,'sp10':c10,'sp11':c11,'sp12':c12}
     
    return render(reqeust,'secure/count_special.html',all_count)
