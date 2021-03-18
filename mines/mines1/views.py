from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *

# Create your views here.



def comite(request):
    return render(request, 'comite.html')