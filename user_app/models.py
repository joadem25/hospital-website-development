from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class profile(models.Model):
    countries =[
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("United Kindom", "UK"),
        ("USA", "USA"),
    ]
    
    states =[
        ("Abia", "Abia"),
        ("Oyo", "Oyo"),
        ("Osun", "Osun"),
        ("Lagos", "Lagos"),
        ("Kano", "Kano"),
        ("Abuja", "Abuja"),
    ]
    
    position =[
        ("CMD", "CMD"),
        ("CMAC", "CMAC"),
        ("HOD", "HOD"),
        ("Consultant", "Consultant"),
        ("Resident Doctor", "Resident Doctor"),
        ("Accountant", "Accountant"),
        ("Secretary", "Secretary"),
        ("Admin Officer", "Admin Officer"),
        ("Clerical Officer", "Clerical Officer"),
        ("Medical Lab Scientist", "Medical Lab Scientist"),
        ("Phermacist", "Phermacist"),
        ("Scientific Officer", "Scientific Officer"),
    ]
    
    dept = [
        ("Emergency Care", "Emergency Care"),
        ("Operation & Surgery", "Operation & Surgery"),
        ("Outdoor Checkup", "Outdoor Checkup"),
        ("Ambulance service", "Ambulance service"),
        ("Medicine & Pharmacy", "Medicine & Pharmacy"),
        ("Blood tetsing", "Blood Testing"),
            
    ]
    
    ma_status =[
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorce", "Divorce"),
        ("Complicated", "Complicated"),
    ]
    blood_group = [
        ("A+", "A+"),
        ("B+", "B+"),
        ("O+", "O+"),
        ("AB+", "AB+"),
        ("A-", "A-"),
        ("B-", "B-"),
        ("O-", "O-"),
        ("AB+", "AB+"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(unique=False, max_length =20, null=True)
    address = models.CharField(unique=False, max_length =100, null=True)
    phone = models.CharField(unique=True, max_length=11, null=True)
    email = models.EmailField(unique=True, max_length=50, null=True)
    date_of_birth = models.DateField(unique=False, max_length=50, null=True)
    gender = models.CharField(unique = False, max_length=50)
    nationality = models.CharField(choices= countries, unique=False, max_length=50, null=True)
    state = models.CharField(choices= countries, unique=False, max_length=50, null=True)
    means_of_identity = models.ImageField(upload_to = "identityImage/", unique = False, null = True)
    particular = models.ImageField(upload_to = "particularsImage/", unique = False, null = True)
    profile_passport = models.ImageField(upload_to = "staffImage/", unique = False, null = True)
    position = models.CharField(choices=position, unique=False, max_length=25, null=True)
    department = models.CharField(choices=dept, unique=False, max_length=40, null=True)
    marital_status = models.CharField(choices = ma_status, unique=False, max_length=20, null=True)
    staff = models.BooleanField(default=False, unique=False)
    blood_group = models.CharField(choices=blood_group, unique=False, max_length=4, null=True)
    next_of_kin = models.CharField(unique=True, max_length=20, null=True)
    
    # Now this is wher the margic happens: we wil now define Signala so our profile model will be automatically created
    #
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)
            
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):    
        instance.profile.save()    
        
    



