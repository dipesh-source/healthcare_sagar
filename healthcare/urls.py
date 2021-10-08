from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls.conf import include
from account import views
from django.conf.urls.static import static
# from django.contrib.auth import views as aut
# from account.forms import User_authenticate
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from adminapp import views as vi
from patient import views as home
urlpatterns = [
    # path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('admin/', admin.site.urls),
    path('',home.homepage,name='home'),
    path('froala_editor/',include('froala_editor.urls')),
    path('user_register', views.register_view,name='register'),
    path('health/', include('account.urls')),
    path('admin_panel/',include('adminapp.urls')),
    path('doctor_panel/',include('doctor.urls')),
    path('patient_site/',include('patient.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
