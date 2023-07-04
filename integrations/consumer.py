import os
import pika
import json
from datetime import datetime


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "integrations.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from project.models import Project
# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def log(message):
    print(f"[+] {datetime.now().strftime('%H:%M:%S.%f')} {message}")
# Declaração da fila

def consumer(ch, method, properties, body):
    data = body.decode()
    # raise Exception()
    project = json.loads(data)
    template_type = project.get("template_type")
    name = project.get("name")

    log(f"Criando Projeto: {name}")
    Project.objects.create(
        name=project.get("name"),
        template_type=project.get("template_type")
    )

    if template_type:
        if template_type == "support":
            log("integrando wpp demo")
        elif template_type == "lead_capture:chat_gpt":
            log("integrando chatgpt")


    ch.basic_ack(delivery_tag=method.delivery_tag)

# Configuração do consumidor
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='integrations', on_message_callback=consumer)

# Inicia o consumidor em segundo plano
print("\033[92m[+] (DJANGO) Integrations aguardando eventos...")
channel.start_consuming()
