from django import forms
from django.db import models
from django.contrib.auth.models import User
from hospitalapp.user_app.models import profile, User
from .models import Services, BookingService
# Create your views here.

class Services_form(forms.ModelForm):
    list_HOD =[]
    # staffs = profile.objects.all().filter(position="HOD")
    
    # for user in staffs:
    #     list_HOD.append((user['user_id'], user['user_id']))
    for user in profile.objects.filter(position="HOD"):
        list_HOD.append((user.user_id, user.user.first_name + " "+ user.user.last_name + " (" + user.department + ")"))
    

    service_logo = forms.FileField(required=False)
    HoD = forms.ChoiceField(choices=list_HOD, required=True)
    description = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Services
        fields = [
            'service_option',
            'HoD',
            'service_logo',
            'price',
            'description',
        ]

class BookService_form(forms.ModelForm):
     
    
    class Meta:
        model = BookingService
        fields = [
            'email',
            'date_created',
            'service_option',
            'description',
            

        ]

        widgets = {
           
            'date_created': forms.NumberInput(attrs={'type':'date'}),
            'description': forms.Textarea(attrs={'cols':60, 'row':5}),
            
        }

class EditBooksService_form(forms.ModelForm):
    list_resident =[(None ,"------")]
    list_consultant =[(None ,"------")]
    # staffs = profile.objects.filter(staff=True)
    
    # for user in staffs:
    #     if user.position == "Resident doctor":
    #         list_resident.append((user['user_id'], user['user_id']['Resident doctor']))
    #     elif user.position == "Consultant":
    #         list_consultant.append((user['user_id'], user['user_id']['Consultant']))
    # print(User.objects.filter(is_staff=True))
    # for user in User.objects.filter(is_staff=True):
    #     if user.position == "Resident doctor":
    #         list_resident.append(user.first_name + " " +user.last_name)
    #     elif user.position == "Consultant":
    #         list_resident.append(user.first_name + " " +user.last_name)
    for user in profile.objects.filter(position="Resident doctor"):
        list_resident.append((user.user_id, user.user.first_name + " "+ user.user.last_name + " (" + user.department + ")"))
    for user in profile.objects.filter(position="Consultant"):
        list_consultant.append((user.user_id, user.user.first_name + " "+ user.user.last_name + " (" + user.department + ")"))

    resident_doctor = forms.ChoiceField(choices=list_resident, required=False)
    consultant_doctor = forms.ChoiceField(choices=list_consultant, required=False)
    
    class Meta:
        model = BookingService
        fields = [
            # 'user',
            'email',
            'date_created',
            'service_option',
            'description',
            # 'resident_doctor',
            'approved_date',
            'approved_time',
            'served',
            'patient_status',
            'doctor_remark',
            'payment',
            'served',
            
        ]

        widgets = {
            'date_created': forms.NumberInput(attrs={'type':'date'}),
            'approved_date': forms.NumberInput(attrs={'type':'date'}),
            'approved_time': forms.NumberInput(attrs={'type':'time'}),
            'description': forms.Textarea(attrs={'cols':40, 'row':5}),
            'doctor_remark': forms.Textarea(attrs={'cols':30, 'row':5}),
        }
