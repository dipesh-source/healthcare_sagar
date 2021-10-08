from django.urls import path
from doctor import views

urlpatterns = [
    path('doctor_homepage/',views.doctor_homepage,name='dochome'),
    path('doctor_post/',views.post_view,name='post_data'),
    path('doctor_time/',views.doc_time_view,name='time'),
    path('doctor_dashbord/',views.doc_dash,name='dash'),
    path('delete_time/<int:id>/',views.time_delete,name='tdelete'),
    path('update_time/<int:id>/',views.update_view,name='update'),
    path('doctor_profile/',views.profile_view,name='docprofile'),
    path('delete_appointment/<int:uid>/',views.delete_appointment,name='dele'),
    path('today_app/',views.today_app,name='today'),
    path('delete_today_app/<int:uid>/',views.delete_today_appointment,name="dele1"),
    path('update_app_date/<int:pid>/',views.update_app_date,name='update_date'),
    path('missing_app/',views.missing_app,name='missing'),
    path('delete_missing_app/<int:mid>/',views.delete_missing,name='miss_del'),
    path('give_treatment/<int:tid>/',views.doc_treatment,name='treatment'),
    path('missing_appointment_cover/<int:mid>/',views.missing_cover,name='miss_cover'),
    path('my_patients/',views.my_patient,name='my_pat'),
    path('patient_record_data/<str:rid>/',views.generate_record,name='record')
]
