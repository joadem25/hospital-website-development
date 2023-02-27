from django.db import models
from django.contrib.auth.models import User
from hospitalapp.user_app.models import profile
from django.utils import timezone
# Create your models here.

class GeneralPurpose:

    dept = [ 
        ("Emergency Care", "Emergency Care"),
        ("Operation & Surgery", "Operation & Surgery"),
        ("Outdoor Checkup", "Outdoor Checkup"),
        ("Ambulance service", "Ambulance service"),
        ("Medicine & Pharmacy", "Medicine & Pharmacy"),
        ("Blood tetsing", "Blood Testing"),
    ]

    user_status = [
        ("----------", "----------"),
        ("Booked for test", "Booked for test"),
        ("Transferred", "Transferred"),
        ("Admitted", "Admitted"),
        ("Discharged", "Discharged"),
        ("Dead", "Dead"),
    ]

class Services(models.Model):
    genP = GeneralPurpose()

    service_id = models.AutoField(primary_key=True)
    service_option = models.CharField(choices=genP.dept, max_length=20, null=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    HoD = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    service_logo = models.ImageField(upload_to="service_logo/", blank=True, null=True, unique=False)
    price = models.BigIntegerField(unique=False)
    description = models.CharField(max_length=100, blank=True, null=True)


class BookingService(models.Model):
    genP = GeneralPurpose()

    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, unique=False)
    profile = models.ForeignKey(User, related_name="profile_id", on_delete=models.CASCADE, null=False, blank=False, unique=False, default=1)
    hod = models.ForeignKey(User, related_name="hod", on_delete=models.CASCADE, null=False, blank=False, unique=False, default=1)
    service_option = models.CharField(choices=genP.dept, max_length=20, null=False, unique=False)
    date_created = models.DateField(default=timezone.now, null=True, blank=True)
    email = models.EmailField(max_length=50, null=False, unique=False)
    # consultant_doctor = models.ForeignKey(User, related_name="consultant_doctor", on_delete=models.CASCADE, null=True, blank=True, unique=False, max_length=20)
    # resident_doctor = models.ForeignKey(User, related_name="resident_doctor", on_delete=models.CASCADE, null=True, blank=True, unique=False, max_length=20)

    consultant_doctor = models.ForeignKey(User, related_name="consultant_doctor", on_delete=models.CASCADE, null=True, blank=True, unique=False, max_length=20)
    resident_doctor = models.ForeignKey(User, related_name="resident_doctor", on_delete=models.CASCADE, null=True, blank=True, unique=False, max_length=20)


    approved_date = models.DateField(null=True, blank=True, unique=False)
    approved_time = models.TimeField(null=True, blank=True, unique=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    payment = models.BooleanField(default=False, blank=True, null=True, unique=False)
    served = models.BooleanField(default=False, blank=True, null=True, unique=False)
    patient_status = models.CharField(choices=genP.user_status, max_length=20, null=True, unique=False)
    doctor_remark = models.CharField(max_length=100, blank=True, null=True, unique=False)
    price = models.BigIntegerField(unique=False, default=00)
