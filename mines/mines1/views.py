from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *

# Create your views here.



def comite(request):
    if request.method == 'POST':
        form=SendForm(request.POST)
        print(request.POST)
        Send.objects.create( Email = request.POST.get("Email"),
        Contact = request.POST.get("Contact"),
        Message = request.POST.get("Message"))
        return render(request, 'comites.html')
    form = SendForm()
    context = {
        'form': form
    }

    return render(request, 'comite.html', context)
