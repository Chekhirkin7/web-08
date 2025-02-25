import pika
import json
from faker import Faker
from models import Contact

fake = Faker()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue', durable=True)
num_contacts = 10

for _ in range(num_contacts):
    contact = Contact(
        fullname=fake.name(),
        email=fake.email(),
    )
    contact.save()

    message = json.dumps({'contact_id': str(contact.id)})
    channel.basic_publish(exchange='', routing_key='email_queue', body=message, properties=pika.BasicProperties(delivery_mode=2))

connection.close()