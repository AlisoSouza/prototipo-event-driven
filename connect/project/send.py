import pika
from pika.exceptions import StreamLostError, ChannelWrongStateError
import json


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def publish(body, channel, exchange: str = 'project.topic', routing_key: str = ''):
    try:
        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=json.dumps(body))
    except (StreamLostError, ChannelWrongStateError):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.basic_publish(exchange='project.topic', routing_key='', body=json.dumps(body))