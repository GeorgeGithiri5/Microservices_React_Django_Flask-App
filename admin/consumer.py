from main.main import Product
import pika , json

params = pika.URLParameters("amqps://bmlulnym:cO8LvzOx-aitUt-8R9gx5uKYkxfjJ4sG@snake.rmq2.cloudamqp.com/bmlulnym")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print("Product likes Increased")

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()