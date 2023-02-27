from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Payment_service
# from .forms import Services_form, BookService_form, EditBooksService_form
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.contrib import messages
from django.db import transaction
from hospitalapp.services_app.models import BookingService, Services
from django.core.mail import send_mail



# Create your views here.
@login_required
def makePayment(request, book_id):
    booking = BookingService.objects.get(booking_id=book_id)
    payment = Payment_service(profile_id=request.user.id, booking_id=book_id, amount=booking.price)
    payment.save()

    payment = BookingService.objects.filter(booking_id=book_id).update(payment=True)
    # send email to staff
    hod = Services.objects.get(service_option=booking.service_option)
    send_mail(
        'Booking has been made by a patient', # Subject of the mail
        'Dear Doctor, a patient just made a booking. Please, refer to a doctor, Thanks.', # Body of the mail
        'joadem25@gmail.com',
        [hod.HoD.email],
        fail_silently = False,
    )

    messages.success(request, ('Your payment was successful'))
    return render(request, "service_app/booking_history.html")

@login_required
def failPayment(request,book_id):
    messages.error(request, ('Your payment failed'))
    return HttpResponsePermanentRedirect(reverse('appointment', args=(request.user_id,)))