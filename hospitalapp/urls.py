from django.urls import path
from .views import PatientListView,PatientDetailView,PatientUpdateView
from . import views
urlpatterns = [
    path('',PatientListView.as_view(),name='home'),
    path('delete/<int:id>',views.delete_view),
    path('patient/<int:pk>/', PatientDetailView.as_view(),name='patient-detail'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name='patient-update'),
    path('patient/new/',views.createPatient,name='patient-create'),
    path('doctor/',views.doctor,name='doctor'),
    path('appoinment/',views.Appoinments,name='appoinment'),
    path('appoinment/detail/',views.detail,name='detail'),
    path('send/',views.accept),
    path('admission/',views.Admit,name='admission'),
    path('admission/details',views.admitdetails,name='admissiondetails'),
]