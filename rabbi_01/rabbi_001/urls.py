
from django.urls import path
from . import views

urlpatterns = [
    path('fi/', views.rabbi_0001, name = 'rabbi_1_1'),
    path('fir/', views.rabbi_0002, name = 'rabbi_1_2'),
    path('firs/', views.rabbi_0003, name = 'rabbi_1_3'),
    path('first/', views.rabbi_0004, name = 'rabbi_1_4'),
    path('tea/', views.teacher_info),

]
