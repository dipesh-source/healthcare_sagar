from django.db.models.query_utils import Q
import patient
from django.contrib.auth import get_user_model
from doctor.models import Post, Treatment
from django.shortcuts import redirect, render
from patient.models import Pat_inqu, Feedback, Vis_inquiry, Book_app
from patient.forms import Patient_inquiry_form, Visitor_inquiry_form, Feedback_form, Book_form
from django.http import HttpResponseRedirect, request
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.forms import Profile_form
from django.contrib.auth.models import User
from adminapp.models import Qualified
from django.conf import settings
from doctor.models import Doc_time
from django.core.paginator import Paginator
from django.core import paginator

def master(request):
    return render(request,'patient/pat_master.html')

'''
    patient inquiry form 
'''
# @login_required(login_url='/health/user_login/')


def homepage(request):
    if request.method == 'POST':
        pi = Patient_inquiry_form(request.POST)
        # vi = Visitor_inquiry_form(request.POST)
        if pi.is_valid():
            ab = pi.cleaned_data['about']
            mes = pi.cleaned_data['message']
            inq = Pat_inqu(patient=request.user, about=ab, message=mes)
            inq.save()
            messages.success(request, 'Successfully Post')
        # if vi.is_valid():
        #     nm = vi.cleaned_data['name']
        #     ph = vi.cleaned_data['phone']
        #     ab = vi.cleaned_data['about']
        #     me = vi.cleaned_data['message']
        #     viq = Vis_inquiry(name = nm,phone = ph,about = ab,message = me)
        #     viq.save()
        #     messages.success(request,'Successfully Post')
    else:
        pi = Patient_inquiry_form()
        # vi = Visitor_inquiry_form()
    qd = Qualified.objects.all()[:4]
    blo = Post.objects.all()[:3]
    doc = Book_app.objects.filter(patient=request.user.username).count()
    doc_da = User.objects.all( ).order_by('id')
    peg = Paginator(doc_da,2,orphans=0)
    req = request.GET.get('page')
    doc_data = peg.get_page(req)
    print('my all appointment ', doc)
    return render(request, 'patient/homepage.html', {'pform': pi, 'quali': qd, 'blog': blo, 'app': doc,'doc':doc_data})


'''
    Visitor inquiry
'''
# def visitor_inquiry_view(request):
#     if request.method == 'POST':
#         vi = Visitor_inquiry_form(request.POST)
#         if vi.is_valid():
#             nm = vi.cleaned_data['name']
#             ph = vi.cleaned_data['phone']
#             ab = vi.cleaned_data['about']
#             me = vi.cleaned_data['message']
#             viq = Vis_inquiry(name = nm,phone = ph,about = ab,message = me)
#             viq.save()
#             messages.info(request,'Inquiry successfully post')
#     else:
#         vi = Visitor_inquiry_form()
#     return render(request,'')

'''
    Patient homepage (website page of healthcare)
'''
# @login_required(login_url='/health/user_login/')

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
        return render(request, 'patient/user_profile.html', {'profile': uc})
    else:
        return HttpResponseRedirect('/health/user_login/')


'''
    patient feedback form
'''


def feedback(request):
    if request.method == 'POST':
        fb = Feedback_form(request.POST)
        if fb.is_valid():
            se = fb.cleaned_data['select']
            tx = fb.cleaned_data['text']
            ex = fb.cleaned_data['excplain']
            fbf = Feedback(patint=request.user, select=se,
                           text=tx, excplain=ex)
            fbf.save()
            fb = Feedback_form()
            messages.success(request, 'Thanks for your feedback')
    else:
        fb = Feedback_form()
    return render(request, 'patient/feedback.html', {'form': fb})


def find_doctor(request):
    qd = Qualified.objects.all()
    return render(request, 'patient/find_doc.html.', {'quali': qd})


'''
    Patient have got some doctor by searching
'''
# User = settings.AUTH_USER_MODEL
User = get_user_model()


@login_required(login_url='/health/user_login/')
def got_doc(request):
    query = request.GET['query']
    # print('###########################',query)
    if len(query) == 0:
        doctor = []
    else:
        doctor1 = User.objects.filter(master__icontains=query)
        doctor2 = User.objects.filter(username__icontains=query)
        doctor = doctor1.union(doctor2)
        # doc = doctor.strip()
        print('Doctor name is here ', doctor)
    parama = {'data': doctor, 'query': query}
    return render(request, 'patient/got_doc.html', parama)


'''
    Get all doctors time
'''


def get_doc_time(request, uid):
    print('User id ####################### ', uid)
    time = Doc_time.objects.filter(pk=uid).values(
        'day', 'start_time', 'end_time')
    print('################  Doctors time  ################')
    print(time)
    return render(request, 'patient/get_time.html', {'data': time})


