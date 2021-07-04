import json, os, django, pika

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

conn_params = pika.ConnectionParameters(host='host.docker.internal')

connection = pika.BlockingConnection(conn_params)

chanel = connection.channel()

chanel.queue_declare(queue='admin')


def callback(ch, methods, properties, body):
    print('Receive in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


chanel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

chanel.start_consuming()

chanel.close()
