from django.shortcuts import render

from neverovertime.models import Project


def project_list(request):
    """
    show all projects in table
    """
    projects = Project.objects.all()

    return render(request, 'project_list.html', {'projects': projects})