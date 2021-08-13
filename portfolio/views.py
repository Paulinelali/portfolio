from django.shortcuts import render
from django.http import HttpResponse
from .models import Projectmodel, myInfo

# Create your views here.

def index(request):
    Projects = Projectmodel.objects.all()
    picturemi = myInfo.objects.all()
    return render(request, "portfolio/index.html ", {"Projects":Projects,"myInfo":picturemi})


def about(request):
    Projects = Projectmodel.objects.all()
    picturemi = myInfo.objects.all()
    return render(request, "portfolio/about.html", {"Projects":Projects,"myInfo":picturemi})


def projects(request):
    Projects = Projectmodel.objects.all()
    picturemi = myInfo.objects.all()
    return render(request, "portfolio/projects.html", {"Projects":Projects,"myInfo":picturemi})

