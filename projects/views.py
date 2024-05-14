from django.shortcuts import render
from .models import Project, Tag, Review
from .forms import ProjectForm

# Create your views here.


def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects,
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projct = Project.objects.get(id=pk)
    context = {
        'project': projct,
    }
    return render(request, 'projects/project.html', context)


def create_project(request):
    form = ProjectForm()
    context = {'form': form}

    return render(request, 'projects/project_form.html', context)
