
import pika, json
from main import Product, db

conn_params = pika.ConnectionParameters(host='host.docker.internal')

connection = pika.BlockingConnection(conn_params)

chanel = connection.channel()

chanel.queue_declare(queue='main')

def callback(ch, methods, properties, body):
    print('Receive in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
    
    elif properties.content_type == 'product_updated':
      product = Product.query.get(data['id'])
      product.title = data['title']
      product.image = data['image']
      db.session.commit()

    
    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()


    


chanel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

chanel.start_consuming()

chanel.close()
