from django.urls import path
from .views import index, project_view, create_chats

app_name = "project"

urlpatterns = [
    path("", index, name="projects"),
    path("projects/<uuid:uuid>/", project_view, name="project"),
    path("projects/<uuid:uuid>/criar-chats", create_chats, name="create_chats"),
]
