from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile
# Create your views here.

class SignUpForm(UserCreationForm):
    # pass
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, required=False, help_text="Enter a valid email address")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class Profile_form(forms.ModelForm):
    gend = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    user_status = [
        ("Active","Active"),
        ("Resigned","Resigned"),
        ("Retired","Retired"),
        ("Transferred","Transferred"),
        ("Admitted","Admitted"),
        ("Discharges","Discharged"),
        ("Dead","Dead"),
    ]

    profile_passport = forms.ImageField(required=False, label='Profile passport')
    means_of_identity = forms.ImageField(required=False, label='Means of Identity')
    particular = forms.FileField(required=False, label='Particulars')
    gender = forms.ChoiceField(choices=gend, required=True, widget=forms.RadioSelect)
    status = forms.ChoiceField(choices=user_status, required=False)
    class Meta:
        model = profile
        fields = [
            'status',
            'address',
            'phone',
            'date_of_birth',
            'gender',
            'nationality',
            'state',
            'means_of_identity',
            'particular',
            'profile_passport',
            'position',
            'department',
            'marital_status',
            'blood_group',
            'next_of_kin',
            'staff',
        ]

        widgets = {
            'date_of_birth':forms.NumberInput(attrs={'type':'date'}),
            
        }