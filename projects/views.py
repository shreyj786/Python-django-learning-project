from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html',context  )


def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'single-project.html', {'project': projectObj})