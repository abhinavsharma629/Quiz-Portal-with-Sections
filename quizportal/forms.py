from django import forms
from .models import Section1, Section2, Section3, Time
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
import csv
import os
from io import StringIO
import io
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from django.core import files
import requests
import tempfile

class OriginalRegistrationForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','first_name','password1','password2']


#Register User Manually
class RegistrationForm(forms.Form):
    file = forms.FileField()

    def save(self):
        file=self.cleaned_data["file"]
        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        for line in csv.reader(io_string, delimiter=','):
            p=User.objects.create(username=line[0], first_name=line[2])
            passw=str(line[0])+str(line[1])
            p.set_password(passw)
            p.save()



class LoginForm(AuthenticationForm):
    id_no=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    password=forms.CharField(widget=forms.PasswordInput(),required=True,max_length=100)


#Section1
class DataInput1(forms.Form):
    file = forms.FileField()

    #CSV File Save to DataBase
    def save(self):
        file=self.cleaned_data["file"]
        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        for line in csv.reader(io_string, delimiter=','):
            if(len(line[2]) != 0):
                p=Section1.objects.create(id_no=line[0], question=line[1], optionA=line[3], optionB=line[4], optionC=line[5], optionD=line[6], correct_choice=line[7])

                #Image Save 
                line1=line[2].split('/')
                openfile = open(line[2], 'rb')
                django_file = File(openfile)
                p.image.save(str(line1[len(line1)-1]), django_file, save=True)
                p.save()
            else:
                p=Section1(id_no=line[0], question=line[1], optionA=line[3],optionB=line[4], optionC=line[5], optionD=line[6], correct_choice=line[7])    
                p.save()


#Section2
class DataInput2(forms.Form):
    file = forms.FileField()

    #CSV File Save to DataBase
    def save(self):
        file=self.cleaned_data["file"]
        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        for line in csv.reader(io_string, delimiter=','):
            if(len(line[2]) != 0):
                p=Section2.objects.create(id_no=line[0], question=line[1], optionA=line[3], optionB=line[4], optionC=line[5], optionD=line[6], correct_choice=line[7])

                #Image Save 
                line1=line[2].split('/')
                openfile = open(line[2], 'rb')
                django_file = File(openfile)
                p.image.save(str(line1[len(line1)-1]), django_file, save=True)
                p.save()
            else:
                p=Section2(id_no=line[0], question=line[1], optionA=line[3],optionB=line[4], optionC=line[5], optionD=line[6], correct_choice=line[7])    
                p.save()


#Section3
class DataInput3(forms.Form):
    file = forms.FileField()

    #CSV File Save to DataBase
    def save(self):
        file=self.cleaned_data["file"]
        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        for line in csv.reader(io_string, delimiter=','):
            if(len(line[2]) != 0):
                p=Section3.objects.create(id_no=line[0], question=line[1], optionA=line[3], optionB=line[4], optionC=line[5], optionD=line[6], correct_choice=line[7])

                #Image Save 
                line1=line[2].split('/')
                openfile = open(line[2], 'rb')
                django_file = File(openfile)
                p.image.save(str(line1[len(line1)-1]), django_file, save=True)
                p.save()
            else:
                p=Section3(id_no=line[0], question=line[1], optionA=line[3],optionB=line[4], optionC=line[5], optionD=line[6], correct_choice=line[7])    
                p.save()

class TimeInput1(forms.Form):
    time=forms.TimeField()

    #End Time to DataBase
    def save(self):
        time=self.cleaned_data["time"]
        #print(e_time)
        obj,notif=Time.objects.get_or_create(s_no=1, time=time)
        if notif is True:
            obj.save()

class TimeInput2(forms.Form):
    time = forms.TimeField()

    #End Time to DataBase
    def save(self):
        time=self.cleaned_data["time"]
        obj,notif=Time.objects.get_or_create(s_no=2, time=time)
        if notif is True:
            obj.save()

class TimeInput3(forms.Form):
    time = forms.TimeField()

    #End Time to DataBase
    def save(self):
        time=self.cleaned_data["time"]
        obj,notif=Time.objects.get_or_create(s_no=3, time=time)
        if notif is True:
            obj.save()