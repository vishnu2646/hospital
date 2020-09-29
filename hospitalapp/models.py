from django.db import models
from django.urls import reverse
# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    report = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    qualification = models.CharField(max_length=20,blank=True,null=True)
    position = models.CharField(max_length=20,blank=True,null=True)
    spelization = models.CharField(max_length=50,null=True,blank=True)

class Appoinment(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    reason = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateField()
    phone = models.IntegerField(null=True,blank=True)

class Admission(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    reason = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateField()
    phone = models.IntegerField(null=True,blank=True)