'''
    Patient will book an appointment
'''


def book_app(request, uid):
    if request.method == 'POST':
        us = User.objects.get(username=uid)
        print('Antic data ###############',us)
        bf = Book_form(request.POST)
        if bf.is_valid():
            wh = bf.cleaned_data['when']
            dis = bf.cleaned_data['disease']
            wri = bf.cleaned_data['write']
            dc = Book_app(doc=us, doctor=us, doc_name=us.username, ph=us.mobile, mast=us.master, add=us.address, when=wh, in_day=us.in_day, out_day=us.out_day, start_time=us.start_time, end_time=us.end_time, pro=us.profile, patient=request.user.username, disease=dis, write=wri,
                          phone=request.user.mobile, gender=request.user.email, fnm=request.user.first_name, lnm=request.user.last_name, dob=request.user.dob, img=request.user.profile, address=request.user.address)

            doc_count = Book_app.objects.filter(doc_name=us.username).count()
            data = Book_app.objects.filter(
                Q(patient=request.user.username) & Q(doctor=us)).count()
            print('hello dipesh parmar ',data)
            if data >= 1:
                messages.error(
                    request, 'You are restricted, already you have two appointments ')
            else:
                dc.save()
                print('******************* Resticted user  *******************')
                print(us)
                messages.success(request, 'Appointment book successfully')
            bf = Book_form()
    else:
        bf = Book_form()
    usx = User.objects.filter(username=uid)
    print('my dipesh parmar user id ', usx)
    data = {'form': bf, 'data': usx}
    return render(request, 'patient/book_app.html', data)


'''
    doctor appointment data
'''

def pat_appoint(request):
    app = Book_app.objects.filter(patient=request.user.username)
    datax = Treatment.objects.filter(pat = request.user)
    return render(request, 'patient/appoint.html', {'data': app,'datax':datax})

'''
    Patient will delete doctor Treatment
'''
def delete_tret(request,tid):
    if request.method == 'POST':
        tre = Treatment.objects.filter(id=tid)
        tre.delete()
    return HttpResponseRedirect('/patient_site/my_appointment/')


'''
    Patient will delete his/her appointment
'''


def delete_pat_app(request, uid):
    if request.method == 'POST':
        bk = Book_app.objects.get(pk=uid)
        bk.delete()
    return HttpResponseRedirect('/patient_site/my_appointment/')


'''
    THis function will display all category of doctors
'''


@login_required(login_url='/health/user_login')
def all_doc_display(request):
    return render(request, 'patient/our_all_doc.html')


'''
    All individual doctors
'''

def  Neurology(request):
    cate1 = User.objects.filter(master = 'Neurology') 
    print('@@@@@@@@@@@@@@@@@@',cate1)
    return render(request,'patient/Neurology.html',{'data':cate1})


def  Ophthalmology(request):
    cate2 = User.objects.filter(master = 'Neurology') 
    return render(request,'patient/Ophthalmology.html',{'data':cate2})

    
def  Dermatology(request):
    cate3 = User.objects.filter(master = 'Dermatology') 
    return render(request,'patient/Dermatology.html',{'data':cate3})

    
def  Surgical(request):
    cate4 = User.objects.filter(master = 'Surgical') 
    return render(request,'patient/Surgical.html',{'data':cate4})

    
def  Cardiology(request):
    cate5 = User.objects.filter(master = 'Cardiology') 
    return render(request,'patient/Cardiology.html',{'data':cate5})

    
def  Dental(request):
    cate6 = User.objects.filter(master = 'Dental') 
    return render(request,'patient/Dental.html',{'data':cate6})

    
def Traumatology(request):
    cate7 = User.objects.filter(master = 'Traumatology') 
    return render(request,'patient/Traumatology.html',{'data':cate7})

    
def  General_Surgeon(request):
    cate8 = User.objects.filter(master = 'General_Surgeon') 
    return render(request,'patient/General_Surgeon.html',{'data':cate8})

    
def  Medicine_Specialists(request):
    cate9 = User.objects.filter(master = 'Medicine_Specialist') 
    return render(request,'patient/Medicine_Specialists.html',{'data':cate9})

    
def  Sports_Medicine_Specialists(request):
    cate10 = User.objects.filter(master = 'Sports_Medicine_Specialists') 
    return render(request,'patient/Sports_Medicine_Specialists.html',{'data':cate10})

    
def  Pediatrics(request):
    cate11 = User.objects.filter(master = 'Pediatrics') 
    return render(request,'patient/Pediatrics.html',{'data':cate11})

    
def  Nutrition_Counselling(request):
    cate12 = User.objects.filter(master = 'Nutrition_Counselling') 
    return render(request,'patient/Nutrition_Counselling.html',{'data':cate12})