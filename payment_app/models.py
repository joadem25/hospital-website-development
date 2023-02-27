from django.db import models
from hospitalapp.user_app.models import profile
from hospitalapp.services_app.models import BookingService 

# Create your models here.

class Payment_service(models.Model):
    payment_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(profile, null=True, unique=False, on_delete=models.CASCADE)
    booking = models.ForeignKey(BookingService, null=False, on_delete=models.CASCADE, unique=False)
    amount = models.BigIntegerField(unique=False, null=False)
    date_of_payment = models.DateField(auto_now_add=True, null=False)