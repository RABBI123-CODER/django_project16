
from django.urls import path
from . import views

urlpatterns = [
    path('fiff/', views.rabbi_0005, name = 'rabbi_5'),
]
