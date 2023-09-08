from django.urls import path
from . import views

urlpatterns = [
    path('se/', views.rabbi_0002, name = 'rabbi_2'),
    path('f/', views.show_forms_data,),
]
