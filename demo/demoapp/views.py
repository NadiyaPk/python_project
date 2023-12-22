from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from .models import Place
from .models import Team
def home(request):
    #name="india"
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
