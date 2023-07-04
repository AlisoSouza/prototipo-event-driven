from django.db import models
from uuid import uuid4
from .send import publish, channel


class Project(models.Model):

    TYPE_SUPPORT = "support"
    TYPE_CHATGPT = "lead_capture:chat_gpt"

    TYPE_CHOICES = [
        (TYPE_SUPPORT, "Support"),
        (TYPE_CHATGPT, "Chat GPT")
    ]

    uuid = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    template_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)

    @property
    def created(self):
        return self.created_on.strftime('%H:%M:%S.%f')

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, **kwargs):

        body = {
            "uuid": str(self.uuid),
            "name": self.name,
            "template_type": self.template_type
        }

        publish(body, channel, routing_key="create")
        # channel.basic_publish(exchange='project.topic', routing_key="", body=json.dumps(body))
        return super().save(force_insert, force_update, using, update_fields)

    def create_chats(self, sector_name):
        body = {"uuid": str(self.uuid), "sector": sector_name}
        publish(body, channel, routing_key="sector")
        return True

