from django.shortcuts import render

# Create your views here.
def programs (request):
    return render (request, 'programs.html')
