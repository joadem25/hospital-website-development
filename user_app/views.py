from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import SignUpForm, Profile_form, User_form
from .models import profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required

def myProfile(request, user_id):
    my_profile = profile.objects.all().filter(user_id=user_id)
    return render(request, "user_app/my_profile.html", {"myprofile": my_profile})

@login_required
# @transaction.atomic
def editProfile(request, user_id):
    # user = profile.objects.all().get(user_id= user_id)

    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(request.POST, instance=user)
        profile_form = Profile_form(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user_form.save()
                user.save()
            if profile_form.cleaned_data['staff']:
                user.is_staff = True
                user.save()
            else:
                user.is_staff = False
                user.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return myProfile(request, user_id)
        else:
            messages.error(request, ('Please correct the error below')) 
            return HttpResponsePermanentRedirect(reverse('edit_profile', args=(user_id,)))
    else:
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(instance=user)
        profile_form = Profile_form(instance=user.profile)
        return render(request, "user_app/edit_profile_form.html", {"user_form": user_form, "profile_form": profile_form})



@login_required
def deactivateProfile(request, user_id):
    my_profile = User.objects.only("is_active").filter(id = user_id)
    if my_profile.values()[0].get("is_active") == True:
        User.objects.only("is_active").filter(id=user_id).update(is_active=False)
    else:
        User.objects.only("is_active").filter(id=user_id).update(is_active=True)
    return HttpResponsePermanentRedirect(reverse("my_profile", args=user_id))
      

def displayStaffs(request):
    # pass
    staff = profile.objects.all().filter(staff=True)
    return render(request=request, template_name="user_app/display_staff.html", context={"staff": staff})

def displayPatients(request):
    # pass
    patient = profile.objects.all().filter(staff=False)
    return render(request=request, template_name="user_app/display_patient.html", context={"patient": patient})




