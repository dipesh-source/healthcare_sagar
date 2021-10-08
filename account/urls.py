from account import views
from django.urls import path
from account.forms import User_authenticate
urlpatterns = [
    path('success/<slug:token>/',views.success),
    path('notify/',views.Notify),
    path('patient_home/',views.patient_home),
    path('user_login/',views.login_view,name='login'),
    path('user_logout/',views.user_logout,name='ulogout'),
    path('with_old/',views.change_pass_with_old,name='withold'),
    path('with_new/',views.change_pass_with_new,name='withold'),
    path('get_email/',views.email_password,name='email'),
    path('info_email/',views.email_info),
    path('reset_password_check/',views.get_email_x),
    path('user_privacy/',views.privacy,name='privacy'),
     
]