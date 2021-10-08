from django.urls import path
from . import views

urlpatterns = [
    path('patient_feedback/',views.feedback,name='feed'),
    path('user_profile/',views.profile_view,name='profile'), 
    path('doctors/',views.find_doctor,name='finddoc'),
    path('our_doctors/',views.got_doc,name='got_doc'),
    path('get_doc_time/<int:uid>/',views.get_doc_time,name='get_time'),
    path('book_app/<str:uid>/',views.book_app,name='book'),
    path('my_appointment/',views.pat_appoint,name='appoint'),
    path('delete_patient_appointment/<int:uid>/',views.delete_pat_app,name = 'dele_app'),
    path('all_doctor_profile/',views.all_doc_display,name='all_doctor'),
    path('Neurology/',views.Neurology,name='Neurology'),
    path('Ophthalmology/',views.Ophthalmology,name='Ophthalmology'),
    path('Dermatology/',views.Dermatology,name='Dermatology'),
    path('Surgical/',views.Surgical,name='Surgical'),
    path('Cardiology/',views.Cardiology,name='Cardiology'),
    path('Dental/',views.Dental,name='Dental'),
    path('Traumatology/',views.Traumatology,name='Traumatology'),
    path('General_Surgeon/',views.General_Surgeon,name='General_Surgeon'),
    path('Medicine_Specialists',views.Medicine_Specialists,name='Medicine_Specialists'),
    path('Sports_Medicine_Specialists/',views.Sports_Medicine_Specialists,name='Sports_Medicine_Specialists'),
    path('Pediatrics/',views.Pediatrics,name='Pediatrics'),
    path('Nutrition_Counselling/',views.Nutrition_Counselling,name='Nutrition_Counselling'),
    path('master/',views.master),
    path('tre_data/<int:tid>/',views.delete_tret,name='tre'),
]


    