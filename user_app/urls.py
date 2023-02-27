from django.contrib import admin
from django.urls import path, include, re_path
from hospitalapp.user_app import views as user_view

urlpatterns = [
    re_path(r'^my_profile/(?P<user_id>\d+)/', user_view.myProfile, name="my_profile"),
    re_path(r'^edit_profile/(?P<user_id>\d+)/', user_view.editProfile, name="edit_profile"),
    re_path(r'^deactivate_profile/(?P<user_id>\d+)/', user_view.deactivateProfile, name="deactivate_profile"),
    re_path(r'^display_staffs/', user_view.displayStaffs, name="display_staffs"),
    re_path(r'^display_patients/', user_view.displayPatients, name="display_patients"),
]