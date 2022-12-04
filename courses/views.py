from django.shortcuts import render
from .forms import CourseForm
# Create your views here.
def courses (request):
    return render (request, 'courses.html')

def create_course (request):
    form= CourseForm()
    if request.metod=="POST":
        form= CourseForm(request.POST)
        if form.is_valid(
            form.save

    context = {
        'form': form
    }        
    return render (request, 'create-course.html', context)
        )