from django.contrib import admin
from django.urls import path, include, re_path
from hospitalapp.services_app import views as service_view

urlpatterns = [
    re_path(r'^create_service/', service_view.create_service, name="create_service"),
    re_path(r'^service/', service_view.displayServices, name = "service"),
    
    re_path(r'^book_service/(?P<user_id>\d+)/', service_view.bookService, name="book_service"),
    re_path(r'^appointment/(?P<user_id>\d+)/', service_view.bookingHistory, name="appointment"),
    re_path(r'^view_booking_detail/(?P<book_id>\d+)/', service_view.bookingDetails, name="view_booking_detail"),
    re_path(r'^edit_booking/(?P<book_id>\d+)/', service_view.editBookService, name="edit_booking"),
    re_path(r'^accept_booking/(?P<book_id>\d+)/', service_view.acceptBooking, name="accept_booking"),
    re_path(r'^decline_booking/(?P<book_id>\d+)/', service_view.declineBookService, name="decline_booking"),
    re_path(r'^doctor_booking/(?P<user_id>\d+)/', service_view.doctorBookService, name="doctor_booking"),
]