from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def user_list(request):
    users = User.objects.all()
    return HttpResponse(users)