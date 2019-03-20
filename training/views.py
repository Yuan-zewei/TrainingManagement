from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse



# Create your views here.
def index(request):
    return render(request, 'training/index.html')



def register(request):
    phonenumbers = settings.AUTH_USER_MODEL.profile.phonenumber.all()
    user_phonenumber = request.GET.get(user=request.user)
    if user_phonenumber in phonenumbers:
        user_password = '123456'
        return JsonResponse({
            'user_password': user_password
        })
    else:
        return JsonResponse ({
            'message':'没有这个用户'
        })

