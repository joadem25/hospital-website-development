from django.contrib import admin
from django.urls import path, include, re_path
from hospitalapp.payment_app import views as pay_view

urlpatterns = [
    re_path(r'^make_payment/(?P<book_id>\d+)/', pay_view.makePayment, name="make_payment"),
    # re_path(r'^payment_success/(?P<book_id>\d+)/', pay_view.makePayment, name="payment_success"),
    re_path(r'^payment_fails/(?P<book_id>\d+)/', pay_view.makePayment, name="payment_fails"),
]