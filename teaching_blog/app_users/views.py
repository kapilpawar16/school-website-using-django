from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("this is working properly")
    return render(request, 'home.html')

# Create your views here.
