from django.urls import path
from . import views
from .forms import createNewTaskForm


urlpatterns = [
    
    path('',views.hello),
    path('projects',views.projects)
]