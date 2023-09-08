from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def rabbi_0003(request):
    return render(request, 'rabbi_003/rabbi_003.html')
