import pika, json

connection = pika.BlockingConnection(pika.ConnectionParameters(
  host='host.docker.internal'
))

chanel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    chanel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)