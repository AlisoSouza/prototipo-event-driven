from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pika
import json
from datetime import datetime


app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

def migrate():
    with app.app_context():
        db.create_all()


class Project(db.Model):
    uuid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)


@app.route("/")
def hello_world():
    projects = Project.query.all()
    print(projects)
    return "<p>Hello, World!</p>"


""""""""""""""""""""
import pika
import json


# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaração da fila
# channel.queue_declare(queue='integrations')

# Consumidor (Consumer)
def log(message):
    print(f"[+] {datetime.now().strftime('%H:%M:%S.%f')} {message}")

def consumer(ch, method, properties, body):
    data = body.decode()
    project = json.loads(data)
    template_type = project.get("template_type")
    name = project.get("name")

    log(f"Criando Projeto: {name}")
    if template_type:
        if template_type == "support":
            log("Criando setor")
        elif template_type == "lead_capture:chat_gpt":
            ...

    ch.basic_ack(delivery_tag=method.delivery_tag)



if __name__ == "__main__":
    # Configuração do consumidor
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='chats', on_message_callback=consumer)

    # Inicia o consumidor em segundo plano
    print("\033[92m[+] (FLASK) Chats aguardando eventos...")
    channel.start_consuming()
    # migrate()