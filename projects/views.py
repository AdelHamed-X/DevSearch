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
    project = Project.objects.get(id=pk)

    context = {
        'project': project,
    }
    return render(request, 'projects/project.html', context)


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            project.featured_image = request.POST.get('featured_image')
            return redirect('projects')

    context = {
        'form': form,
    }
    return render(request, 'projects/project-form.html', context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form': form,
    }
    return render(request, 'projects/project_form.html', context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {
        'object': project,
    }
    return render(request, 'projects/delete.html', context)
