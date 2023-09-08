from django.http import HttpResponse
from django.shortcuts import render
from rabbi_001.models import teacher
# Create your views here.


def rabbi_0001(request):
    course = 'machine learning'
    Tclass = 21
    seat = 20
    duration = '2.5 month'
    # offering = {'what' :'it is my project'}
    offering = {'c': course, 'tl': Tclass, 'st': seat, 'd': duration}
    return render(request, 'rabbi_001/rabbi_001.html', context=offering)


def rabbi_0002(request):
    teacher = {'names': ['shakil', 'mejba', 'sohanur']}
    return render(request, 'rabbi_001/rabbi_002.html', context=teacher)


def rabbi_0003(request):
    return render(request, 'rabbi_001/rabbi_003.html')


def rabbi_0004(request):
    return render(request, 'rabbi_001/rabbi_004.html')
# class declaration from models.py in rabbi_001

def teacher_info(request):
    teach = teacher.objects.all()
    return render(request, 'rabbi_001/teacher.html', {'thr': teach})
    


