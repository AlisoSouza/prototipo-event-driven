from django.forms import ModelForm
from .models import Project


class ProjetForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "template_type"]
