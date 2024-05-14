from django.shortcuts import render, redirect
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

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def update_project(request, pk):
    projectobj = Project.objects.get(id=pk)
    form = ProjectForm(instance=projectobj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=projectobj)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)
