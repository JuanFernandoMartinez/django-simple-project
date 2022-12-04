from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task 
from .forms import createNewTaskForm


# Create your views here.



def hello(request):
    file_data = {
        'h_title': 'Home page Django',
        'title': 'Wellcome to my home page',
        'form': createNewTaskForm()
    }
    return render(request, 'index.html', file_data)

def projects(request):
    p = list(Task.objects.values())
    view_data = {
        'projects': p,
        'h_title': 'Projects List',
        'title': 'Projects dashboard'
    }
    return render(request, 'projects.html', view_data)
