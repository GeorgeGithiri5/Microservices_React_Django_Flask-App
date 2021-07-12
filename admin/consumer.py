import pika 

params = pika.URLParameters("amqps://bmlulnym:cO8LvzOx-aitUt-8R9gx5uKYkxfjJ4sG@snake.rmq2.cloudamqp.com/bmlulnym")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()