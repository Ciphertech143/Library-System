from django.shortcuts import render
from .forms import StudentForm


# Create your views here.
def students(request):
    return render (request, 'contact.html')

    def create_student (request):
         form = StudentForm()
    if request.metod=="POST":
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }        
    return render (request, 'create-contact.html', context)
         