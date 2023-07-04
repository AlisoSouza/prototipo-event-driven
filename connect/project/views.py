from .models import Project
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import ProjectSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ProjetForm

class ProjectViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "uuid"


def index(request):
    template_name = "project/index.html"
    form = ProjetForm()
    if request.method == "POST":
        form = ProjetForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect(reverse('project:project', args=[project.uuid]))

    context = {
        "form": form
    }
    return render(request, template_name, context)

def project_view(request, uuid):
    print(uuid)
    template_name = "project/project.html"
    project = get_object_or_404(Project, uuid=uuid)
    context = {
        "project": project
    }
    return render(request, template_name, context)

def create_chats(request, uuid):
    project = get_object_or_404(Project, uuid=uuid)
    context = {
        "project": project
    }
    project.create_chats("Chats")
    return redirect(reverse('project:project', args=[project.uuid]))