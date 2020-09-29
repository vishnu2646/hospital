from django.contrib import admin
from .models import Patient,Doctor,Admission,Appoinment
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Admission)
admin.site.register(Appoinment)