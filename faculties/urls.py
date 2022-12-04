from django.urls import path

from .views import faculties

urlpatterns= [
    path ( '', faculties, name= 'faculty')
]