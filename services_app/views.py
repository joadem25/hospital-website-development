from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Services, BookingService, User
from .forms import Services_form, BookService_form, EditBooksService_form
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail

@login_required
def create_service(request):
    if request.method == 'POST':
        service_form = Services_form(request.POST, request.FILES)
        if service_form.is_valid():
            service_form.save()
        return displayServices(request)
    else:
        service_form = Services_form()
        return render(request=request, template_name='service_app/create_service.html', context={"services":service_form})
@login_required
def displayServices(request):
    services = Services.objects.all()
    return render(request=request, template_name='service_app/service.html', context={"services":services})
@login_required
def bookService(request, user_id):
    if request.method == 'POST':
        booking_form = BookService_form(request.POST, request.FILES)
        if booking_form.is_valid():
            service = Services.objects.filter(service_option=booking_form.cleaned_data['service_option'])
            # print(service)
            booking = booking_form.save(commit=False)
            booking.profile_id = user_id
            booking.user_id =user_id
            booking.price = service.values()[0]['price']
            booking.hod_id = service.values()[0]['HoD_id']
            booking.save()
            messages.success(request, ('Appointment booked successfully'))
            return HttpResponsePermanentRedirect(reverse('appointment', args=(user_id,)))
        else:
            messages.error(request, ('Failed to create booking'))
            return HttpResponsePermanentRedirect(reverse('book_service', args=(user_id,)))
        
    else:
        booking_form = BookService_form()
        return render(request=request, template_name='service_app/booking_service.html', context={"booking_form":booking_form})
@login_required
def bookingHistory(request, user_id):
    booking_history = BookingService.objects.all().filter(user_id = user_id)
    return render(request=request, template_name='service_app/booking_history.html', context={"booking_history": booking_history})

@login_required
def editBookService(request, book_id):
    if request.method == 'POST':
        booking = get_object_or_404(BookingService, booking_id = book_id)
        booking_form = EditBooksService_form(request.POST, instance=booking)
        if booking_form.is_valid():
            email = booking_form.cleaned_data['email']
            booking_form.save()(commit=False)
            booking.consultant_doctor_id = booking_form.cleaned_data["consultant_doctor"]
            booking.resident_doctor_id = booking_form.cleaned_data["resident_doctor"]
            booking.save()
            # send mail notification to the patient
            send_mail(
            f'Booking Approved', # Subject of the mail
            'Dear {booking.user.first_name}, login to your portal to see information about your booking, Thanks', # Body of the mail
            'joadem25@gmail.com',
            [email],
            fail_silently = False,
            )

            # send a notification to the hod
            send_mail(
            f'Booking has been approved', # Subject of the mail
            'Dear HOD, Dr. {booking.consultant_doctor} accepted the patient named  {booking.user.first_name} you referrred to him. Thanks', # Body of the mail
            'joadem25@gmail.com',
            [email],
            fail_silently = False,
            )

            messages.success(request, ('Booking edited successfully'))
            return HttpResponsePermanentRedirect(reverse('view_booking_detail', args=(book_id,)))
        else:
            messages.error(request, ('Please correct the error below'))
            return HttpResponsePermanentRedirect(reverse('edit_booking', args=(book_id,)))
        
    else:
       
        booking = get_object_or_404(BookingService, booking_id = book_id)
        booking_form = EditBooksService_form(request.POST or None, instance=booking)
        return render(request, template_name='service_app/edit_booking_service_form.html', context={"booking_form":booking_form})

@login_required
def bookingDetails(request, book_id):
    booking_details = BookingService.objects.all().filter(booking_id=book_id)
    return render(request, template_name='service_app/booking_details.html', context={"booking_details": booking_details})

def acceptBooking(request, book_id):
    if request.method == 'POST':
        booking = get_object_or_404(BookingService, booking_id = book_id)
        booking_form = EditBooksService_form(request.POST, instance=booking)
        if booking_form.is_valid():
            email = booking_form.cleaned_data['email']
            booking_form.save()

            messages.success(request, ('Booking edited successfully'))
            return HttpResponsePermanentRedirect(reverse('view_booking_detail', args=(book_id,)))
        else:
            messages.error(request, ('Please correct the error below'))
            return HttpResponsePermanentRedirect(reverse('edit_booking', args=(book_id,)))
        
    else:
        booking = get_object_or_404(BookingService, booking_id = book_id)
        booking_form = EditBooksService_form(request.POST, instance=booking)
        return render(request, template_name='service_app/edit_booking_service_form.html', context={"booking_form":booking_form})

def declineBookService(request, book_id):
    pass

@login_required
def doctorBookService(request, user_id):
    
    if request.user.profile.position == "CMD":
        my_booking = BookingService.objects.all().order_by('date_created').reverse()
    elif request.user.profile.position == "HOD":
        print(BookingService.objects.filter())
        my_booking = BookingService.objects.filter(service_option=request.user.profile.department).order_by('date_created').reverse()
    elif request.user.profile.position == "Consultant":
        my_booking = BookingService.objects.filter(user_id=request.user.id, service_option=request.user.profile.department)
    else:
        my_booking = BookingService.objects.filter(user_id=request.user.id, service_option=request.user.profile.department)

    return render(request, template_name='service_app/my_patient_booking.html', context={"my_booking": my_booking})