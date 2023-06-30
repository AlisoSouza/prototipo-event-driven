import pika
import json
from datetime import datetime

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def consumer(ch, method, properties, body):
    data = body.decode()

    project = json.loads(data)
    template_type = project.get("template_type")
    name = project.get("name")

    if template_type:
        if template_type == "support":
            print(f"[+] Projeto: {name}: {datetime.now().strftime('%H:%M:%S.%f')} criando setor")
        elif template_type == "lead_capture:chat_gpt":
            print(f"[+] Projeto: {name}: {datetime.now().strftime('%H:%M:%S.%f')} ignora")

    ch.basic_ack(delivery_tag=method.delivery_tag)

# Configuração do consumidor
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='chats', on_message_callback=consumer)

# Inicia o consumidor em segundo plano
print("Chats aguardando mensagens...")
channel.start_consuming()