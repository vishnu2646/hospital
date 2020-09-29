from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,UpdateView
from .models import Patient,Doctor,Appoinment,Admission
from .forms import (
    CreatePatientForm,
    AppoinmentForm,
    AdmissionForm
)
from twilio.rest import Client
from twilio.rest.authy.v1 import form
# Create your views here.
class PatientListView(ListView):
    model = Patient
    template_name = 'index.html'
    context_object_name = 'patients'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['report']
    template_name = 'forms/recordform.html' 

    def form_valid(self, form):
        form.save()
        return redirect('home')

def doctor(request):
    context = {
        'doctors':Doctor.objects.all()
    }
    return render(request,'doctor.html',context)

def createPatient(request):
    form = CreatePatientForm()
    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,'forms/patientform.html',{'form':form})



def Appoinments(request):
    form = AppoinmentForm()
    if request.method == 'POST':
        form = AppoinmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("detail")
    return render(request,'forms/appoinmentform.html',{'form':form})

def detail(request):
    context = {
        'appoinments':Appoinment.objects.all()
    }
    return render(request,'appoinment_details.html',context)

def accept(request):
    appoinments = Appoinment.objects.all()
    TWILIO_ACCOUNT_SID = 'AC1874fd1bea0e6cfd32bfeabf58c5e7bd'
    TWILIO_AUTH_TOKEN = '9926bbd45f36efe372c68ba83b3e6fb7'
    client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
    for appoinment in appoinments:
        message = client.messages.create(to='appoinments.phone', from_='12028581215', body='Your Appoinment is confirmed and do not delete the Message')
        print(message.sid)
    return redirect('detail')

def delete(request,id):
    appoinments = Appoinment.objects.get(id=id)
    appoinments.delete()
    TWILIO_ACCOUNT_SID = 'AC1874fd1bea0e6cfd32bfeabf58c5e7bd'
    TWILIO_AUTH_TOKEN = '9926bbd45f36efe372c68ba83b3e6fb7'
    client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
    for appoinment in appoinments:
        message = client.messages.create(to=appoinment.phone, from_='12028581215', body='Your Appoinment is Rejected,so please try again with other date or try again')
        print(message.sid)
    return redirect('detail')

def Admit(request):
    form = AdmissionForm()
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,'forms/addmission.html',{'form':form})

def admitdetails(request):
    context = {
        'admissions':Admission.objects.all()
    }
    return render(request,'admission_details.html',context)

def delete_view(request,id):
    patients = Patient.objects.get(id=id)
    patients.delete()
    return redirect('home')