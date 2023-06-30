from django.db import models
from uuid import uuid4


class Project(models.Model):
    uuid = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    template_type = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
