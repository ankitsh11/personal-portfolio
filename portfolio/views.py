from django.shortcuts import render
from .models import Project

def Home(request):
    objectdisplay=Project.objects.all()
    return render(request,'portfolio/home.html',{'display':objectdisplay})
