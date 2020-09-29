from django import forms
from .models import Patient,Appoinment,Admission
class CreatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name','age','gender','report']

class AppoinmentForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        fields = '__all__'

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'
