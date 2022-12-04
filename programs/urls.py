from django.urls import path

from .views import programs
urlpatterns = [
    path('all/', programs)
]