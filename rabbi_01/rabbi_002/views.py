from django.http import HttpResponse
from django.shortcuts import render
from . forms import teacher_registration

# Create your views here.


def rabbi_0002(request):
    return render(request, "rabbi_002/rabbi_002.html")


def show_forms_data(request):
    if request.method == 'post':
        fm = teacher_registration(request.post)
        if fm.is_valid():
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['repassword'])
            
        
    else:
        fm = teacher_registration()
        print("this is get statement")
    #fm.order_fields(field_order=['email','last_name','first_name'])
    return render(request, 'rabbi_002/forms.html', {'forms':fm})
