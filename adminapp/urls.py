from django.urls import path
from adminapp import views 

urlpatterns = [
    path('main_admin/',views.admin_home,name='manage'),
    # path('admin_nes/',views.admin_home,name='adminapp'),
    path('get_error/',views.error_data),
    path('gallery_page/',views.gallery_view,name='gallery'),
    path('qualified/',views.qualified_doc,name='quali'),
    path('view_appoinement/',views.view_all_appointment,name='view'),
    path('filter_doctor/',views.filter_view_all_doctors,name='filter_doctor'),
    path('view_doctors/',views.all_doctors,name='doctors'),
    path('delete_doctor/<int:uid>/',views.delete_doctor,name='delete_doc'),
    path('view_patients/',views.view_all_patient,name='patients'),
    path('delete_patient/<int:uid>/',views.delete_patient,name='delete_pat'),
    path('read_feedack/',views.all_feedback,name='feedback'),
    path('delete_feedback/<int:uid>/',views.delete_feedback,name='fed_delete'),
    path('count_specialist/',views.count_specialist,name='counts'),
    path('final/',views.final),
]
 