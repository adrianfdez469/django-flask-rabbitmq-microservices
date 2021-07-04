import pika
import json

conn_params = pika.ConnectionParameters(host='host.docker.internal')

connection = pika.BlockingConnection(conn_params)

chanel = connection.channel()


def publish(method, body):

    properies = pika.BasicProperties(method)

    chanel.basic_publish(
        exchange='', routing_key='main', body=json.dumps(body), properties=properies
    )
