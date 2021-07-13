import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

params = pika.URLParameters("amqps://bmlulnym:cO8LvzOx-aitUt-8R9gx5uKYkxfjJ4sG@snake.rmq2.cloudamqp.com/bmlulnym")

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)