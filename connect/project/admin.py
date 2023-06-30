from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "uuid", "created_on")

admin.site.register(Project, ProjectAdmin)