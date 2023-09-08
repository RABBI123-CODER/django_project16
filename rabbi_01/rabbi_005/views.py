from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def rabbi_0005(request):
    return render(request, 'rabbi_005/rabbi_005.html')
